

import random
import asyncio
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("<", ">")
TOKEN = "NTEzNDU3NDU4MjMzMjEyOTQ5.Dv7jTA.F9dRUOJBIS0JHfU4ifbkmq1Ucf8"
guessing_game = False
listc = ['https://media.discordapp.net/attachments/513421811535577102/523950657913356298/unknown.png',
         'https://media.discordapp.net/attachments/507177498979729439/522012171060772865/47680161_970311609835022_6712277784720310272_o.png?width=710&height=667',
         'https://media.discordapp.net/attachments/507177498979729439/522012171060772864/a52ce10.jpg',
         'https://media.discordapp.net/attachments/507177498979729439/522012170381426690/32b1cef.jpg?width=524&height=666',
         'https://media.discordapp.net/attachments/507177498979729439/522012170381426689/IMG_20181204_164520_267.jpg?width=890&height=667',
         'https://media.discordapp.net/attachments/507177498979729439/522012169596829699/hsi1z0v3hwz11.jpg?width=748&height=667',
         'https://media.discordapp.net/attachments/507177498979729439/522012169596829697/aef009c.jpg?width=962&height=341',
         'https://media.discordapp.net/attachments/507177498979729439/522012169001369601/I_have_ALL_of_the_human_souls_Jon-1.gif',
         'https://media.discordapp.net/attachments/507177498979729439/522012169001369600/b4d09bb.jpg?width=778&height=666',
         'https://media.discordapp.net/attachments/507177498979729439/522011480368087041/83ba6f2.jpg?width=560&height=666',
         'https://media.discordapp.net/attachments/507177498979729439/522011479482826754/8969861.jpg',
         'https://media.discordapp.net/attachments/507177498979729439/522011479482826753/70ecb1f.png?width=566&height=666',
         'https://media.discordapp.net/attachments/507177498979729439/522011478920921090/28541c0.jpg?width=962&height=539',
         'https://media.discordapp.net/attachments/517732832119095296/522015869048455168/unknown.png',
         'https://media.discordapp.net/attachments/507177498979729439/522011478308683777/42a5abe.jpg?width=962&height=449',
         'https://media.discordapp.net/attachments/507177498979729439/522011478308683776/d9a323b.jpg?width=962&height=542',
         'https://media.discordapp.net/attachments/501371473152442398/521404972768821268/unknown.png',
         'https://media.discordapp.net/attachments/501371473152442398/521402203714355200/c1bf762.png',
         'https://media.discordapp.net/attachments/501371473152442398/521404670917476362/big_mac.png']
x = (random.choice(listc))

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='hi',
                description="greeting",
                brief="tries not to be an asshole",
                aliases=['Whats up', 'Hi', 'Hi FAM'],
                pass_context=True)
async def greetings(context):
    possible_responses = [
        'Hi, whats up',
        'Hi, hows your day',
        'Hi, wanna play big chungus',
        'Hi, its sans',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(
    name='meme',
    description="shit memes",
    brief="why do you use this command",
    aliases=['meme to my ham please', 'wanna some meme'],
    pass_context=True)
async def meme (context):


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with fellow FAMs"))
    print("Logged in as " + client.user.name)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
