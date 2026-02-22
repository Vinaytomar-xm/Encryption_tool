import streamlit as st
from cryptography.fernet import Fernet

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Encryption Tool",
    page_icon="🔐",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.card {
    background: #161b22;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(0,0,0,0.4);
}
.title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #58a6ff;
}
.sub {
    text-align: center;
    color: #8b949e;
    margin-bottom: 25px;
}
.footer {
    text-align: center;
    color: #6e7681;
    font-size: 12px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- KEY ----------------
key = 'aACUphGs9XV1GmWNhlmSoOD8C7P3AXO4_IrlJm-ugNI='
cipher = Fernet(key)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("🔑 Encryption Key")
    st.code(key)
    st.info("Keep this key secret.\nAnyone with this key can decrypt messages.")

# ---------------- MAIN CARD ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("<div class='title'>🔐 Message Encryptor / Decryptor</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Secure your text using Fernet Encryption</div>", unsafe_allow_html=True)

msz = st.text_area(
    "✉️ Enter your message",
    height=120,
    placeholder="Type your secret message here..."
)

select = st.selectbox(
    "⚙️ Choose Action",
    ["Encrypt", "Decrypt"]
)

col1, col2 = st.columns(2)

with col1:
    submit = st.button("🚀 Submit", type="primary", use_container_width=True)

with col2:
    clear = st.button("🧹 Clear", type="primary", use_container_width=True)

# ---------------- LOGIC ----------------
if submit:
    if not msz.strip():
        st.warning("⚠️ Please enter a message first.")
    else:
        try:
            if select == "Encrypt":
                encrypted = cipher.encrypt(msz.encode())
                st.success("✅ Message Encrypted Successfully")
                st.code(encrypted.decode())
            else:
                decrypted = cipher.decrypt(msz.encode())
                st.success("✅ Message Decrypted Successfully")
                st.code(decrypted.decode())
        except Exception as e:
            st.error("❌ Invalid input or key!")
            st.caption(str(e))

if clear:
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>@ 2026 Built with ❤️ Vinay Singh Tomar</div>",
    unsafe_allow_html=True
)