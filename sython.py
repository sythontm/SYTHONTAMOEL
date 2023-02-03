from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from config import *
import asyncio
from telethon import events
# -

sython.start()
c = requests.session()
bot_username = '@t06bot'
bot_usernamee = '@A_MAN9300BOT'

y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

LOGS = logging.getLogger(__name__)

DEVS = [
    5159123009,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]


async def join_channel():
    try:
        await sython(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass






@sython.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
**☆ WELCOME TO SOURCE SYTHON
☆ VERSION : 1.3
☆ PING : `{ms}`
☆ DATE : `{m9zpi}`
☆ ID : `{event.sender_id}`
☆ SOURCE SYTHON : @SAYTHONH**

-قـم بأرسال `.الاوامر`
''')



    


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython.get_entity(bot_username)
        await sython.send_message('@t06bot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython.get_entity(bot_username)
        await sython.send_message('@t06bot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython.get_messages('@t06bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython.get_messages('@t06bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython(ImportChatInviteRequest(bott))
                msg2 = await sython.get_messages('@t06bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython.send_message(event.chat_id, "تم الانتهاء من التجميع !")


##################


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع الجوكر"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython.get_entity(bot_usernamee)
        await sython.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython.get_entity(bot_usernamee)
        await sython.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython(ImportChatInviteRequest(bott))
                msg2 = await sython.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython.send_message(event.chat_id, "تم الانتهاء من التجميع !")





print("- sython Userbot Running ..")
sython.run_until_disconnected()
