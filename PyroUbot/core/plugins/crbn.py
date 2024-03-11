from io import BytesIO
#import requests
#from PIL import Image


from PyroUbot import *
"""
async def generate_carbon_png(code: str) -> Image:
    carbon_url = f"https://carbon.now.sh/?code={code}"
    response = await requests.get(carbon_url)
    image_bytes = BytesIO(response.content)
    image = Image.open(image_bytes)
    return image
    """

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


async def carbon_func(client, message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    ex = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    carbon = await make_carbon(text)
    await ex.edit("ᴜᴘʟᴏᴀᴅɪɴɢ . . .")
    await asyncio.gather(
        ex.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"<b>ᴄᴀʀʙᴏɴɪꜱᴇᴅ by :</b>{client.me.mention}",
        ),
    )
    carbon.close()
