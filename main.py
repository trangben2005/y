import discord 
client = discord.Client()
from keep_alive import keep_alive
keep_alive()

@client.event
async def on_ready():
    print('{0.user} đã kết nối'.format(client))
@client.event
async def on_message(tn):
    if tn.author == client.user:
        return
    if 'hi' in tn.content.lower():await tn.channel.send('hi cc')  
    if 'cc?' in tn.content.lower():
        await tn.channel.send('cc = chào cậu')
    if 'Hi' in tn.content.lower():
       await tn.channel.send('Hi cc')
client.run('MTIyMDYwMjkxMTk3MzcwMzc1Mw.GMWKDf.Kkjmxp6PzXxBHUuXS98fGXPk82hASpeK0sJQ3Y')