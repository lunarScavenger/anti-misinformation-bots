"""
Anti-Misinformation Discord Bot
A simple Discord bot which responds with facts when someone reports another user of spreading misinformation
"""

import imghdr # seemed to auto import >> https://docs.python.org/3/library/imghdr.html
import hikari
import lightbulb


"""
Start Up Section
"""

# instantiates a bot instance
bot = lightbulb.BotApp(token="", default_enabled_guilds=(), prefix="=") # enter bot token from Discord Developers page

# when the bot starts
@bot.listen(hikari.StartedEvent)
async def on_start(event):
    print("Bot has started") # print in the Terminal that the bot has started


"""
Prefix Commands
"""

# general burn command
@bot.command
@lightbulb.option("object", "What should be burnt", type=str)
@lightbulb.command("burn", "Burns whatever the user wants")
@lightbulb.implements(lightbulb.PrefixCommand)
async def burn(ctx):
    print("\'burn\' command has been run: " + ctx.options.object)
    if ctx.options.object == "bible" or ctx.options.object == "Bible":
        burn_response = "You just burnt the Bible. How interesting"
    else:
        burn_response = ctx.options.object + " has been burnt"
    await ctx.respond(burn_response)

# credits command
@bot.command
@lightbulb.command("credits", "Giving credit where credit is due")
@lightbulb.implements(lightbulb.PrefixCommand)
async def credits(ctx):
    await ctx.respond("This Discord bot was built on Hikari (<https://github.com/hikari-py/hikari>) and Hikari Lightbulb (<https://github.com/tandemdude/hikari-lightbulb>) in VSCodium (<https://github.com/VSCodium/vscodium>) by one person. \n \nBeing completely new to this, the developer followed the documentation linked on the GitHub pages and websites and a few videos (<https://redirect.invidious.io/watch?v=xc1VpbRd4is> (_first video in series linked_)). This contributed to why the code is so messy")

# reddit bot command
@bot.command
@lightbulb.option("bot_platform", "Which bot would you like to know of")
@lightbulb.command("bots", "What happened to the other bots")
@lightbulb.implements(lightbulb.PrefixCommand)
async def reddit(ctx):
    if ctx.options.bot_platform == "Reddit" or ctx.options.bot_platform == "reddit":
        bot_response = "The Reddit bot, `/u/notburningthebible`, is dead. Following a rough development with some working demos, it was decided to not proceed with the idea. \nIts source code can be found here: \n[link to source code]"
    elif ctx.options.bot_platform == "Twitter" or ctx.options.bot_platform == "twitter":
        bot_response = "The Twitter bot was faced with errors on Twitter's end, making it not possible for us to start development on it"
    else:
        bot_response = "There was no bot planned for the platform named"
    await ctx.respond(bot_response)


"""
Slash Commands
"""

# ping-pong command
@bot.command # declares command
@lightbulb.command("ping", "A quick ping-pong command") # command name and description
@lightbulb.implements(lightbulb.SlashCommand) # declares the command as a slash command
async def ping(ctx):
    await ctx.respond("Pong!") 

# source code command
@bot.command
@lightbulb.command("source", "Links to the bot source code")
@lightbulb.implements(lightbulb.SlashCommand)
async def source(ctx):
    await ctx.respond("[link to source code]")


"""
Misinformation Command Group
"""
# sets up the group
@bot.command # declares command
@lightbulb.command("misinfo", "Help people that are spreading misinformation") # command name and description
@lightbulb.implements(lightbulb.SlashCommandGroup) # declares the command as a slash command group
async def misinformation_group(ctx):
    pass

# earth shape
@misinformation_group.child
@lightbulb.option("shape", "What shape the user is claiming the Earth to be", type=str)
@lightbulb.option("user", "The user to be pinged")
@lightbulb.command("earth", "Respond with comments about the true shape of the Earth")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def earth_shape_response(ctx):
    await ctx.respond("Hello there, " + ctx.options.user + ". \n \n You appear to be spreading misinformation regarding the Earth's shape, claiming it to be a " + ctx.options.shape + ". \n \nAstronomy is very confusing, yes, but this should have been taught in grade school. If you would like, here's a NASA article covering all of the basics about the Earth. It really is interesting. \nhttps://www.nasa.gov/audience/forstudents/5-8/features/nasa-knows/what-is-earth-58.html")

# masks
@misinformation_group.child
@lightbulb.option("user", "The user to be pinged")
@lightbulb.command("mask", "Respond with real information about masks")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def mask_response(ctx):
    await ctx.respond("My goodness, " + ctx.options.user + "! Please just wear a mask. \nThe government may not be requiring them anymore, but they are still very helpful and will not harm you. \n \nFor everyone present, here's a link to get **free** masks: \nhttps://www.cdc.gov/coronavirus/2019-ncov/your-health/free-masks.html")

# vaccines
@misinformation_group.child
@lightbulb.option("user", "The user to be pinged")
@lightbulb.command("vaxx", "Respond with real information about vaccines")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def mask_response(ctx):
    await ctx.respond("Are you serious, " + ctx.options.user + "? Are you actually spreading misinformation regarding vaccines? They have been proven countless times to be safe. They protect not just you, but everyone around you. \nIf you are confused, read this page: \nhttps://www.cdc.gov/coronavirus/2019-ncov/vaccines/effectiveness/work.html. \n \nYou can even get some vaccines for completely **free**: https://www.vaccines.gov/")

"""
Misinformation Trolling Command Group
"""
# sets up the group
@bot.command # declares command
@lightbulb.command("m1s1nf0", "Please only do this if they are being uncooperative") # command name and description
@lightbulb.implements(lightbulb.SlashCommandGroup) # declares the command as a slash command group
async def misinformation_trolling_group(ctx):
    pass

# earth shape
@misinformation_trolling_group.child
@lightbulb.option("your_shape", "What shape you want to claim the Earth to be", type=str)
@lightbulb.option("user_shape", "What shape the user is claiming the Earth to be", type=str)
@lightbulb.option("user", "The user to be pinged")
@lightbulb.command("3ar7h", "Mess with the user spreading misinformation about the shape of the Earth with a different shape")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def earth_shape_response(ctx):
    await ctx.respond("Hello there, " + ctx.options.user + ". \nYou appear to be spreading misinformation regarding the Earth's shape, claiming it to be a " + ctx.options.user_shape + ". \n \nHonestly, how could you get that so wrong? Everyone should know by now that the Earth is a " + ctx.options.your_shape)

# masks
@misinformation_trolling_group.child
@lightbulb.option("user", "The user to be pinged")
@lightbulb.command("m4sk", "Mess with the user spreading misinformation about masks")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def mask_response(ctx):
    await ctx.respond("My goodness, " + ctx.options.user + "! Why must you be against masks? \n \nThey disturb your breathing patterns for a good reason: it prepares you for lower-oxygen environments. \nThis is all to prepare the human race to live on other planets that don't have as much oxygen")

# vaccines
@misinformation_trolling_group.child
@lightbulb.option("user", "The user to be pinged")
@lightbulb.command("v4xx", "Mess with the user spreading misinformation about vaccines")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def mask_response(ctx):
    await ctx.respond("Are you serious, " + ctx.options.user + "? Why would you be against vaccines? \n \nThey give you access to 5G! Don't you want the lightning fast internet speeds provided by 5G networks?")


"""
Runs The Bot
"""

bot.run()
