import streamlit as st

st.set_page_config(
    page_title="EmagreceJá 💖",
    page_icon="🌸",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    .stApp {
        background: linear-gradient(180deg, #fff0f6 0%, #fff6fb 100%);
        font-family: 'Poppins', sans-serif;
    }
    .main-title { text-align:center; color:#e91e63; font-size:32px; font-weight:700; margin-bottom:10px; }
    .subtitle { text-align:center; color:#555; margin-bottom:30px; }
    .card { background:white; border-radius:14px; padding:18px; box-shadow:0 6px 15px rgba(233,30,99,0.1); text-align:center; }
    .price { color:#e91e63; font-weight:700; font-size:18px; margin-top:6px; }
    .btn { background:#e91e63; color:white; padding:8px 16px; border-radius:10px; border:none; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">🌸 EmagreceJá — Sua jornada leve e feminina</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Produtos ilustrativos e dicas para cuidar de você com carinho.</div>', unsafe_allow_html=True)

produtos = [
    {"nome": "Shake Proteico Rosa", "preco": "R$79,90", "img": "https://cdn-icons-png.flaticon.com/512/4314/4314507.png"},
    {"nome": "Chá Detox Floral", "preco": "R$39,90", "img": "https://cdn-icons-png.flaticon.com/512/1047/1047711.png"},
    {"nome": "Kit Fitness Rosa", "preco": "R$129,90", "img": "https://cdn-icons-png.flaticon.com/512/1754/1754160.png"}
]

cols = st.columns(3)
for col, p in zip(cols, produtos):
    with col:
        st.markdown(f"""
        <div class="card">
            <img src="{p['img']}" width="100"><br>
            <strong>{p['nome']}</strong><br>
            <span class="price">{p['preco']}</span><br><br>
            <button class="btn">Comprar (demo)</button>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 💌 Receba novidades")
nome = st.text_input("Seu nome")
email = st.text_input("Seu e-mail")
if st.button("Quero receber novidades 💖"):
    if nome and email:
        st.success(f"Obrigada, {nome}! (Demo)")
    else:
        st.error("Preencha nome e e-mail antes de enviar.")
