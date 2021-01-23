from telethon import TelegramClient, events

client= TelegramClient("client", 1508153, "e840817be5fdbf4efd169e9d0a7773ad", device_model="Xiaomi MI A1",
                      system_version="5.10.0", app_version="10 P (27)")
client.start()
@client.on(events.NewMessage(
    chats="https://t.me/telegacommunity"))
async def normal_handler(event):
    print(event)
    if str(event.message.message).startswith("/"):
       data= await client.get_entity(str(event.message.message).split(" ")[1])
       await client.send_message(event.message.peer_id,str(data))




client.run_until_disconnected()
