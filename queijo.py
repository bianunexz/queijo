import streamlit as st
import random

# ---------- Personalização via CSS ----------
st.markdown("""
<style>
/* Fundo geral */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(120deg, #232526 0%, #1a1a2e 100%);
}
/* Título principal em branco */
h1, .main h1 {
    color: #fff !important;
    font-size: 3.5rem !important;
}
/* Subtítulos (labels) em uma linha só e cor clara */
label, .stTextInput > label, .stTextInput label {
    color: #ffe066 !important;
    white-space: nowrap;
    font-weight: bold;
    font-size: 1.1rem;
}
/* Caixas de resposta em roxo escuro */
.stTextInput > div > div > input {
    background-color: #3f2169 !important;
    color: #fff !important;
    border-radius: 10px;
    border: none;
    font-size: 1.1rem;
}
/* Botão estilizado */
.stButton>button {
    background-color: #ffe066;
    color: #232526;
    border-radius: 25px;
    font-weight: bold;
    font-size: 1.1rem;
    margin-top: 10px;
}
.stButton>button:hover {
    background-color: #ffbe0b;
    color: #232526;
}
/* Caixas de código */
.stCodeBlock {
    background: #fffbe6;
    color: #232526;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Banner com logo do Instagram ----------
st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 16px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Logo Instagram" width="70" style="margin-right: 20px;">
        <h1 style="color: #fff; margin-bottom: 0;">Gerador de Bio Criativa</h1>
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
