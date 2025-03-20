import streamlit as st
import requests
import matplotlib.pyplot as plt

API_KEY = "93d1905d727918bcb58024ebb09c3416"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},UZ&appid={API_KEY}&units=metric&lang=uz"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {"Harorat": data['main']['temp'], "Namlik": data['main']['humidity'], "Shamol": data['wind']['speed']}
    else:
        return None

osimliklar = {
    "Olma": {"Harorat": (15, 25), "Namlik": (60, 70), "Rasm": "https://www.auchan.ru/f/c/insecure/w:620/plain/https://www.auchan.ru/files/original/19867054"},
    "O‘rik": {"Harorat": (20, 30), "Namlik": (50, 60), "Rasm": "https://main-cdn.sbermegamarket.ru/big2/hlr-system/116/186/072/910/181/452/100029367888b1.jpg"},
    "Pomidor": {"Harorat": (18, 30), "Namlik": (50, 70), "Rasm": "https://avatars.mds.yandex.net/i?id=df64a76bd8c27f17d010b2c717361d07f98c39ee-10261182-images-thumbs&n=13"},
    "Limon": {"Harorat": (20, 35), "Namlik": (70, 80), "Rasm": "https://avatars.mds.yandex.net/i?id=08c5da42c792cb4a96215a30a08e7c7bc6bbe26c-5132176-images-thumbs&n=13"},
    "Banan": {"Harorat": (22, 32), "Namlik": (75, 85), "Rasm": "https://avatars.mds.yandex.net/i?id=0530774768189981d802db61110d3b7ce3294a18-4569781-images-thumbs&n=13 "},
    "Bodring": {"Harorat": (18, 30), "Namlik": (60, 80), "Rasm": "https://avatars.mds.yandex.net/i?id=9619d4f4a98afca6bda5681e31681d212d004e1e-5499277-images-thumbs&n=13"},
    "Sabzi": {"Harorat": (12, 22), "Namlik": (50, 70), "Rasm": "https://avatars.mds.yandex.net/i?id=f455f788d82d9ada2b7bdd4923c2d94a6459f27b-5226766-images-thumbs&n=13"},
    "Karam": {"Harorat": (10, 22), "Namlik": (60, 80), "Rasm": "https://avatars.mds.yandex.net/i?id=2fbe7572d1b979f01923c9121e9ee8c5c1b0d719-4568742-images-thumbs&n=13"},
    "Gilos": {"Harorat": (15, 28), "Namlik": (55, 70), "Rasm": "https://i.pinimg.com/736x/03/70/2b/03702b90bd29ac0c4f3770678ff56a78.jpg"},
    "Shaftoli": {"Harorat": (18, 30), "Namlik": (60, 75), "Rasm": "https://avatars.mds.yandex.net/i?id=75315163095a0684e37dbb497d7320ef7307c631-4034735-images-thumbs&n=13"},
    "Anor": {"Harorat": (25, 35), "Namlik": (40, 60), "Rasm": "https://avatars.mds.yandex.net/get-altay/13212679/2a0000019272339ba9f27823f2ed20ffa5ea/XXXL"},
    "Gulkaram": {"Harorat": (12, 22), "Namlik": (60, 80), "Rasm": "https://avatars.mds.yandex.net/i?id=6581736039b84ea4490d64dd432bd78b22b2d66b-10093836-images-thumbs&n=13"},
    "Tarvuz": {"Harorat": (25, 35), "Namlik": (40, 60), "Rasm": "https://cdn.culture.ru/images/f2f82675-5455-56f6-8a25-4adb5a24b87d"},
    "Qovun": {"Harorat": (25, 35), "Namlik": (40, 60), "Rasm": "https://main-cdn.sbermegamarket.ru/big2/hlr-system/-10/970/834/992/251/38/100048530720b1.jpg"},
    "Kartoshka": {"Harorat": (12, 22), "Namlik": (60, 80), "Rasm": "https://cache3.youla.io/files/images/780_780/5c/c5/5cc57ff76c4b44b31d197aa3.jpg"},
    "Bulg‘or qalampiri": {"Harorat": (20, 30), "Namlik": (50, 70), "Rasm": "https://www.healthbenefitstimes.com/9/gallery/cayenne-pepper/Cayenne-peppers.jpg"},
    "No‘xat": {"Harorat": (10, 20), "Namlik": (60, 75), "Rasm": "https://avatars.mds.yandex.net/i?id=22bda6a74654a69e68a54d2b5a65e42a4d308f95-10813564-images-thumbs&n=13"},
    "Loviya": {"Harorat": (18, 28), "Namlik": (50, 70), "Rasm": "https://avatars.mds.yandex.net/i?id=679fcb43f081394f1888412e3de2a6612aa88dd1-4303190-images-thumbs&n=13"},
    "Makkajo‘xori": {"Harorat": (30, 40), "Namlik": (20, 40), "Rasm": "https://avatars.mds.yandex.net/i?id=5a3ab163a9edb34c51b3fc0672017fdd0ff46dac-10875714-images-thumbs&n=13"}
}

def main():
    st.set_page_config(page_title="GREENGUIDE", layout="wide")
    st.markdown(
        """
        <style>
        .title {
            text-align: center; 
        }
        </style>
        <h1 class="title">GREENGUIDE</h1>
        """,
        unsafe_allow_html=True
    )

    menu = ["Ob-havo", "O‘simlik va Mevalar", "Foydali o'simlik va mevalar", "Ko‘rsatmalar", "Contact"]
    if "selected_page" not in st.session_state:
        st.session_state.selected_page = "Ob-havo"

    cols = st.columns(len(menu))
    for i, item in enumerate(menu):
        with cols[i]:
            if st.button(item, key=item):
                st.session_state.selected_page = item

    if st.session_state.selected_page == "Ob-havo":
        st.header("Ob-havo ma’lumoti")
        viloyatlar = [
            "Toshkent", "Andijon", "Fergana", "Namangan", "Samarqand",
            "Urganch", "Navoiy", "Qashqadaryo", "Tirmiz", "Jizzax", "Buxoro", "Sirdaryo"
        ]
        shahar = st.selectbox("🌍 Viloyatni tanlang:", viloyatlar)
        weather_data = get_weather(shahar)
        if weather_data:
            api_temp = weather_data['Harorat']
            namlik = weather_data['Namlik']
            api_wind_speed = weather_data['Shamol']

            st.subheader(f"📡 {shahar} viloyati ob-havo ma'lumoti (API)")
            st.write(f"**🌡 Harorat:** {api_temp}°C")
            st.write(f"**💧 Namlik:** {namlik}%")
            st.write(f"**🌬 Shamol tezligi:** {api_wind_speed} m/s")

            st.subheader("✍️ Qo‘lda ob-havo ma’lumotlarini kiriting")
            user_temp = st.number_input("🌡 Harorat (°C):", min_value=-10.0, max_value=50.0, value=float(api_temp))
            user_humidity = st.number_input("💧 Namlik (%):", min_value=0, max_value=100, value=int(namlik))
            user_wind_speed = st.number_input("🌬 Shamol tezligi (m/s):", min_value=0.0, max_value=50.0, value=float(api_wind_speed))

            st.subheader("📊 Ob-havo ma’lumotlari diagrammasi")
            labels = ["Harorat", "Namlik ", "Shamol tezligi", "Kiritilgan Harorat", "Kiritilgan Namlik", "Kiritilgan Shamol"]
            values = [api_temp, namlik, api_wind_speed, user_temp, user_humidity, user_wind_speed]

            fig, ax = plt.subplots(figsize=(12, 4))
            ax.bar(labels, values, color=['blue', 'green', 'red', 'cyan', 'lime', 'orange'])
            ax.set_ylabel("Qiymatlar")
            ax.set_title(f"{shahar} viloyati ob-havo tahlili")
            plt.xticks(rotation=30)
            st.pyplot(fig)
        else:
            st.error(" Ob-havo ma'lumotlarini olishda xatolik yuz berdi!")

    elif st.session_state.selected_page == "O‘simlik va Mevalar":
        st.header("O‘simliklar va mevalarning o‘sish sharoitlari")
        tanlangan_osimlik = st.selectbox("O‘simlik va mevani tanlang:", list(osimliklar.keys()))
        if tanlangan_osimlik:
            info = osimliklar[tanlangan_osimlik]
            st.subheader(tanlangan_osimlik)
            st.write(f"**Harorat:** {info['Harorat']}")
            st.write(f"**Namlik:** {info['Namlik']}")
            if 'Rasm' in info:
                st.image(info['Rasm'], caption=tanlangan_osimlik, width=300)

    elif st.session_state.selected_page == "Foydali o'simlik va mevalar":
        tanlov = st.radio("Ob-havo ma'lumotlarini qanday kiritmoqchisiz?", ("Viloyatni tanlash", "Qo'lda kiritish"))
        if tanlov == "Viloyatni tanlash":
            st.header("Viloyat tanlang")
            viloyat = st.selectbox("Viloyatni tanlang:", [
                "Toshkent", "Andijon", "Fergana", "Namangan", "Samarqand",
                "Urganch", "Navoiy", "Qashqadaryo", "Tirmiz", "Jizzax", "Buxoro", "Sirdaryo"
            ])
            if viloyat:
                obhavo = get_weather(viloyat)
                if obhavo:
                    harorat = obhavo['Harorat']
                    namlik = obhavo['Namlik']
                    st.write(f"🌡 **Harorat:** {harorat}°C")
                    st.write(f"💧 **Namlik:** {namlik}%")
                    mos_osimliklar = []
                    for o, sh in osimliklar.items():
                        min_temp, max_temp = sh['Harorat']
                        min_humidity, max_humidity = sh['Namlik']
                        if (min_temp <= harorat <= max_temp) or (min_humidity <= namlik <= max_humidity):
                            mos_osimliklar.append(o)
                    if mos_osimliklar:
                        st.subheader("✅ Ushbu ob-havo sharoitiga mos keladigan o‘simliklar va mevalar:")
                        st.write(", ".join(mos_osimliklar))
                        st.subheader("🌱 Mos keladigan o'simliklar va mevalar rasmlari:")
                        cols = st.columns(3)
                        for i, osimlik in enumerate(mos_osimliklar):
                            with cols[i % 3]:
                                st.image(osimliklar[osimlik]['Rasm'], caption=osimlik, width=200)
                    else:
                        st.write("❌ Afsuski, hech qanday o‘simlik va meva mos kelmadi.")
                else:
                    st.error("❌ Ob-havo ma'lumotlarini olishda xatolik yuz berdi!")
        else:
            st.subheader("✍️ Qo‘lda ob-havo ma’lumotlarini kiriting")
            harorat = st.number_input("🌡 Harorat (°C):", min_value=-10.0, max_value=50.0)
            namlik = st.number_input("💧 Namlik (%):", min_value=0, max_value=100)
            mos_osimliklar = []
            for o, sh in osimliklar.items():
                min_temp, max_temp = sh['Harorat']
                min_humidity, max_humidity = sh['Namlik']
                if (min_temp <= harorat <= max_temp) or (min_humidity <= namlik <= max_humidity):
                    mos_osimliklar.append(o)
            if mos_osimliklar:
                st.subheader("✅ Ushbu ob-havo sharoitiga mos keladigan o‘simliklar va mevalar:")
                st.write(", ".join(mos_osimliklar))
                st.subheader("🌱 Mos keladigan o'simliklar va mevalar rasmlari:")
                cols = st.columns(3)
                for i, osimlik in enumerate(mos_osimliklar):
                    with cols[i % 3]:
                        st.image(osimliklar[osimlik]['Rasm'], caption=osimlik, width=200)
            else:
                st.write("❌ Afsuski, hech qanday o‘simlik va meva mos kelmadi.")

    elif st.session_state.selected_page == "Ko‘rsatmalar":
        st.header("1.Ko'chatni tayyorlash")
        st.video("https://youtu.be/eFkjqbOtCDs?si=dudExa-4Q8MO50bC")
        st.subheader("2. Mevali daraxtlarning ko'chatini ekish tartibi")
        st.video("https://youtu.be/_r1Ewbfg1kM?si=VufYfowOGL2lv5ZE")
        st.subheader("3. Ko'chatlarga yozgi shakl berish")
        st.video("https://youtu.be/i88ZKKT9hng?si=gELJctDqt_UmjP9L")
        st.subheader("4.Ko'chatlarga qishki shakl berish")
        st.video("https://youtu.be/NGct-HYuEDs?si=g_fKvv6xDP5XFwq7")
        st.subheader("5. Daraxtga shakl berish")
        st.video("https://youtu.be/YtpFCKlFxRo?si=o-3FyivzzIWT2exb")
        st.subheader("6.Danakli va urug'li mevalarga shakl berish bo'yicha maslahatlar")
        st.video("https://youtu.be/2kdJFxZskrQ?si=_DpnEGkGT1f-ao95")

    elif st.session_state.selected_page == "Contact":
        st.header("📞 Aloqa uchun Ma'lumotlarim")
        st.subheader("📧 E-mail")
        st.write("✉️ **akkaunt.for.hp@gmail.com**")
        st.write("✉️ **oashirov383@gmail.com**")
        st.write("✉️ **askarmain7@gmail.com**")
        st.subheader("💬 Telegram")
        st.write("🔗 [@jafar_master](https://t.me/jafar_master)")
        st.write("🔗 [@Bek_042020](https://t.me/Bek_042020)")
        st.write("🔗 [@gulyamov](https://t.me/gulyamov)")
            # Telefon raqam
        st.subheader("📱 Telefon")
        st.write("📞 **+998 94 344 04 45**")
        st.write("📞 **+998 88 909 03 07**")
        st.write("📞 **+998 90 511 75 15**")
     # Fikr-mulohaza shakli
        st.subheader("📩 Fikr-mulohazalaringiz bo'lsa ")
        feedback = st.text_area("Sharxingizni yozing:")
        if st.button("Yuborish"):
                if feedback:
                    st.success("Rahmat! Sharxingiz qabul qilindi. 📩")
                else:
                    st.warning("Iltimos, sharxingizni kiriting!")
# Contact sahifasini chaqirish


        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
        main()
