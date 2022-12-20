from nextcord.ext import commands
import datetime, asyncio

bot = commands.Bot(command_prefix = '/')

async def schedule_daily_message():
    #ถ้าอยากให้ทักมาทุกวันเวลานี้ให้ใส่ฟังก์ชั่น while True: แล้วเอา #บรรทัดที่9ออก
    now = datetime.datetime.now()
    #then = now+datetime.timedelta(days=1)
    then = now.replace(hour=15, minute=32)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)

    channel = bot.get_channel(แชลแนลไอดี)

    await channel.send("สวัสดีค่ะ หวานใจมาหาตามสัญญาแล้วน้าา (>//<)")

@bot.event
async def on_ready():
    print(f"Loggined in as: {bot.user.name}")
    await schedule_daily_message()
    
bot.run("โทเคน")
