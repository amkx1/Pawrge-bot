import os
import discord
from discord.ext import commands
from discord import app_commands

class LinuxCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Prefix command
    @commands.command(name="lx")
    async def lx_prefix(self, ctx, subcommand: str = None):
        await self.send_linux_info(ctx, subcommand)

    # Slash command
    @app_commands.command(name="lx", description="Linux commands")
    @app_commands.describe(subcommand = "What do you want to know about?")
    @app_commands.choices(subcommand=[
        app_commands.Choice(name="intro", value="intro"),
        app_commands.Choice(name="index", value="index"),
        app_commands.Choice(name="basics", value="basics"),
        app_commands.Choice(name="perms", value="perms"),
        app_commands.Choice(name="cronj", value="cronj"),
        app_commands.Choice(name="bash", value="bash"),
        app_commands.Choice(name="processes", value="processes"),
        app_commands.Choice(name="filesys", value="filesys")
    ])
    async def lx_slash(self, interaction: discord.Interaction, subcommand: str):
        await self.send_linux_info(interaction, subcommand, is_slash=True)

    async def send_linux_info(self, ctx_or_interaction, subcommand, is_slash=False):
        if not subcommand:
            embed = discord.Embed(
                title="Uh-oh!",
                description="I think you meant `.lx intro` or `.lx index`.",
                color=discord.Color.from_str("#D14775")
            )

            if is_slash:
                await ctx_or_interaction.response.send_message(embed=embed)
            else:
                await ctx_or_interaction.send(embed=embed)
            return
        
        md_files = {
            "intro": "intel/linux/lxintro.md",
            "index": "intel/linux/lxindex.md",
            "basics": "intel/linux/lxbasics.md",
            "perms": "intel/linux/lxperms.md",
            "cronj": "intel/linux/lxcronjobs.md",
            "bash": "intel/linux/lxbash.md",
            "processes": "intel/linux/lxprocesses.md",
            "filesys": "intel/linux/lxfilesystem.md"
        }

        file_path = md_files.get(subcommand.lower())
        if not file_path or not os.path.exists(file_path):
            embed = discord.Embed(
                title="404",
                description="Unknown command or file not found",
                color=discord.Color.from_str("#D14775")
            )
            if is_slash:
                await ctx_or_interaction.response.send_message(embed=embed)
            else:
                await ctx_or_interaction.send(embed=embed)
            return
        
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            title = lines[0].strip().lstrip("#").strip() if lines else f"Linux {subcommand.capitalize()}"
            description = "".join(lines[1:]).strip() if len(lines) > 1 else "No content found."

        embed = discord.Embed(
            title=title,
            description=description[:4096],
            color=discord.Color.from_str("#D14775")
        )

        if is_slash:
            await ctx_or_interaction.response.send_message(embed=embed)
        else:
            await ctx_or_interaction.send(embed=embed)

async def setup(bot):
    await bot.add_cog(LinuxCommands(bot))
    print("LinuxCommands loaded successfully.") 



