#DeathLands bot by DSGNTN

#imports
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import time
import random

#bot prefix definition
bot = commands.Bot(command_prefix='DL', description='Deathlands bot.')

#bot start
@bot.event
async def on_ready():
    print ("I'm ready and up and running")
    print ("My name is: " + bot.user.name)
    print ("My ID is: " + bot.user.id)

#hello test command
@bot.command(pass_context=True)
async def hello(ctx):
    await bot.delete_message(ctx.message)
    await bot.say(":smile: Well hello there I'm " + bot.user.name + " here to help you! Check out DLhelp to know what I can do!")
    print ("user invoked command hello")

#opme MTTS test command
@bot.command(pass_context=True)
async def opme(ctx):
    randomnum = random.randint(0, 2)
    
    if randomnum == 1:
        message = ":japanese_ogre: You tried so hard but didn't succeed, this bot is not meant for rookies like you " + ctx.message.author.name + "!"
    else:
        if randomnum == 2:
            message = "Mission failed better luck next time " + ctx.message.author.name + "."
        else:
            message = "You got opped but even faster deopped."    

    await bot.delete_message(ctx.message)
    await bot.say(message)
    print ("user invoked command opme")

#apply command
@bot.command(pass_context=True)
async def apply(ctx):
    await bot.delete_message(ctx.message)
    print ("user invoked command apply")
    await bot.send_message(ctx.message.author, ":smile: Hello there a little birdie told me you want to apply for " + ctx.message.server.name + ". Well then all you need to do is hit the following link and fill in the form! \nWe will then read your apply as soon as possible and let you know if you got accepted! \n**LINK** : https://igdt.typeform.com/to/lsdkRS")

#serverip command
@bot.command(pass_context=True)
async def serverip(ctx):
    await bot.delete_message(ctx.message)
    print ("user invoked command serverip")
    await bot.send_message(ctx.message.author, "Join our server and become the next #1 on our Skyblock or Factions server, or maybe on one of our parkours? :wink: \n**SERVERIP** : 198.50.128.62")

#store command
@bot.command(pass_context=True)
async def store(ctx):
    await bot.delete_message(ctx.message)
    print ("user invoked command store")
    await bot.send_message(ctx.message.author, "You ready to get to the next level and by buying a rank or something else? \nVisit the following link to make your purchases! \n**LINK** : https://deathlandsigdt.buycraft.net/")

#website command
@bot.command(pass_context=True)
async def website(ctx):
    await bot.delete_message(ctx.message)
    print ("user invoked command store")
    await bot.send_message(ctx.message.author, "What planet are you from? \nGo and pay a visit to our posts on PlanetMinecraft! \n**LINK**: <https://www.planetminecraft.com/server/deathlands-4172003/>")

#serverinfo command
@bot.command(pass_context=True)
async def serverinfo(ctx):
    await bot.delete_message(ctx.message)

    online = 0
    for i in ctx.message.server.members:
        if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
            online += 1

    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x8B0000)
    embed.set_author(name="Server info")
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.add_field(name="Online members", value=online, inline=True)
    embed.add_field(name="Server name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Region", value=ctx.message.server.region, inline=True)
    embed.add_field(name="Counted roles", value=len(ctx.message.server.roles), inline   =True)
    embed.add_field(name="Total members", value=len(ctx.message.server.members))
    embed.add_field(name="Discord Server link", value="<https://discord.gg/7zeHSkj>", inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.send_message(ctx.message.author, embed=embed)

#kick command
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.delete_message(ctx.message)
    if ctx.message.author.id == "240903777194868737" or ctx.message.author.id == "371718064603136010":
        membername = user.name
        await bot.say(":boot: Cya, {}. You should've behaved yourself!".format(membername))
        await bot.kick(user)
    else:
        invokename = ctx.message.author.mention
        await bot.say("You do not have permissions to do this {}".format(invokename))

#botinfo command
@bot.command(pass_context=True)
async def botinfo(ctx):
    await bot.delete_message(ctx.message)
    embed = discord.Embed(title="Deathlands Bot", description="The official Deathlands Bot.", color=0x8B0000)
    embed.set_author(name="DSGNTN")
    embed.add_field(name="Server count", value=f"{len(bot.servers)}")
    await bot.say(embed=embed)

#help command
bot.remove_command('help')
@bot.command(pass_context=True)
async def help(ctx):
    await bot.delete_message(ctx.message)
    embed = discord.Embed(title="Deathlands Bot", description="The official Deathlands Bot has following commands:", color=0x8B0000)
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.add_field(name="DLserverinfo", value="This command will show you all the information you need about the discord server.", inline=False)
    embed.add_field(name="DLbotinfo", value="I am Bot, but why me and by who, find out by doing this command!", inline=True)
    embed.add_field(name="DLhelp", value="Well you are looking at this list right now so no further explanation is needed.",inline=True)
    embed.add_field(name="DLpermsinfo", value="Well you can buy a rank to get better gear but that's not all you'll be getting!", inline=True)
    embed.add_field(name="DLapply", value="Do you want to help our staff team out? Then you can find all you need via this command to join " + ctx.message.server.name, inline=True)
    embed.add_field(name="DLserverip", value="Enjoying the things you've seen here in our discord and are you eager to join the server, then here's where you need to be.", inline=True)
    embed.add_field(name="DLstore", value="Well... I don't know what you think but I think buying keys or a rank helps out the server a lot!", inline=True)
    embed.add_field(name="DLwebsite", value="It's not our own website yet but it's a very clear post on PlanetMinecraft about our server.", inline=True)
    embed.add_field(name="DLhelpme @user", value="If you're in need of some help you can do this command and tag a person behind it to notify the person you need his/her help.", inline=True)
    embed.add_field(name="DLsuggestion [suggestion message]", value="Got a suggestion then just drop it by using this command and it will be added to our suggestion list!", inline=True)
    embed.add_field(name="DLbugsproblems [bug or problem message]", value="Found any bugs or got a problem, then just let us know via this command!", inline=True)
    embed.add_field(name="DLreport @user [prooflink] [reasoning]", value="Found someone who doesn't like to follow rules and you've got proof of it? Then slide it in to our channels via this command.", inline=True)
    await bot.say(embed=embed)

#id test command
@bot.command(pass_context=True)
async def id(ctx, number: int):
    msg = number
    await bot.send_message(ctx.message.author, msg)
    await bot.say(number)

#permsinfo command
@bot.command(pass_context=True)
async def permsinfo(ctx):
    description = "Deathlands permissions per rank.\nThis list contains following ranks with their perms:"
    
    info = "\n\nRanks can be purchased at the store, link can be found via DLstore."
    await bot.delete_message(ctx.message)
    await bot.send_message(ctx.message.author, description + "\n\n__**COAL**__\n**[1]** /kit coal \n**[2]** /realname \n**[3]** /ptime \n**[4]** /feed or /eat \n**[5]** /ec \n**[6]** /sethome (5x) \n**[7]** /disguise cow \n**[8]** Joining the full server\n\n__**IRON**__\n**[1]** /kit iron \n**[2]** /fly \n**[3]** island fly (only Skyblock) \n**[4]** /sethome (8x) \n**[5]** /hat \n**[6]** /wb \n**[7]** /disguise pig \n**[8]** all commands of **COAL** rank\n\n__**GOLD**__\n**[1]** /kit gold \n**[2]** /clearinventory or /clear \n**[3]** /sethome (10x) \n**[4]** /disguise sheep \n**[5]** able to do chatcolor (villager at skyblock) \n**[6]** afk bypass \n**[7]** all commands of **IRON** rank\n\n__**DIAMOND**__\n**[1]** /kit diamond \n**[2]** /heal \n**[3]** /back \n**[4]** /sethome (15x) \n**[5]** /disguise rabbit \n**[6]** /chest \n**[7]** keep exp on death \n**[8]** all commands of **GOLD** rank\n\n__**EMERALD**__\n**[1]** /kit emerald \n**[2]** /nick \n**[3]** /disguise wolf \n**[4]** /sethome (20x) \n**[5]** all commands of **DIAMOND** rank\n\n__**SAPPHIRE**__\n**[1]** /kit sapphire \n**[2]** /fix or /repair \n**[3]** /sethome (20x) \n**[4]** chest 2 \n**[5]** /disguise villager \n**[6]** all commands of **EMERALD** rank" + info)

#helpme command
@bot.command(pass_context=True)
async def helpme(ctx, user: discord.Member):
    await bot.delete_message(ctx.message)
    author = ctx.message.author.mention
    tagged = user.mention
    await bot.say(tagged + " it looks like " + author + " needs help with something.")

#deny command
@bot.command(pass_context=True)
async def deny(ctx, user: discord.Member, *, tekst: str):
    await bot.delete_message(ctx.message)
    if ctx.message.author.id == "240903777194868737" or ctx.message.author.id == "371718064603136010":
        membername = user.mention
        applychannel = bot.get_channel("487243608429297675")
        deny = "Sorry to say {} but you have been denied.".format(membername) + "\nReasoning : " + tekst
        await bot.send_message(destination=applychannel, content=deny)
    else:
        invokename = ctx.message.author.mention
        await bot.say("You do not have permissions to do this {}".format(invokename))

#accept command
@bot.command(pass_context=True)
async def accept(ctx, user: discord.Member):
    await bot.delete_message(ctx.message)
    if ctx.message.author.id == "240903777194868737" or ctx.message.author.id == "371718064603136010":
        membername = user.mention
        applychannel = bot.get_channel("487243608429297675")
        accept = "Hey there {} you have been accepted! Please send a private message to @IGDT#2841 for more information.".format(membername)
        await bot.send_message(destination=applychannel, content=accept)
    else:
        invokename = ctx.message.author.mention
        await bot.say("You do not have permissions to do this {}".format(invokename))

#update command
@bot.command(pass_context=True)
async def update(ctx, *, tekst: str):
    await bot.delete_message(ctx.message)
    if ctx.message.author.id == "240903777194868737":
        updatechannel = bot.get_channel("486892903986102293")
        update = "**[Discord Bot UPDATE]** " + tekst + "."
        await bot.send_message(destination=updatechannel, content=update)
    else:
        invokename = ctx.message.author.name
        await bot.say("You do not have permissions to do this {}".format(invokename))

#changelog command
@bot.command(pass_context=True)
async def changelog(ctx, titel, *, tekst:str):
    await bot.delete_message(ctx.message)
    if ctx.message.author.id == "240903777194868737" or ctx.message.author.id == "371718064603136010":
        changelogchannel = bot.get_channel("476110089992798229")
        await bot.send_message(destination=changelogchannel, content ="**[{}]** ".format(titel.upper()) + tekst + ".") 
    else:
        invokename = ctx.message.author.name
        await bot.say("You do not have permissions to do this {}".format(invokename))

#suggestion command
@bot.command(pass_context=True)
async def suggestion(ctx, *, tekst: str):
    await bot.delete_message(ctx.message)
    suggestionchannel = bot.get_channel("467675399858421770")
    reaction = ctx.message.author.name + " your suggestion has been received and will be processed.\nSubject: " + tekst + "."
    suggestion = "**[SUGGESTION]** " + ctx.message.author.name + " has following suggestion: " + tekst + "."
    await bot.send_message(destination=suggestionchannel, content=reaction)
    taskchannel = bot.get_channel("478891216902160385")
    await bot.send_message(destination=taskchannel, content=suggestion)

#bugsproblems command
@bot.command(pass_context=True)
async def bugsproblems(ctx, *, tekst: str):
    await bot.delete_message(ctx.message)
    bugsproblemschannel = bot.get_channel("467675426517680130")
    reaction = ctx.message.author.name + " your bugs-problems report has been received and will be processed."
    report = "**[BUGS-PROBLEMS]** " + ctx.message.author.name + " has reported following bugs-problems: " + tekst + "."
    await bot.send_message(destination=bugsproblemschannel, content=reaction)
    taskchannel = bot.get_channel("478891216902160385")
    await bot.send_message(destination=taskchannel, content=report)

#report command
@bot.command(pass_context=True)
async def report(ctx, user: discord.Member, proof: str, *, tekst: str):
    await bot.delete_message(ctx.message)
    reportchannel = bot.get_channel("487347855028125708")
    playerreportchannel = bot.get_channel("487349549971800064")
    reaction = ctx.message.author.name + "  your report has been received, thank you for maintaining our rules!"
    report = "**[REPORT]** " + ctx.message.author.name + " is reporting " + user.name + " with following reasoning: \n" + tekst + "\nWith following proof: " + proof
    await bot.send_message(destination=reportchannel, content=report)
    await bot.send_message(destination=playerreportchannel, content=reaction)
    



#welcoming message
#@bot.command(pass_context=True)
#async def on_member_join(user: discord.Member):
    
#    welcomingchannel = bot.get_channel("476024612895850498")
#    await bot.send_message(destination=welcomingchannel, content="Welcome " + user.mention)

bot.run("NDc2MDA2MDI1MzI2MTAwNDgw.DknsHQ.TYy1I5Hg9Nveb-xCiBTbQGdy00A")
