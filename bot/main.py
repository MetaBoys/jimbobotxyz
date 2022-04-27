# bot.py
import os
import discord
from dotenv import load_dotenv

TOKEN = os.environ.get("TOKEN")

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.edit(nick='Jimbo')



@client.event
async def on_message(message):

  isMessageJimbo = message.content.replace(" ","")
  isMessageJimbo = isMessageJimbo.lower()
  
  index = 0
  if message.channel.name == 'jimbo':
    messageDelete = False
  
    if (len(isMessageJimbo) < 5) or (len(isMessageJimbo) %5 !=0):
      messageDelete = True


    while index + 1 < len(isMessageJimbo):
      
      if isMessageJimbo[index] != "j":
        messageDelete = True
        break
      index += 1
      
      if isMessageJimbo[index] != "i":
        messageDelete = True
        break
      index += 1
        
      if isMessageJimbo[index] != "m":
        messageDelete = True
        break
      index += 1
        
      if isMessageJimbo[index] != "b":
        messageDelete = True
        break
      index += 1
        
      if isMessageJimbo[index] != "o":
        messageDelete = True
        break
      index += 1

    if messageDelete:
      await message.delete()
      
  
  if message.channel.name == 'shill':
    angry = False

    if(message.author.bot): return
    if (len(isMessageJimbo) < 5) or (len(isMessageJimbo) %5 !=0):
      angry = True


    while index + 1 < len(isMessageJimbo):
      if angry:
        break
      
      if isMessageJimbo[index] != "j":
        angry = True

        break
      index += 1
      
      if isMessageJimbo[index] != "i":
        angry = True
      
        break
      index += 1
        
      if isMessageJimbo[index] != "m":
        angry = True
        break
      index += 1
        
      if isMessageJimbo[index] != "b":
        angry = True
        break
      index += 1
        
      if isMessageJimbo[index] != "o":
        angry = True
     
        break
      index += 1

      
    if angry:
      if(message.author.bot): return
      await message.channel.send(file= discord.File("angryJimbo.jpg"))
        

  if message.author == client.user:
        return



client.run(TOKEN)

