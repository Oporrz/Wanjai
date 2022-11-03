import discord

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):

        if str(message.author) == "PorGod#5314":  # ถ้าเป็น Username+Tag discord นี้ จงส่งข้อความว่า
            await message.channel.send("Hello " + str(message.author) + "!")
        else: 
            await message.channel.send("Hello, My name is Wanjai.")

client.run('โทเคน') 
