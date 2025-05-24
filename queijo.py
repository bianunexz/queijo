import streamlit as st
import random

# ---------- Personalização via CSS ----------
st.markdown("""
<style>
body {
    background-color: #1a1a2e;
}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(120deg, #232526 0%, #1a1a2e 100%);
}
h1, h2, h3, h4, h5, h6 {
    color: #ffe066 !important;
}
.stTextInput>div>div>input {
    background-color: #23243a;
    color: #fff;
}
.stButton>button {
    background-color: #ffe066;
    color: #232526;
    border-radius: 25px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #ffbe0b;
    color: #232526;
}
.stCodeBlock {
    background: #fffbe6;
    color: #232526;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Banner com imagem ----------
st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: center;">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="Ícone de bio" width="80" style="margin-right: 20px;">
        <h1 style="color: #ffe066;">Gerador de Bio Criativa 🌟</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<div style="text-align:center; color:#eee; font-size:18px; margin-bottom:32px;">
Responda as perguntas e receba sugestões incríveis para sua bio no Instagram, LinkedIn e mais!
</div>
""", unsafe_allow_html=True)

# ---------- Perguntas ----------
nome = st.text_input("Seu nome (opcional):")
profissao = st.text_input("Profissão ou área de atuação:")
hobbies = st.text_input("Hobbies ou paixões:")
frase = st.text_input("Uma frase favorita ou lema (opcional):")
adjetivo = st.text_input("Como você se define em uma palavra? (ex: criativo, dedicado)")

rede = st.selectbox(
    "Para qual rede social você quer a bio?",
    ["Instagram", "LinkedIn", "Twitter/X", "TikTok", "Outra"]
)

if st.button("✨ Gerar Bios!"):
    bios = []
    if rede == "Instagram":
        bios.append(f"{adjetivo.capitalize()} | {profissao} | {hobbies}\n✨ {frase}" if frase else f"{adjetivo.capitalize()} | {profissao} | {hobbies}")
        bios.append(f"{profissao} apaixonado(a) por {hobbies}\n{frase}" if frase else f"{profissao} apaixonado(a) por {hobbies}")
        bios.append(f"{nome} • {profissao}\n{hobbies}\n\"{frase}\"" if nome and frase else f"{profissao} • {hobbies}")
    elif rede == "LinkedIn":
        bios.append(f"{profissao} focado(a) em resultados e apaixonado(a) por {hobbies}.")
        bios.append(f"Profissional {adjetivo} com experiência em {profissao} | {hobbies}")
        bios.append(f"{nome}, {profissao}. {frase}" if nome and frase else f"{profissao} dedicado(a) a {hobbies}.")
    elif rede == "Twitter/X":
        bios.append(f"{adjetivo.capitalize()} em {profissao} • {hobbies}\n{frase}" if frase else f"{adjetivo.capitalize()} em {profissao} • {hobbies}")
        bios.append(f"{profissao} | {hobbies}\n{frase}" if frase else f"{profissao} | {hobbies}")
    elif rede == "TikTok":
        bios.append(f"{profissao} que ama {hobbies} 💡\n{frase}" if frase else f"{profissao} que ama {hobbies} 💡")
        bios.append(f"Conteúdo: {profissao} & {hobbies}\nSiga para mais! 🚀")
    else:
        bios.append(f"{adjetivo.capitalize()} {profissao} • {hobbies}\n{frase}" if frase else f"{adjetivo.capitalize()} {profissao} • {hobbies}")

    st.subheader("Suas bios criativas:")
    for bio in bios:
        st.code(bio, language="markdown")

st.markdown("""
---
<div style="text-align:center">
    <span style="color:#ffe066">Feito com ❤️ no Streamlit</span>
</div>
""", unsafe_allow_html=True)

