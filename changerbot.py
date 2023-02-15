import disnake

intents.members = True
intents.message_content = True
intents.presences = True
intents.bans = True
client = commands.Bot(command_prefix='!', intents=intents)
@client.event
async def on_ready():
  print(f'Logged in as: {client.user}')
  
@client.slash_command(description="rainbow colour change")
@commands.has_permissions(administrator=True)
async def colourchange(inter):
    while True:

        role1 = inter.guild.get_role(1057866061699108975)
        role2 = inter.guild.get_role(1057877928693739570)
        role3 = inter.guild.get_role(1057869872735989860)
        role4 = inter.guild.get_role(1057869849247875143)
        role5 = inter.guild.get_role(1057869677633740941)
        role6 = inter.guild.get_role(1057869888514953226)
        role7 = inter.guild.get_role(1057869895959838730)

        await inter.author.add_roles(role1)
        time.sleep(3)
        await inter.author.add_roles(role2)
        await inter.author.remove_roles(role1)

        time.sleep(3)
        await inter.author.add_roles(role3)
        await inter.author.remove_roles(role2)
        
        time.sleep(3)
        await inter.author.add_roles(role4)
        await inter.author.remove_roles(role3)
        time.sleep(3)


        await inter.author.add_roles(role4)
        time.sleep(3)
        await inter.author.add_roles(role5)
        await inter.author.remove_roles(role4)

        time.sleep(3)
        await inter.author.add_roles(role6)
        await inter.author.remove_roles(role5)
        
        time.sleep(3)
        await inter.author.add_roles(role7)
        await inter.author.remove_roles(role6)

        time.sleep(3)
        await inter.author.add_roles(role1)
        await inter.author.remove_roles(role7)

client.run('Your BOT Token')
