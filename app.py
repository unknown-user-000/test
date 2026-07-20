import os

from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Link Boost Business
PAYMENT_LINK_BOT = "https://boostservices.boostbusiness.my/op/7Lx82Rxt"
PAYMENT_LINK_MATH_APP = "https://boostservices.boostbusiness.my/op/UmcwJEwp"

# Link WhatsApp untuk iPad / Tablet
IPAD_WHATSAPP_LINK = "https://wa.me/message/YKG56UO7SM5MD1"

# Nombor WhatsApp admin tanpa simbol +
ADMIN_WHATSAPP = "60172310958"


def main_menu() -> str:
    return """
Hai 👋 Selamat datang ke *Digital Business Store*.

Kami menyediakan produk digital dan servis automasi WhatsApp.

Sila pilih:

1️⃣ App Matematik
2️⃣ Servis WhatsApp Bot
3️⃣ iPad / Tablet
4️⃣ Cara Pembayaran
5️⃣ Semak Pembayaran
6️⃣ Hubungi Admin

Anda juga boleh taip:
*TANYA*, *PERTANYAAN*, *ASK* atau *QUESTION*

Balas nombor *1 hingga 6*.
""".strip()


@app.route("/", methods=["GET"])
def home():
    return "WhatsApp Business Bot sedang aktif ✅", 200


@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_message = request.form.get("Body", "").strip()
    sender = request.form.get("From", "")
    message = incoming_message.lower()

    response = MessagingResponse()
    reply = response.message()

    # Menu utama
    if message in {
        "hi",
        "hai",
        "hello",
        "menu",
        "start",
        "mula",
        "assalamualaikum",
        "salam",
    }:
        reply.body(main_menu())

    # App Matematik
    elif message in {
        "1",
        "app matematik",
        "matematik",
        "math app",
        "aplikasi matematik",
    }:
        reply.body(
            f"""
📚 *APP MATEMATIK*

Aplikasi pembelajaran Matematik yang sesuai digunakan melalui telefon, tablet atau iPad.

✅ Aktiviti Matematik interaktif
✅ Sesuai untuk pembelajaran kanak-kanak
✅ Akses produk secara digital
✅ Mudah digunakan
✅ Boleh belajar pada bila-bila masa

💳 *Bayar melalui Boost Business:*

{PAYMENT_LINK_MATH_APP}

Selepas pembayaran dibuat, balas menggunakan format berikut:

*BAYAR APP*

Nama:
Jumlah:
Nombor rujukan Boost:
Tarikh pembayaran:

Anda juga boleh menghantar screenshot resit pembayaran.
""".strip()
        )

    # Servis WhatsApp Bot
    elif message in {
        "2",
        "whatsapp bot",
        "bot whatsapp",
        "servis whatsapp bot",
        "setup bot",
        "automation bot",
    }:
        reply.body(
            f"""
🤖 *SERVIS SETUP WHATSAPP BOT*

Kami membantu menyediakan bot WhatsApp untuk bisnes anda.

Bot boleh digunakan untuk:

✅ Menjawab pertanyaan pelanggan
✅ Memberikan menu produk dan servis
✅ Menghantar payment link
✅ Mengambil maklumat pelanggan
✅ Menjawab soalan lazim
✅ Mengarahkan pelanggan kepada admin
✅ Mengurus tempahan secara automatik

💳 *Bayar setup melalui Boost Business:*

{PAYMENT_LINK_BOT}

Selepas pembayaran dibuat, balas menggunakan format berikut:

*BAYAR BOT*

Nama:
Nama bisnes:
Jenis bisnes:
Nombor rujukan Boost:
Tarikh pembayaran:

Admin akan menghubungi anda selepas pembayaran disahkan.
""".strip()
        )

    # iPad / Tablet
    elif message in {
        "3",
        "ipad",
        "tablet",
        "ipad tablet",
        "beli ipad",
    }:
        reply.body(
            f"""
📱 *iPAD / TABLET*

Untuk melihat katalog, harga dan stok semasa, tekan link berikut:

{IPAD_WHATSAPP_LINK}

Selepas membuka link, sila beritahu model iPad atau tablet yang anda cari.

Contoh maklumat:

Model:
Kapasiti:
Warna:
Bajet:
Lokasi:

Taip *MENU* untuk kembali ke menu utama.
""".strip()
        )

    # Cara pembayaran
    elif message in {
        "4",
        "bayar",
        "payment",
        "cara pembayaran",
        "payment link",
        "boost",
    }:
        reply.body(
            f"""
💳 *CARA PEMBAYARAN*

Pilih payment link mengikut produk atau servis:

📚 *App Matematik*
{PAYMENT_LINK_MATH_APP}

🤖 *Setup WhatsApp Bot*
{PAYMENT_LINK_BOT}

Cara membuat pembayaran:

1. Tekan link Boost Business.
2. Masukkan maklumat yang diperlukan.
3. Lengkapkan pembayaran.
4. Simpan nombor rujukan transaksi.
5. Hantar nombor rujukan atau screenshot resit kepada kami.

Pembayaran akan disemak oleh admin.
""".strip()
        )

    # Semak pembayaran
    elif message in {
        "5",
        "semak bayaran",
        "semak pembayaran",
        "status pembayaran",
        "payment status",
        "check payment",
    }:
        reply.body(
            """
🧾 *SEMAK PEMBAYARAN*

Sila hantar maklumat menggunakan format berikut:

*SEMAK BAYARAN*

Nama:
Produk atau servis:
Jumlah:
Nombor rujukan Boost:
Tarikh pembayaran:

Anda juga boleh menghantar screenshot resit.

Status pembayaran akan disemak oleh admin.
""".strip()
        )

    # Hubungi admin
    elif message in {
        "6",
        "admin",
        "agent",
        "manusia",
        "hubungi admin",
        "contact admin",
    }:
        reply.body(
            f"""
👩‍💼 *HUBUNGI ADMIN*

Tekan link berikut untuk menghubungi admin:

https://wa.me/{ADMIN_WHATSAPP}

Sila tinggalkan maklumat berikut:

Nama:
Produk atau servis:
Pertanyaan:

Admin akan membalas secepat mungkin.
""".strip()
        )

    # Buyer menaip pertanyaan dalam ayat pendek atau panjang
    elif any(
        keyword in message
        for keyword in [
            "pertanyaan",
            "nak tanya",
            "saya nak tanya",
            "tanya",
            "ask",
            "question",
            "inquiry",
            "enquiry",
            "help",
            "bantuan",
        ]
    ):
        reply.body(
            f"""
💬 *PERTANYAAN PELANGGAN*

Untuk bercakap terus dengan admin, tekan link berikut:

https://wa.me/{ADMIN_WHATSAPP}

Sila sertakan:

Nama:
Produk atau servis:
Pertanyaan anda:

Admin akan membalas secepat mungkin.

Taip *MENU* untuk kembali ke menu utama.
""".strip()
        )

    # Bukti bayaran App Matematik
    elif message.startswith("bayar app"):
        reply.body(
            """
Terima kasih ✅

Maklumat pembayaran *App Matematik* telah diterima.

Status: *Menunggu semakan admin*

Selepas pembayaran disahkan, akses produk akan diberikan kepada anda.
""".strip()
        )

    # Bukti bayaran WhatsApp Bot
    elif message.startswith("bayar bot"):
        reply.body(
            """
Terima kasih ✅

Maklumat pembayaran *Setup WhatsApp Bot* telah diterima.

Status: *Menunggu semakan admin*

Selepas pembayaran disahkan, admin akan menghubungi anda untuk mendapatkan:

• Nama bisnes
• Senarai produk atau servis
• Harga
• Soalan lazim pelanggan
• Payment link
• Gaya jawapan bot
""".strip()
        )

    # Semakan bayaran
    elif message.startswith("semak bayaran"):
        reply.body(
            """
Maklumat pembayaran telah diterima 🧾

Status semasa: *Menunggu semakan admin*

Admin akan menyemak pembayaran berdasarkan nombor rujukan Boost yang diberikan.
""".strip()
        )

    # Pilihan tidak dikenali
    else:
        reply.body(
            """
Maaf, saya tidak memahami pilihan tersebut.

Taip *MENU* untuk melihat menu utama.

1️⃣ App Matematik
2️⃣ Servis WhatsApp Bot
3️⃣ iPad / Tablet
4️⃣ Cara Pembayaran
5️⃣ Semak Pembayaran
6️⃣ Hubungi Admin

Atau taip *TANYA* untuk bercakap dengan admin.
""".strip()
        )

    print(f"Mesej daripada {sender}: {incoming_message}")

    return Response(str(response), mimetype="text/xml")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
