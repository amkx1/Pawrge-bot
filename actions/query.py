import discord
from discord.ext import commands
from intel.data.cybersec_data import cybersecurity_terms

class QueryCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="what")
    async def what(self, ctx, *, query: str):
        term = query.lower().strip()
        if term in cybersecurity_terms:
            embed = discord.Embed(
                title = term.title(),
                description = cybersecurity_terms[term],
                color=discord.Color.from_str("#D14775")
            )  
        else:
            embed = discord.Embed(
                title = "Term not found.",
                description = "Try `.listterms` to see other terms.",
                color=discord.Color.from_str("#D14775")
            ) 
        await ctx.send(embed=embed)

    @commands.command(name="listterms")
    async def listterms(self, ctx):
        terms = ', '.join(sorted(cybersecurity_terms.keys()))
        await ctx.send(f"List of Terms: {terms}")

async def setup(bot):
    await bot.add_cog(QueryCommands(bot))