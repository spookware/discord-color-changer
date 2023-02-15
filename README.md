# Discord Color Changer

My first public repo, this is a shittily coded discord color changer that, in essence, just swaps color roles. I don't recommend using it on more than one person, and you need to set it up on your own because im lazy and dont feel like doing anything like that.

# Setup Guide

Replace ```YOUR ROLE ID``` with a color role from your server. If you want it to have more, or less colors that it cycles, just delete the lines the role id values in them, as well as the lines that add the specified role. For example:

I only want it to cycle 3 roles:

```
@client.slash_command(description="rainbow colour change")
async def colourchange(inter):
    while True:

        role1 = inter.guild.get_role(YOUR ROLE ID)
        role2 = inter.guild.get_role(YOUR ROLE ID)
        role3 = inter.guild.get_role(YOUR ROLE ID)

        await inter.author.remove_roles(role3)
        time.sleep(3)
        await inter.author.add_roles(role2)
        await inter.author.remove_roles(role1)

        time.sleep(3)
        await inter.author.add_roles(role3)
        await inter.author.remove_roles(role2)
        time.sleep(3)
        await inter.author.add_roles(role1)

```

I believe you'll need the disnake lib for this, or convert it to use discord.py.
Chances are I won't update for a while if ever.
