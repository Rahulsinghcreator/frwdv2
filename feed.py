from pyrogram import Client
from pyrogram import errors as pyro_errors
import time
import secrets
import string
from Config import *
import logging

# Get the root logger
root_logger = logging.getLogger()

# Increase the size of the log buffer
logging.basicConfig(
    format="[%(asctime)s] [%(levelname)s] [%(name)s] : %(message)s",
    level=logging.ERROR,
    datefmt="%H:%M:%S",
)


random_string = "".join(
  secrets.choice(string.ascii_letters + string.digits)
  for _ in range(10)
)


app = Client(name=f"{random_string}", api_id=API_ID, api_hash=API_HASH, session_string=STRING)

async def forward_message():
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
    while True:
        for i in chat_ids:
            try:
                await app.forward_messages(chat_id, channel_username, message_id)
                success += 1
            except pyro_errors.FloodWait as e:
                print(f"You have a floodwait of {int(e.value/60)} Minute & {int(e.value % 60)}.Please Wait Be Patience \nTill Now Group in sended : {success}\nTill Now Fail : {fail}")
                await asyncio.sleep(int(e.value) + 100)
            except pyro_errors.Forbidden as e:
                print(f"Forbidden Error in `{i}`: {e}")
                continue
            except pyro_errors.BadRequest as e:
                print(f"BadRequest Error in `{i}` : {e}")
                continue
            except Exception as e:
                print(f"Error in sending message in {i} due to : {e}")
                fail += 1
                continue
            if int(success + fail) % len(owo) == 0:
                stime = random.randint(1200, 1500)
                print(f"Till Now Groups in Sended :  `{success}`\nTill Now Its Fail : `{fail}`\nSleeped For : `{stime}`")
            else:
                stime = random.randint(2, 4)
            time.sleep(stime)  # Add a delay of 1 second between each forward operation
print("Bot started")
app.run(forward_message())
