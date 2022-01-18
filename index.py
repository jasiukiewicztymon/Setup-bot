import discum
import os
import colorama
from colorama import Fore

typeselector = 1

while (typeselector == 1 or typeselector == 2):
#-------------------------------------------------------------------
# Printing the menu...
# Here the user do the selection about the params they want 
#-------------------------------------------------------------------
    title = '''
___________________________________________________________________________________________________________
    ________   _________    ___________________   _____      _____      _____   _____________________ 
    \______ \  \_   ___ \  /   _____/\______   \ /  _  \    /     \    /     \  \_   _____/\______   \\
    |    |  \ /    \  \/  \_____  \  |     ___//  /_\  \  /  \ /  \  /  \ /  \  |    __)_  |       _/
    |    `   \\\\     \____ /        \ |    |   /    |    \/    Y    \/    Y    \ |        \ |    |   \\
    /_______  / \______  //_______  / |____|   \____|__  /\____|__  /\____|__  //_______  / |____|_  /
            \/         \/         \/                   \/         \/         \/         \/         \/ 
___________________________________________________________________________________________________________
    '''
    print(Fore.MAGENTA + title + '\n')
    msg = input(Fore.RESET + 'Input the message content: ')
    print()
    idspath = input('Give the discords ids PATH: ')
    print()
    accescode = input('Give the acces code: ')
    print()
    serverid = input('Give the server id: ')
    print()
    channelid = input('Give the channel id: ')
    print()
    typeselector = input(Fore.MAGENTA + '\n[2] - One time spam\n[1] - Multi spam\n[0] - Exit\n\n')
    
    print(Fore.RESET)
    os.system('cls')

    if (typeselector == '0'):
        break

#-------------------------------------------------------------------

    bot = discum.Client(accescode)

    def close_after_fetching(resp, guild_id):
        if bot.gateway.finishedMemberFetching(guild_id):
            lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
            print(str(lenmembersfetched) + ' members fetched')
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()

    def get_members(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guild_id).members

    members = get_members(serverid, channelid)
    memberslist = []

    os.system('cls')

for memberID in members:
    memberslist.append(memberID)

f = open('ids.txt', "a")
for element in memberslist:
    f.write(element + '\n')
f.close()

discord_token = "Njg1MDgzMDk5NDU2OTk1MzUw.YebkKw.v0R6lUbGuvzRrueRPtyxVcY6unI"
#botter = commands.Bot(command_prefix = '$')

r = open('ids.txt', 'r')
rlines = r.readlines()

#@botter.event
#async def on_ready(): 
   # print('The bot connected')
    #for line in rlines:
       # for i in range(75):
        #    channel = line.create_dm()
        #    botter.send_message(channel,msg)

#botter.run(discord_token)