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

# Prefix command
@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(
        title= "Help",
        description="Here are some commands to get you started..\n\n"
                    "`.hello` - Greet the bot.\n"
                    "`.starthere` - Get started with cybersecurity. Know how to dive deeper into the field.\n"
                    "`.threats` - Learn about different threats and vulnerabilities and how to prevent them.\n"
                    "`.rtbt` - More about red teams and blue teams.\n"
                    "`.ctfs` - CTFS are a great to practice your skills. Learn more about them here.\n",
        color=discord.Color.from_str("#D14775")            
    )

    embed.add_field(name="\u200b", value="\u200b", inline=False)

    embed.add_field(
        name="General",
        value="Use `.info list` to get basic information and new updates added to Pawrge.\n",
        inline=False
    )

    embed.add_field(
        name="Tools",
        value="Use `.tool list` to get a list of different tools and their applications.\n",
        inline=False
    )

    embed.add_field(
        name="Linux",
        value="Use `.lx intro` to get started with Linux commands and their applications.\n",
        inline=False
    )

    embed.add_field(
        name="Networking",
        value="Use `.net list` to learn about networking concepts.\n",
        inline=False
    )

    embed.add_field(
        name="Cryptography",
        value="Use `.en list` to learn about cryptography concepts.\n",
        inline=False
    )

    embed.add_field(
        name="Digital Forensics",
        value="Use `.df list` to learn about digital forensics.\n",
        inline=False
    )

    embed.set_footer(text="Check out my creator's profile at https://github.com/amkx1")
    await ctx.send(embed=embed) 

# Slash command
@bot.tree.command(name="help", description="Show help information for Pawrge bot.")
async def help_slash(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Help",
        description="Here are some commands to get you started..\n\n"
                    "`.hello` - Greet the bot.\n"
                    "`.starthere` - Get started with cybersecurity.\n"
                    "`.threats` - Learn about different threats and vulnerabilities.\n"
                    "`.rtbt` - More about red teams and blue teams.\n"
                    "`.ctfs` - CTFS are a great way to practice your skills.\n",
        color=discord.Color.from_str("#D14775")
    )
    
    embed.add_field(name="\u200b", value="\u200b", inline=False)
    embed.add_field(
        name="General",
        value="Use `.info list` to get basic information and new updates added to Pawrge.\n",
        inline=False
    )

    embed.add_field(
        name="Tools",
        value="Use `.tool list` to get a list of different tools and their applications.\n",
        inline=False
    )       

    embed.add_field(
        name="Linux",
        value="Use `.lx intro` to get started with Linux commands and their applications.\n",
        inline=False
    )

    embed.add_field(
        name="Networking",
        value="Use `.net list` to learn about networking concepts.\n",
        inline=False
    )

    embed.add_field(
        name="Cryptography",
        value="Use `.en list` to learn about cryptography concepts.\n",
        inline=False
    )

    embed.add_field(
        name="Digital Forensics",
        value="Use `.df list` to learn about digital forensics.\n",
        inline=False
    )
    embed.set_footer(text="Check out my creator's profile at  https://github.com/amkx1")
    await interaction.response.send_message(embed=embed)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user.name}')

async def main():
    await bot.load_extension("actions.linux")
    await bot.start(TOKEN)

asyncio.run(main())

