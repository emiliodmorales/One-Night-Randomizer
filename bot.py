import asyncio
from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
from discord import app_commands
from randomizer import ROLE_WEIGHTS, randomize as randomRoles

load_dotenv()

OWNER_USERID_ENV = os.getenv('OWNER_USERID')
if OWNER_USERID_ENV is None:
    raise ValueError("OWNER_USERID environment variable not set")
OWNER_USERID: int = int(OWNER_USERID_ENV)

DISCORD_TOKEN_ENV = os.getenv('DISCORD_TOKEN')
if DISCORD_TOKEN_ENV is None:
    raise ValueError("DISCORD_TOKEN environment variable not set")
DISCORD_TOKEN: str = DISCORD_TOKEN_ENV

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

class WeightsGroup(app_commands.Group):
    def __init__(self):
        super().__init__(name="weights", description="Role weights commands")

    @app_commands.command(name="show", description="Show the weights for each role")
    async def show(self, interaction: discord.Interaction):
        print(f'Sending role weights')
        if isinstance(ROLE_WEIGHTS, dict):
            formatted = '\n'.join(f"{role}: {weight}" for role, weight in ROLE_WEIGHTS.items())
        elif isinstance(ROLE_WEIGHTS, list):
            formatted = '\n'.join(str(item) for item in ROLE_WEIGHTS)
        else:
            formatted = str(ROLE_WEIGHTS)
        await interaction.response.send_message(f'```\n{formatted}```')

    @app_commands.command(name="set", description="Set the weight for a specific role")
    async def set(self, interaction: discord.Interaction, role: str, weight: float):
        # if interaction.user.id != OWNER_USERID:
        #     await interaction.response.send_message("You must be the owner to use this command!", ephemeral=True)
        #     return
        if role not in ROLE_WEIGHTS:
            await interaction.response.send_message(f"Role '{role}' not found.", ephemeral=True)
            return
        ROLE_WEIGHTS[role] = weight
        await interaction.response.send_message(f"Set weight for '{role}' to {weight}.")

    @app_commands.command(name="increase", description="Increase the weight for a specific role")
    async def increase(self, interaction: discord.Interaction, role: str, amount: float):
        # if interaction.user.id != OWNER_USERID:
        #     await interaction.response.send_message("You must be the owner to use this command!", ephemeral=True)
        #     return
        if role not in ROLE_WEIGHTS:
            await interaction.response.send_message(f"Role '{role}' not found.", ephemeral=True)
            return
        ROLE_WEIGHTS[role] += amount
        await interaction.response.send_message(f"Increased weight for '{role}' by {amount}. New weight: {ROLE_WEIGHTS[role]}")

    @app_commands.command(name="decrease", description="Decrease the weight for a specific role")
    async def decrease(self, interaction: discord.Interaction, role: str, amount: float):
        # if interaction.user.id != OWNER_USERID:
        #     await interaction.response.send_message("You must be the owner to use this command!", ephemeral=True)
        #     return
        if role not in ROLE_WEIGHTS:
            await interaction.response.send_message(f"Role '{role}' not found.", ephemeral=True)
            return
        ROLE_WEIGHTS[role] -= amount
        await interaction.response.send_message(f"Decreased weight for '{role}' by {amount}. New weight: {ROLE_WEIGHTS[role]}")

    @app_commands.command(name="reset", description="Reset all role weights to default")
    async def reset(self, interaction: discord.Interaction):
        # if interaction.user.id != OWNER_USERID:
        #     await interaction.response.send_message("You must be the owner to use this command!", ephemeral=True)
        #     return
        from importlib import reload
        import randomizer
        reload(randomizer)
        global ROLE_WEIGHTS
        ROLE_WEIGHTS = randomizer.ROLE_WEIGHTS.copy()
        await interaction.response.send_message("All role weights have been reset to default.")

# Register the group
client.tree.add_command(WeightsGroup())

@client.event
async def on_ready():
    print(f'Logged On as {client.user}')

@client.tree.command(name="randomize", description="random role list")
async def randomize(interaction: discord.Interaction, players: int):
    print(f'Making a role list for {players} players')
    
    if players < 1:
        await interaction.response.send_message("Number of players must be positive!", ephemeral=True)
        return

    loop = asyncio.get_running_loop()
    roles = await loop.run_in_executor(None, randomRoles, players) 

    if roles.startswith("Not enough players") or roles.startswith("Too many players"):
        await interaction.response.send_message(roles, ephemeral=True)
    else:
        await interaction.response.send_message(f'```\n{roles}```')
    print(roles)

@client.tree.command(name="help", description="show help for commands")
async def help_command(interaction: discord.Interaction):
    help_text = (
        "**Available Commands:**\n"
        "/randomize <players> - Generate a random role list for the given number of players.\n"
        "\n**/weights subcommands:**\n"
        "/weights show - Show the weights for each role.\n"
        "/weights set <role> <weight> - Set the weight for a specific role (owner only).\n"
        "/weights increase <role> <amount> - Increase the weight for a role by a given amount (owner only).\n"
        "/weights decrease <role> <amount> - Decrease the weight for a role by a given amount (owner only).\n"
        "/weights reset - Reset all role weights to default (owner only).\n"
        "\n/help - Show this help message.\n"
        "sync (owner only, text command) - Sync the command tree with Discord."
    )
    await interaction.response.send_message(help_text, ephemeral=True)

@client.command()
async def sync(ctx):
    print("sync command")
    if ctx.author.id == OWNER_USERID:
        await client.tree.sync()
        await ctx.send('Command tree synced.')
    else:
        await ctx.send('You must be the owner to use this command!')

client.run(DISCORD_TOKEN)