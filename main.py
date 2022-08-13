import os

import discord
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	text = message.content
	data = requests.get(f'http://ispothate.eastus.cloudapp.azure.com:8000/ishomophobia?text={text}').json()
	if (data['ishomophobia'] == True):
		await message.delete()
		embed = discord.Embed(title="Message removed", url="https://adm.viu.ca/positive-space/how-homophobia-hurts-us-all", description="Educate yourself about homophobia and postive LGBTQ speech!")
		await message.channel.send(embed=embed)
		return
	data = requests.get(f'http://ispothate.eastus.cloudapp.azure.com:8000/ishate?text={text}').json()
	if (data['HATE'] > 0.4):
		await message.delete()
		embed = discord.Embed(title="Message removed", url="https://impakter.com/hurt-feelings-real-danger-hate-speech/", description="Educate yourself about anti-hate speech and supporting others!")
		await message.channel.send(embed=embed)
		return
	data = requests.get(f'http://ispothate.eastus.cloudapp.azure.com:8000/isswearing?text={text}').json()
	if (data['isswearing'] == True):
		await message.delete()
		await message.channel.send(data['text'])
		await message.channel.send('Message censored. Please use more respectful speech, thanks!')
		return

client.run(TOKEN)
