"""
Telegram userbot (Render.com uchun doimiy ishlaydigan versiya)
Muallif: ChatGPT (GPT-5)
"""

from telethon import TelegramClient, events
import asyncio
from keep_alive import keep_alive  # Render serverda tirik tutish uchun

# === SOZLAMALAR ===
API_ID = 25501859
API_HASH = "3794184d222264f05dbc4622f3962b5f"
SESSION_NAME = "userbot_session"

# Avtomatik javob matni
AUTO_REPLY = "Hozir javob bera olmayman. Keyinroq yozsangiz, albatta javob beraman."

async def main():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        # Faqat private chatlarga javob beradi (guruh emas)
        if not event.is_private:
            return

        try:
            await event.reply(AUTO_REPLY)
            sender = await event.get_sender()
            print(f"✅ Javob yuborildi: {sender.first_name} ({event.chat_id})")
        except Exception as e:
            print(f"⚠️ Xatolik: {e}")

    print("🔄 Telegram userbot ishga tushmoqda...")
    await client.start()
    print("🤖 Userbot ishga tushdi! Har safar yangi xabar kelsa avtomatik javob beradi.")
    await client.run_until_disconnected()


if __name__ == "__main__":
    keep_alive()  # Render serverni tirik tutadi
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⏹ To‘xtatildi.")
