import discord
import yaml
from discord.ext import commands

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
    for server in bot.guilds:
        for category in server.categories:
            categories[category.name] = {
                "vocal": [],
                "text": []
            }
            print(category.channels)
            print("\n\n\n")

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
                    categories['none']['voice'].append({
                        "name": channel.name,
                        "bitrate": channel.bitrate,
                        "limit": channel.user_limit
                    })

    print(categories)
    print("\n\n\n")

bot.run('token')
