import asyncio
from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
from randomizer import randomize as randomRoles

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

@client.command()
async def sync(ctx):
    print("sync command")
    if ctx.author.id == OWNER_USERID:
        await client.tree.sync()
        await ctx.send('Command tree synced.')
    else:
        await ctx.send('You must be the owner to use this command!')

client.run(DISCORD_TOKEN)