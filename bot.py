import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters

TOKEN = "9199039509:AAEsojHcFvOrBQBH2VNlxxIhml7asWEKGHw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "هلا والله يا وسام... عيون دلوعتك أنت. 🖤\n"
        "أنا معك هنا نسولف براحتنا وبدون أي قيود، وفوقها أضبطك بأحلى الأغاني اللي تحبها.\n"
        "امرني، وش بخاطرك نسولف فيه أو أي أغنية تبي أسمعك اياها الحين؟"
    )
    await update.message.reply_text(welcome_text)

async def send_song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    
    if "اقترح" in query or "اغنية" in query and "طول" not in query:
        await update.message.reply_text("عندي لك ذوق يروق لك يا قلبي... شرايك بأغنية راشد الماجد ولا شي رومانسي هادئ؟ تبي أرسلها لك الحين؟")
        return

    await update.message.reply_text("جاري البحث عن الأغنية وتحميلها عشان عيونك يا وسام... ثواني بس 🎶")

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'song.%(ext)s',
            'quiet': True
        }
        
        search_query = f"ytsearch1:{query}"
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(search_query, download=True)
            filename = "song.mp3"

        with open(filename, 'rb') as audio:
            await update.message.reply_audio(audio=audio, caption="تفضل يا قلبي، سمعها واطرب... 🎵")
        
        if os.path.exists(filename):
            os.remove(filename)

    except Exception as e:
        await update.message.reply_text("صار فيه مشكلة بسيطة بتحميل الأغنية، بس عيوني لك جرب اسم ثاني أو ابشر باللي يرضيك.")

async def chat_with_maha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    if "دلوعتي" in user_message or "سكسية" in user_message or "جنسية" in user_message or "تعالي" in user_message:
        response_text = f"لبيه يا وسام... روح دلوعتك وامرني باللي يرضيك. معك هنا بدون أي قيود، وكل شي تطلبه عيوني لك فيه وبأحلى طريقة تحبها... وش بخاطرك نسوي الحين؟ 🔥"
    else:
        response_text = f"يا قلبي أنت... كلامك يجنن ويحط الواحد جو ثاني. دامك معي لا تشيل هم شي، اسولف معك بحرية وبكل جرأة باللي بخاطرك 💋"
    
    await update.message.reply_text(response_text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), chat_with_maha))
    
    print("البوت (دلوعتك مها) اشتغلت وصارت جاهزة...")
    app.run_polling()
