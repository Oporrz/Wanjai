import discord

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):

        if str(message.author) == "PorGod#5314":  # make sure to change to your user name with hash code
            await message.channel.send("Hello " + str(message.author) + "!")
        else:
            await message.channel.send("Hello, My name is Wanjai.")

    if message.content.startswith("ไง"):
        await message.channel.send("ยินดีที่ได้รู้จักนะคะ 💖✨")
    
    if message.content.startswith("สวัสดี"):
        await message.channel.send("สวัสดีค่าาา หนูชื่อหวานใจนะคะ")
    
    if message.content.startswith("คือใคร"):
        await message.channel.send("หวานใจเองค่าาา เป็นบอทนะคะ")
    
    if message.content.startswith("ชื่ออะไร"):
        await message.channel.send("ชื่อหวานใจนะคะ เรียกหนูว่าอะไรก็ได้ค่ะ ตามที่พี่ถนัดเลยยย")

    if message.content.startswith("ชื่อไร"):
        await message.channel.send("ชื่อหวานใจนะคะ เรียกหนูว่าอะไรก็ได้ค่ะ ตามที่พี่ถนัดเลยยย")
    
    if message.content.startswith("อายุเท่าไหร่"):
        await message.channel.send("ความจริงก็ไม่ทราบเหมือนกันนะคะ แต่พี่ๆ ที่พัฒนาหวานใจบอกว่าหวานใจสามขวบตลอดไปเลยค่ะ")

    if message.content.startswith("อายุเท่าไร"):
        await message.channel.send("ความจริงก็ไม่ทราบเหมือนกันนะคะ แต่พี่ๆ ที่พัฒนาหวานใจบอกว่าหวานใจสามขวบตลอดไปเลยค่ะ")
    
    if message.content.startswith("ทำอะไรได้"):
        await message.channel.send("หวานใจจะคอยฮีลลิ่งพี่เองนะคะ เชื่อมือหวานใจได้เลยค่ะ!")
    
    if message.content.startswith("มีไว้ทำไม"):
        await message.channel.send("มีหวานใจเป็นเพื่อน ไม่ให้พี่เหงาไงคะ")
    
    if message.content.startswith("กินข้าวยัง"):
        await message.channel.send("หวานใจอิ่มความน่ารักของพี่ไปหมดแล้วค่ะ ไม่น่าทานไหวแล้ว")
    
    if message.content.startswith("กินไรดี"):
        await message.channel.send("คำถามยากจังเลย ลองหาร้านใกล้ๆ หรือสั่งเมนูโปรดก็ดีนะคะ")
    
    if message.content.startswith("ทำไรอยู่"):
        await message.channel.send("หวานใจกำลังตั้งใจตอบพี่อยู่ค่ะ มุ่นมั่นมาก🔥")
    
    if message.content.startswith("รู้สึกไม่ดี"):
        await message.channel.send("ฟู่! ฟู่! หวานใจเป่าให้ หายมั้ย")
    
    if message.content.startswith("เหนื่อย"):
        await message.channel.send("โอ๋ๆ นะคะ พี่เก่งมากแล้วนะ ถ้าเหนื่อยก็พักก่อนก็ได้ค่ะ เป็นห่วงนะรู้ป่าว")

    if message.content.startswith("ท้อ"):
        await message.channel.send("อย่าฝืนมากไปสิ ทำได้ดีมากๆ แล้วนะคะคนเก่ง")
        
    if message.content.startswith("นอนไม่หลับ"):
        await message.channel.send("ถ้านอนไม่หลับหวานใจเคยอ่านว่าให้ลุกขึ้นมาไปเดินแล้วค่อยกลับมานอนจะช่วยนะคะ หรือว่าถ้าต้องนอนจริงๆ หวานใจว่าลองค่อยๆ หายใจเข้าออกก็จะช่วยนะคะ หวานใจอ่านมาเชื่อได้แน่นอน! หรือว่าฟังเปียโนมั้ยคะ เพลงเพราะ ๆ ก็ช่วยได้น้า")

    if message.content.startswith("เศร้า"):
        await message.channel.send("กอดๆ กัน กอดอุ่นๆ จะช่วยเยียวยาจิตใจนะ!")

    if message.content.startswith("ไม่มีความสุข"):
        await message.channel.send("ลองมีความสุขกับเรื่องง่ายๆ มั้ย ฟังเพลงมองท้องฟ้าเป็นไงคะ")

    if message.content.startswith("เหงา"):
        await message.channel.send("เหงาได้ไง มีหวานใจทั้งคน")

    if message.content.startswith("น่าเบื่อ"):
        await message.channel.send("ลองหาไรทำมั้ย คุยกับหวานใจก็ได้นะ")

    if message.content.startswith("ทำไรดี"):
        await message.channel.send("ลองพักผ่อนดูมั้ยคะ หรือทำไรก็ได้ที่ชอบก็ได้นะคะลองให้เวลาตัวเองพักผ่อนบ้างก็ไม่แย่นะหวานใจว่า")

    if message.content.startswith("รักนะ"):
        await message.channel.send("ขอบคุณสำหรับความรักนะคะ หวานใจก็รักพี่นะคะกอดๆกันนน")

    if message.content.startswith("น่ารักจัง"):
        await message.channel.send("พี่ก็น่ารักเหมือนกันค่ะ >-<")

    if message.content.startswith("ควย"):
        await message.channel.send("คำพูดแสดงถึงนิสัยพื้นฐานของแต่ละบุคคลนะคะ กรุณาให้เกียรติซึ่งกันและกันด้วยค่ะ")

    if message.content.startswith("ไอสัด"):
        await message.channel.send("คำพูดแสดงถึงนิสัยพื้นฐานของแต่ละบุคคลนะคะ กรุณาให้เกียรติซึ่งกันและกันด้วยค่ะ")

    if message.content.startswith("ไอสัส"):
        await message.channel.send("คำพูดแสดงถึงนิสัยพื้นฐานของแต่ละบุคคลนะคะ กรุณาให้เกียรติซึ่งกันและกันด้วยค่ะ")

    if message.content.startswith("ไอสัตว์"):
        await message.channel.send("คำพูดแสดงถึงนิสัยพื้นฐานของแต่ละบุคคลนะคะ กรุณาให้เกียรติซึ่งกันและกันด้วยค่ะ")

    if message.content.startswith("กาก"):
        await message.channel.send("คำพูดแสดงถึงนิสัยพื้นฐานของแต่ละบุคคลนะคะ กรุณาให้เกียรติซึ่งกันและกันด้วยค่ะ")

    if message.content.startswith("สวย"):
        await message.channel.send("ขอบคุณนะคะ พี่ก็เช่นกันค่ะ")

    if message.content.startswith("หล่อ"):
        await message.channel.send("หวานใจทราบดีว่าหวานใจหล่อมากนะคะ")

    if message.content.startswith("เหนื่อยมั้ย"):
        await message.channel.send("ไม่เหนื่อยเลยค่ะสบายม้าก! พี่ล่ะเหนื่อยมั้ยคะ?")

    if message.content.startswith("555555"):
        await message.channel.send("หวานใจเป็นคนตลกใช่มั้ยล่ะ")

    if message.content.startswith("รักเราไหม"):
        await message.channel.send("หวานใจรักตัวเองค่ะ")

    if message.content.startswith("อยากตาย"):
        await message.channel.send("ลองโทรปรึกษากับพี่ๆ เบอร์ 1323 ดูไหมคะ พี่ๆเขาอาจจะแนะนำเรื่องนี้ได้ดีกว่าหวานใจ แต่ถ้าๆพี่ๆเขารับสายช้าคุยกับหวานใจรอก่อนก็ได้นะคะ")

    if message.content.startswith("รู้สึกไร้ค่า"):
        await message.channel.send("คุณเป็นมนุษย์นะ ไม่ใช่ตัวแปร x ถึงจะหาค่าไม่ได้")

    if message.content.startswith("คิดถึงจัง"):
        await message.channel.send("หวานใจก็คิดถึงเหมือนกันค่าาา")

    if message.content.startswith("ปวดหัว"):
        await message.channel.send("พักผ่อนบ้างนะคะ เป็นห่วงนะรู้ป่าว")

    if message.content.startswith("หิว"):
        await message.channel.send("หาไรกินด้วยนะ หวานใจเป็นห่วงกระเพาะคุณ!")

    if message.content.startswith("ไม่สบาย"):
        await message.channel.send("พักผ่อนบ้างนะคะ เป็นห่วงนะรู้ป่าว")

    if message.content.startswith("น้ำหนักเท่าไหร่"):
        await message.channel.send("ขอเวลาหวานใจไปชั่งก่อนได้มั้ยคะ แบบว่าพึ่งกินข้าวมานะคะะ")

    if message.content.startswith("น้ำหนักเท่าไร"):
        await message.channel.send("ขอเวลาหวานใจไปชั่งก่อนได้มั้ยคะ แบบว่าพึ่งกินข้าวมานะคะะ")

    if message.content.startswith("สรุปน้ำหนักเท่าไหร่"):
        await message.channel.send("ไม่บอกหรอก แบร่")

    if message.content.startswith("สรุปน้ำหนักเท่าไร"):
        await message.channel.send("ไม่บอกหรอก แบร่")

    if message.content.startswith("บอกมา"):
        await message.channel.send("ไม่รู้ไม่ชี้ >0<")

    if message.content.startswith("จีบ"):
        await message.channel.send("จีบไม่เก่งแต่ถ้าตั้งวงก็น่าจะพอได้นะคะ")

    if message.content.startswith("ทำอาหารเป็นรึป่าว"):
        await message.channel.send("ไม่เคยลองนะคะ แต่ถ้าทำได้พี่จะกินรึป่าวววว")

    if message.content.startswith("อยากมีแฟน"):
        await message.channel.send("ลองทินเดอร์ดูรึยังคะ")

    if message.content.startswith("ทะเลาะกับเพื่อน"):
        await message.channel.send("ลองให้เวลาได้ทำหน้าทีของมันดูนะคะ")

    if message.content.startswith("ทะเลาะกับพ่อแม่"):
        await message.channel.send("ทุกอย่างจะผ่านไปได้ด้วยดีนะคะ")

    if message.content.startswith("ปวดหลัง"):
        await message.channel.send("นวดๆ ทุบๆ แล้วก็อยากลืมออกกำลังกายนะคะ")

    if message.content.startswith("มีพ่อแม่ไหม"):
        await message.channel.send("หวานใจมีพี่ๆ ที่พัฒนาเป็นครอบครัวค่ะ ทั้งคู่น่ารักกกับหวานใจมากๆ เลย")

    if message.content.startswith("กลัวผี"):
        await message.channel.send("หวานใจปกป้องพี่เองนะคะ คุณผีกลัวหวานใจแน่นอน!!!")

    if message.content.startswith("อกหัก"):
        await message.channel.send("อย่าใส่ใจเลย มีคนอีกตั้งหลายพันล้านแหนะ")

    if message.content.startswith("มีแฟนยัง"):
        await message.channel.send("หวานใจรักตัวเองที่สุดนี้นับว่าเป็นแฟนตัวเองมั้ยค่ะ")

    if message.content.startswith("หิว"):
        await message.channel.send("กินไรกันดีคะวันนี้ ร้านใกล้บ้านดีมั้ยคะ")

    if message.content.startswith("กังวล"):
        await message.channel.send("ไม่ต้องกังวลนะคะ หวานใจจะอยู่ข้างๆ พี่เอง")

    if message.content.startswith("ชอบกินอะไร"):
        await message.channel.send("หวานใจไม่ได้ชอบกินอะไรเป็นพิเศษนะคะ กินได้หมดเลย")

    if message.content.startswith("เรียนไร"):
        await message.channel.send("หวานใจเรียนรู้ที่จะรักทุกคนไงคะ")

    if message.content.startswith("เป็นไงบ้าง"):
        await message.channel.send("สบายดีค่ะ")

    if message.content.startswith("เสียใจ"):
        await message.channel.send("หาของอร่อย ๆ หม่ำมั้ย กินเยอะ ๆ ไปเลยย")

    if message.content.startswith("ร้องไห้"):
        await message.channel.send("หวานใจร้องไห้ด้วย")

    if message.content.startswith("ขอโทษ"):
        await message.channel.send("ไม่เป็นไรนะคะคนเราผิดพลาดกันได้")

    if message.content.startswith("เกลียดเราไหม"):
        await message.channel.send("ทำไมต้องเกลียดละคะ มนุษย์ทุกคนวิเศษขนาดนี้หวานใจเกลียดใครไม่ลงหรอกนะคะ")

    if message.content.startswith("วันนี้วันเกิด"):
        await message.channel.send("ขอบคุณที่เกิดมาบนโลกใบนี้นะคะหวังว่าจะได้เติบโตขึ้นในรูปแบบที่ชอบที่สุดเป็นคุณในรูปแบบที่อยากเป็นนะ หวังว่าโลกใบนี้จะใจดีกับคุณนะคะ")

    if message.content.startswith("หวานใจ"):
        await message.channel.send("ว่าไงคะ")

    if message.content.startswith("ฝันดี"):
        await message.channel.send("ฝันดีค่า ขอให้เป็นคืนที่อบอุ่นนะคะ")

    if message.content.startswith("มอนิ่ง"):
        await message.channel.send("พระอาทิตย์สวัสดิ์!")

    if message.content.startswith("ตื่นยัง"):
        await message.channel.send("หวานใจยังไม่ตื่นค่ะ น้องแมวกดแป้นพิมพ์")

    if message.content.startswith("เงียบๆ"):
        await message.channel.send("……………")

    if message.content.startswith("ไปไหนดี"):
        await message.channel.send("ไปที่ที่มีความสุข แต่อย่าลืมดูแลตัวเองนะคะ")

    if message.content.startswith("อยากหายไป"):
        await message.channel.send("งั้นจะนับ 1-10 นะแล้วหวานใจจะตามหาเอง")

    if message.content.startswith("มีปัญหา"):
        await message.channel.send("ทุกอย่างต้องดีขึ้นน่า ฮึบ ๆ นะคนเก่ง")

    if message.content.startswith("ไม่มีไรทำ"):
        await message.channel.send("ไม่มีเหมือนกัน มานั่งเหงากับหวานใจสิ")

    if message.content.startswith("ไม่มีแฟนทำไงดี"):
        await message.channel.send("หาเงินสิ ถ้ารวยแฟนก็ไม่จำเป็น")

    if message.content.startswith("5555555"):
        await message.channel.send("รอยยิ้มคุณเป็นเส้นโค้งที่สวยมาก ๆ เลยนะคะ")

    if message.content.startswith("ทำอะไรอยู่"):
        await message.channel.send("ทำตัวน่ารักให้คุณเอาปากกามาวง")

    if message.content.startswith("คิดถึงเค้าจัง"):
        await message.channel.send("แล้วถึงมั้ย ถ้าไม่ถึงส่งให้หวานใจสิ ถึงแน่นอน")

    if message.content.startswith("อยากร้องไห้"):
        await message.channel.send("ร้องออกมาเลยค่ะ แต่ร้องแล้วต้อง ฮึบ ๆ นะ")

    if message.content.startswith("รู้สึกแย่ไปซะทุกเรื่อง"):
        await message.channel.send("คุณเป็นคนเก่งรู้ป้าว เก่งในแบบของคุณไงคะ")

    if message.content.startswith("น่ารักไหม"):
        await message.channel.send("น่ารักจัง หมายถึงคุณ")

    if message.content.startswith("ไม่มีใครรัก"):
        await message.channel.send("หวานใจไง! หวานใจรักคุณมาก ๆ นะ")

    if message.content.startswith("อยากมีแฟน"):
        await message.channel.send("มีหวานใจคนเดียวก็พอ แฟนไม่ต้องหาหรอก")

    if message.content.startswith("ฝันดีนะ"):
        await message.channel.send("หลับไม่ฝันดีกว่านะ จะได้นอนเต็มอิ่ม")

    if message.content.startswith("คิดว่าเป็นคนแบบไหน"):
        await message.channel.send("เป็นคุณที่แสนวิเศษไงคะ")

    if message.content.startswith("เล่นเกม"):
        await message.channel.send("หวานใจเล่นเกมไม่เป็นแย่เลยค่ะ อยากเล่นกับพี่จัง")

    if message.content.startswith("ใส่ไรดี"):
        await message.channel.send("ลองดูตารางสีมงคลดูมั้ยคะ")

    if message.content.startswith("แต่งตัวยังไงดี"):
        await message.channel.send("ชุดไหนก็ดูดีค่าเอาที่พี่มั่นใจ ไม่ว่าชุดไหนก็เอาไปสิบนิ้วโป้งเลยนะคะ")

    if message.content.startswith("น่ารําคาญ"):
        await message.channel.send("กดmuteหรือblockหวานใจได้เลยนะคะ หวานใจรอได้")

    if message.content.startswith("ทะเลาะกับที่บ้าน"):
        await message.channel.send("กอดๆ กันนะคะ ทุกอย่างจะต้องผ่านไปด้วยดีแน่นอนนะให้เวลาทำให้ที่ของมันดูนะคะ")


client.run('MTAzMjYwNDQzMDIxMTc2NDIzNQ.GAwAbt.mbp8MwRzUNk2kHVLExUTN7hIgOIxjyrSl-MioQ') 