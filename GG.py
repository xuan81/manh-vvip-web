import streamlit as st
import streamlit.components.v1 as components

# Cấu hình Web
st.set_page_config(page_title="MẠNH THÀNH HỒNG AAA", layout="wide")

# Kiểm tra mật khẩu (Dùng biến đơn giản để không lỗi)
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

def check():
    if st.session_state["pw"] == "manh2026":
        st.session_state['auth'] = True
    else:
        st.error("MẬT KHẨU SAI!")

if not st.session_state['auth']:
    st.markdown("<h1 style='text-align:center; color:#ff003c;'>🔒 HỆ THỐNG BẢO MẬT</h1>", unsafe_allow_html=True)
    st.text_input("NHẬP MK:", type="password", key="pw", on_change=check)
    st.stop()

# --- GIAO DIỆN GAME AAA ---
html_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap" rel="stylesheet">
    <style>
        body { background: #000; color: #fff; margin: 0; font-family: sans-serif; overflow-x: hidden; }
        #loader { position: fixed; inset: 0; background: #000; z-index: 99; display: flex; flex-direction: column; justify-content: center; align-items: center; transition: 1s; }
        .bar { width: 200px; height: 2px; background: #333; margin-top: 10px; position: relative; }
        .progress { position: absolute; height: 100%; width: 0; background: #ff003c; animation: load 2s forwards; }
        @keyframes load { to { width: 100%; } }
        .glitch { font-family: 'Orbitron'; font-size: 5vw; text-align: center; margin-top: 20vh; text-transform: uppercase; color: #fff; position: relative; }
        .glitch::before { content: 'MẠNH THÀNH HỒNG'; position: absolute; left: -2px; text-shadow: -2px 0 #ff003c; animation: g 0.3s infinite; }
        @keyframes g { 0% { transform: translate(0); } 50% { transform: translate(-2px, 2px); } 100% { transform: translate(0); } }
        .v-box { width: 80%; margin: 50px auto; border: 2px solid #ff003c; box-shadow: 0 0 30px #ff003c; border-radius: 15px; overflow: hidden; }
    </style>
</head>
<body>
    <div id="loader">
        <div style="font-family:'Orbitron'; color:#ff003c;">LOADING SYSTEM...</div>
        <div class="bar"><div class="progress"></div></div>
    </div>
    <div class="glitch">MẠNH THÀNH HỒNG</div>
    <div class="v-box">
        <iframe width="100%" height="500" src="https://www.youtube.com/embed/CjxNsYAQNf8" frameborder="0" allowfullscreen></iframe>
    </div>
    <script>
        window.onload = () => { setTimeout(() => { 
            document.getElementById('loader').style.opacity = '0'; 
            setTimeout(() => document.getElementById('loader').style.display = 'none', 1000); 
        }, 2000); };
    </script>
</body>
</html>
"""
components.html(html_code, height=1200, scrolling=True)
