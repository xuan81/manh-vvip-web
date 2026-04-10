import streamlit as st
import random

# --- CẤU HÌNH GIAO DIỆN GAMING VVIP ---
st.set_page_config(page_title="Hello Teacher", page_icon="👑", layout="centered")

# Nhúng CSS "Siêu Cấp Thượng Hạng"
st.markdown("""
    <style>
    /* Nền VVIP tối thượng (charcoal black & gold) */
    .stApp {
        background: radial-gradient(circle, #050505 0%, #000000 100%);
        color: #fff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Hiệu ứng Nền Vũ Trụ Vàng (Gợi ý VIP) */
    .vvip-background {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: transparent;
        z-index: -2; /* Nền xa nhất */
    }
    .vvip-gradient-glow {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(135deg, rgba(20,20,30,0.8) 0%, rgba(10,10,15,1) 50%, rgba(20,20,30,0.8) 100%);
        opacity: 0.9;
    }

    /* Tiêu đề Tia Sét VIP */
    .gaming-title {
        font-size: 3rem !important;
        font-weight: 900;
        text-align: center;
        text-transform: uppercase;
        color: #ffd700; /* Vàng kim */
        text-shadow: 0 0 10px #ffd700, 0 0 20px #f00, 0 0 40px #ffd700;
        animation: lightning-gold 1.5s infinite;
        margin-bottom: 30px;
    }
    @keyframes lightning-gold {
        0%, 100% { opacity: 1; filter: brightness(1); }
        50% { opacity: 0.8; filter: brightness(1.5) drop-shadow(0 0 15px #fff); }
    }

    /* Ô nhập mật khẩu RGB Cầu Vồng (VIP hơn) */
    div[data-baseweb="input"] {
        border: none !important;
        padding: 5px;
        background: linear-gradient(90deg, #ffd700, #ff0000, #ffd700, #ff0000, #ffd700);
        background-size: 400%;
        border-radius: 10px;
        animation: rgb-border-vvip 10s linear infinite;
    }
    @keyframes rgb-border-vvip {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    input {
        background-color: #000 !important;
        color: #fff !important;
        border-radius: 5px !important;
    }

    /* Nút bấm VIP Cấp Cao */
    .stButton>button {
        background: linear-gradient(45deg, #ffd700, #f00);
        color: #000; /* Chữ đen sang trọng */
        border: none;
        padding: 15px 30px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 50px;
        box-shadow: 0 5px 20px rgba(255, 215, 0, 0.5);
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        transform: scale(1.05) translateY(-3px);
        box-shadow: 0 10px 40px rgba(255, 215, 0, 0.8);
        filter: brightness(1.2);
    }

    /* Hiệu ứng hạt kim loại VIP Floating */
    .particle {
        position: fixed;
        border-radius: 50%;
        pointer-events: none;
        z-index: -1;
        animation: float linear infinite;
    }
    @keyframes float {
        0% { transform: translateY(0) translateX(0); opacity: 0; }
        20% { opacity: 1; }
        100% { transform: translateY(-100vh) translateX(30px); opacity: 0; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- TẠO HIỆU ỨNG HẠT KIM LOẠI VIP (Cho nền thượng hạng) ---
particle_html = '<div class="vvip-background"><div class="vvip-gradient-glow"></div>'
for i in range(25):
    size = random.randint(3, 7)
    left = random.randint(0, 100)
    dur = random.randint(8, 20)
    delay = random.randint(0, 10)
    color = random.choice(["rgba(255, 215, 0, 0.5)", "rgba(255, 255, 255, 0.3)"])
    particle_html += f'<div class="particle" style="width:{size}px; height:{size}px; left:{left}%; animation-duration:{dur}s; animation-delay:{delay}s; background:{color};"></div>'
particle_html += '</div>'
st.markdown(particle_html, unsafe_allow_html=True)

# --- XỬ LÝ BẢO MẬT ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def check_password():
    if st.session_state["password"] == "manh1234": # Mật khẩu VVIP
        st.session_state["authenticated"] = True
        st.balloons()
    else:
        st.error("Mật khẩu sai")

if not st.session_state['authenticated']:
    st.markdown('<p class="gaming-title">', unsafe_allow_html=True)
    st.write("---")
    st.text_input("NHẬP MÃ", type="password", key="password", on_change=check_password)
    st.info("🔥 Mật khẩu là manh1234")
    st.stop()

# --- NỘI DUNG ---
st.markdown('<p class="gaming-title">🔥Tin học </p>', unsafe_allow_html=True)
st.snow()
st.video("https://www.youtube.com/watch?v=CjxNsYAQNf8")

st.markdown("""
    <div style="background: rgba(0,0,0,0.7); padding: 25px; border-radius: 15px; border-left: 5px solid #ffd700; border-right: 5px solid #ff0000;">
        <h3 style="color: #ffd700; text-shadow: 0 0 10px #f00; margin-top: 0;">🎖️ Thông Tin</h3>
        <p><b>- Chủ sở hữu:</b> Mạnh-----Thành-----Hồng</p>
        <p><b>- Trạng thái:</b> Hoạt động</p>
        <p><b>- Công nghệ:</b> Python - Github</p>
    </div>
""", unsafe_allow_html=True)

if st.button("🔴 THOÁT "):
    st.session_state['authenticated'] = False
    st.rerun()
