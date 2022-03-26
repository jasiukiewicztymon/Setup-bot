import discord
import json
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='s-')

@bot.command()
async def channelslist(ctx):
    # listing and writing channels to yaml file with confings
    categories = {
        "none": {
            "vocal": [],
            "text": []
        }
    }

    # adding all channels with categories
    for server in bot.guilds:
        for category in server.categories:
            categories[category.name] = {
                "vocal": [],
                "text": []
            }
            for channel in category.channels:
                if str(channel.type) == 'text':
                    proprieties = {"name": channel.name}

                    try:
                        nsfw = channel.nsfw
                        proprieties["nsfw"] = str(nsfw).lower()
                    except:
                        proprieties["nsfw"] = 'none' 

                    try:
                        news = channel.news
                        proprieties["news"] = str(news).lower()
                    except:
                        proprieties["news"] = 'none' 

                    categories[category.name]['text'].append(proprieties)

                if str(channel.type) == 'voice':
                    proprieties = {"name": channel.name}

                    try:
                        bitrate = channel.bitrate
                        proprieties["bitrate"] = str(bitrate).lower()
                    except:
                        proprieties["bitrate"] = 'none' 

                    try:
                        limit = channel.user_limit
                        proprieties["limit"] = str(limit).lower()
                    except:
                        proprieties["limit"] = 'none' 

                    categories[category.name]['vocal'].append(proprieties)

    # adding all channels without categories
    for server in bot.guilds:
        for channel in server.channels:
            try:
                int(channel.category_id)
            except:
                if str(channel.type) == 'text':
                    proprieties = {"name": channel.name}

                    try:
                        nsfw = channel.nsfw
                        proprieties["nsfw"] = str(nsfw).lower()
                    except:
                        proprieties["nsfw"] = 'none' 

                    try:
                        news = channel.news
                        proprieties["news"] = str(news).lower()
                    except:
                        proprieties["news"] = 'none' 

                    categories['none']['text'].append(proprieties)

                if str(channel.type) == 'voice':
                    proprieties = {"name": channel.name}

                    try:
                        bitrate = channel.bitrate
                        proprieties["bitrate"] = str(bitrate).lower()
                    except:
                        proprieties["bitrate"] = 'none' 

                    try:
                        limit = channel.user_limit
                        proprieties["limit"] = str(limit).lower()
                    except:
                        proprieties["limit"] = 'none' 

                    categories['none']['vocal'].append(proprieties)

    with open('{}.json'.format(ctx.message.guild.name), 'w', encoding='utf8') as outfile:
        outdata = json.dumps(categories, ensure_ascii=False)
        outfile.write(outdata)
    await ctx.send(file=discord.File(r'./{}.json'.format(ctx.message.guild.name)))

@bot.command()
async def create(ctx, *args):
    guild = ctx.message.guild
    arg = []
    temp = ""

    for arr in args:
        if arr != '|':
            temp += arr + " "
        else:
            temp = temp[0:len(temp) - 1]
            arg.append(temp)
            temp = ""
    
    temp = temp[0:len(temp) - 1]
    arg.append(temp)

    if len(arg) == 2:
        # creation of channel without category
        if arg[0] == 'text':
            await guild.create_text_channel(arg[1])
        elif arg[0] == 'vocal':
            await guild.create_voice_channel(arg[1])
        else:
            await ctx.reply('Invalid channel type')

    if len(arg) == 3:
        # creation of channel with category

        # getting category
        id = 0
        for server in bot.guilds:
            for category in server.categories:
                if category.name == arg[2]:
                    if arg[0] == 'text':
                        await guild.create_text_channel(arg[1], category=category)
                    elif arg[0] == 'vocal':
                        await guild.create_voice_channel(arg[1], category=category)
                    else:
                        await ctx.reply('Invalid channel type')

                try:
                    id = int(arg[2])
                except:
                    continue

                if category.id == id:
                    if arg[0] == 'text':
                        await guild.create_text_channel(arg[1], category=category)
                    elif arg[0] == 'vocal':
                        await guild.create_voice_channel(arg[1], category=category)
                    else:
                        await ctx.reply('Invalid channel type')

bot.run('token')
