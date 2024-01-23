import asyncio
from pyrogram import Client
from pyrogram import errors as pyro_errors
import time
import secrets
import string
from Config import *
import logging
from logging.handlers import RotatingFileHandler

# Get the root logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("Assist.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGS = logging.getLogger()


app = Client(name="client", api_id=API_ID, api_hash=API_HASH, session_string=STRING)

def forward_message():
    success = 0
    fail = 0
    parts = MSG_LINK.split("/")
    channel_username = parts[3]
    message_id = int(parts[4])
    chat_ids = []# Replace with the actual chat IDs you want to forward the message to
    with open("updated.txt", "r") as f:
        content = f.read()
        new_content = content.split("/n")
        for i in new_content:
            i = i.replace("https://t.me/", "@").replace(" ", "").strip()
            chat_ids.append(i)
        print(f"Total Chat : {len(chat_ids)}")
    for i in chat_ids:
        try:
            await app.forward_messages(chat_id, channel_username, message_id)
            success += 1
        except pyro_errors.FloodWait as e:
            print(f"You have a floodwait of {int(e.value/60)} Minute & {int(e.value % 60)}.Please Wait Be Patience \nTill Now Group in sended : {success}\nTill Now Fail : {fail}")
            await asyncio.sleep(int(e.value) + 100)
        except pyro_errors.Forbidden as e:
            print(f"Forbidden Error in `{i}`: {e}")
        except pyro_errors.BadRequest as e:
            print(f"BadRequest Error in `{i}` : {e}")
        except Exception as e:
            print(f"Error in sending message in {i} due to : {e}")
            fail += 1
        if int(success + fail) % len(owo) == 0:
            stime = random.randint(1200, 1500)
            print(f"Till Now Groups in Sended :  `{success}`\nTill Now Its Fail : `{fail}`\nSleeped For : `{stime}`")
        else:
            stime = random.randint(1, 4)
        await asyncio.sleep(stime) # Add a delay of 1 second between each forward operation
            
async def start_bot():
    try:
        await app.start()
        lol = await app.get_me()
        #await app.join_chat("@sassyads")
        #await app.send_message(, f"#START\n\nVersion:- α • 1.1\n\nYour Market Place Bot Has Been Started Successfully")
        app.run(forward_message())
        await idle()
    except Exception as e:
        print(e)


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
