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

    @app_commands.command(name="save", description="Save the current weights to roles.json")
    async def saveweight(self, interaction: discord.Interaction):
        if interaction.user.id != OWNER_USERID:
            await interaction.response.send_message("You must be the owner to use this command!", ephemeral=True)
            return
        import json
        import os
        ROLES_PATH = os.path.join(os.path.dirname(__file__), 'roles.json')
        with open(ROLES_PATH, 'r', encoding='utf-8') as f:
            roles_data = json.load(f)
        roles_data['weights'] = ROLE_WEIGHTS
        with open(ROLES_PATH, 'w', encoding='utf-8') as f:
            json.dump(roles_data, f, indent=2)
        await interaction.response.send_message("Role weights have been saved to roles.json.")

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
    # Gather top-level commands
    commands_list = [
        f"/{cmd.name} - {cmd.description}" for cmd in client.tree.get_commands() if not isinstance(cmd, app_commands.Group)
    ]
    # Gather weights subcommands
    weights_group = next((cmd for cmd in client.tree.get_commands() if cmd.name == "weights"), None)
    weights_subs = []
    if weights_group:
        weights_subs = [f"/weights {sub.name} - {sub.description}" for sub in weights_group.commands]
    help_text = "**Available Commands:**\n" + "\n".join(commands_list)
    if weights_subs:
        help_text += "\n\n**/weights subcommands:**\n" + "\n".join(weights_subs)
    help_text += "\n\n/help - Show this help message.\n"
    help_text += "sync (owner only, text command) - Sync the command tree with Discord."
    await interaction.response.send_message(help_text, ephemeral=True)

@client.command()
async def sync(ctx):
    print("sync command")
    if ctx.author.id == OWNER_USERID:
        await client.tree.sync()
        await ctx.send('Command tree synced.')
    else:
        await ctx.send('You must be the owner to use this command!')

@client.tree.command(name="newgame", description="Get a link to start a new ONU Werewolf game")
async def newgame(interaction: discord.Interaction):
    url = "https://netgames.io/games/onu-werewolf/new"
    await interaction.response.send_message(f"[Start a new game]({url})", ephemeral=True)

client.run(DISCORD_TOKEN)