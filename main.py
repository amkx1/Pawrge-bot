import asyncio
import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '.', intents=intents)

bot.remove_command('help')

# Prefix command
@bot.command(name='hello')
async def greetings(ctx):
    embed = discord.Embed(
        title = "Hello!",
        description="I'm Pawrge, a cybersecurity bot designed to help you with your learning! Type `.help` to learn more.",
        color=discord.Color.from_str("#D14775")
    )
    await ctx.send(embed=embed) 

# Slash command: /hello
@bot.tree.command(name="hello", description="Say hello to Pawrge!")
async def hello_slash(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Hello!",
        description="I'm Pawrge, a cybersecurity bot designed to help you with your learning! Type `/help` or `.help` to learn more.",
        color=discord.Color.from_str("#D14775")
    )
    await interaction.response.send_message(embed=embed)

def help_embed():
    embed = discord.Embed(
        title= "Help",
        description="Here are some commands to get you started..\n\n"
                    "`hello` - Greet the bot.\n"
                    "`starthere` - Get started with cybersecurity. Know how to dive deeper into the field.\n"
                    "`threats` - Learn about different threats and vulnerabilities and how to prevent them.\n"
                    "`rtbt` - More about red teams and blue teams.\n"
                    "`ctfs` - CTFS are a great to practice your skills. Learn more about them here.\n",
        color=discord.Color.from_str("#D14775")            
    )

    embed.add_field(name="\u200b", value="\u200b", inline=False)

    embed.add_field(
        name="General",
        value="Use `info list` to get basic information and new updates added to Pawrge.\n",
        inline=False
    )

    embed.add_field(
        name="Tools",
        value="Use `tool list` to get a list of different tools and their applications.\n",
        inline=False
    )

    embed.add_field(
        name="Linux",
        value="Use `lx intro` to get started with Linux commands and their applications.\n",
        inline=False
    )

    embed.add_field(
        name="Networking",
        value="Use `net list` to learn about networking concepts.\n",
        inline=False
    )

    embed.add_field(
        name="Cryptography",
        value="Use `en list` to learn about cryptography concepts.\n",
        inline=False
    )

    embed.add_field(
        name="Digital Forensics",
        value="Use `df list` to learn about digital forensics.\n",
        inline=False
    )

    embed.set_footer(text="Check out my creator's profile [here](https://github.com/amkx1)")
    return embed

# Prefix command
@bot.command(name='help')
async def help(ctx):
    embed = help_embed()
    await ctx.send(embed=embed)
     

# Slash command
@bot.tree.command(name="help", description="Show help information for Pawrge bot.")
async def help_slash(interaction: discord.Interaction):
    embed = help_embed()
    await interaction.response.send_message(embed=embed)

def getcontent_embed(file_path, default_title):
    if not os.path.exists(file_path):
        return discord.Embed(
            title="404",
            description="Unknown command or file not found",
            color=discord.Color.from_str("#D14775")
        )
    
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        title = lines[0].strip().lstrip("#").strip() if lines else default_title
        description = "".join(lines[1:]).strip() if len(lines) > 1 else "No content found."

    embed = discord.Embed(
        title=title,
        description=description[:4096],
        color=discord.Color.from_str("#D14775")
    )
    return embed

@bot.command(name='starthere')
async def starthere(ctx):
    embed = getcontent_embed("intel/general/starthere.md", default_title="Start Here")
    await ctx.send(embed=embed)

@bot.tree.command(name="starthere", description="Get started with cybersecurity.")
async def starthere_slash(interaction: discord.Interaction):
    embed = getcontent_embed("intel/general/starthere.md", default_title="Start Here")
    await interaction.response.send_message(embed=embed)

@bot.command(name='threats')
async def threats(ctx):
    embed = getcontent_embed("intel/general/threats.md", default_title="Threats and Vulnerabilities")
    await ctx.send(embed=embed)

@bot.tree.command(name="threats", description="Learn about threats and vulnerabilities.")
async def threats_slash(interaction: discord.Interaction):
    embed = getcontent_embed("intel/general/threats.md", default_title="Threats and Vulnerabilities")
    await interaction.response.send_message(embed=embed)

@bot.command(name='rtbt')
async def rtbt(ctx):
    embed = getcontent_embed("intel/general/rtbt.md", default_title="Red Teams and Blue Teams")
    await ctx.send(embed=embed)

@bot.tree.command(name="rtbt", description="Learn about Red Teams and Blue Teams.")
async def rtbt_slash(interaction: discord.Interaction):
    embed = getcontent_embed("intel/general/rtbt.md", default_title="Red Teams and Blue Teams")
    await interaction.response.send_message(embed=embed)

@bot.command(name='ctfs')
async def ctfs(ctx):
    embed = getcontent_embed("intel/general/ctfs.md", default_title="Capture The Flag (CTF)")
    await ctx.send(embed=embed)

@bot.tree.command(name="ctfs", description="Learn about Capture The Flag (CTF) challenges.")
async def ctfs_slash(interaction: discord.Interaction):
    embed = getcontent_embed("intel/general/ctfs.md", default_title="Capture The Flag (CTF)")
    await interaction.response.send_message(embed=embed)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user.name}')

async def main():
    await bot.load_extension("actions.linux")
    await bot.start(TOKEN)

asyncio.run(main())

