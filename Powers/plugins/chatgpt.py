import os, time
import openai
from pyrogram import filters
from Powers import Powers
from pyrogram.enums import ChatAction, ParseMode
from gtts import gTTS



openai.api_key = "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"




@Powers.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(Powers :Powers, message):
    
    try:
        start_time = time.time()
        await Powers.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**ʜᴇʟʟᴏ sɪʀ**\n**ᴇxᴀᴍᴘʟᴇ:-**`.ask How to set girlfriend ?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            await message.reply_text(f"{x}")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e} ")        






@Powers.on_message(filters.command(["assis"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(Powers :Powers, message):
    
    try:
        start_time = time.time()
        await Powers.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**ʜᴇʟʟᴏ sɪʀ**\n**ᴇxᴀᴍᴘʟᴇ:-**`.assis How to set girlfriend ?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            text = x    
            tts = gTTS(text, lang='en')
            tts.save('output.mp3')
            await Powers.send_voice(chat_id=message.chat.id, voice='output.mp3')
            os.remove('output.mp3')            
            
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e} ")        




