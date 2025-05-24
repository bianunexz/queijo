import streamlit as st  # Importa o Streamlit, que serve para criar o site de forma fácil e interativa
import random           # Importa o random, que serve para escolher uma bio aleatória das opções

# --- CSS para personalizar o visual do site ---
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(120deg, #232526 0%, #1a1a2e 100%);
}
/* Título principal */
h1, .main h1 {
    color: #fff !important; /* Branco */
    font-size: 3.5rem !important;
}
/* Labels dos campos (as perguntas) */
label, .stTextInput > label, .stTextInput label {
    color: #fff !important;
    white-space: nowrap; /* Deixa tudo em uma linha só */
    font-weight: bold;
    font-size: 1.08rem;
}
/* Caixas de texto (onde digita as respostas) com roxo escuro */
.stTextInput > div > div > input {
    background-color: #432c66 !important;
    color: #fff !important;
    border-radius: 10px;
    border: none;
    font-size: 1.08rem;
}
/* Botão em roxo claro */
.stButton>button {
    background-color: #7d5fff;
    color: #fff;
    border-radius: 25px;
    font-weight: bold;
    font-size: 1.1rem;
    margin-top: 10px;
    border: none;
}
.stButton>button:hover {
    background-color: #a685e2;
    color: #fff;
}
/* Caixa do código da bio gerada */
.stCodeBlock {
    background: #282c34;
    color: #fff;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)
# Todo esse bloco serve para mudar as cores, o fundo, as caixas e o botão do site

# Banner com a logo do Instagram e título
st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 16px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Logo Instagram" width="70" style="margin-right: 20px;">
        <h1 style="color: #fff; margin-bottom: 0;">Gerador de Bio Criativa</h1>
    </div>
    """,
    unsafe_allow_html=True
)


# Subtítulo e explicação centralizados
st.markdown("""
<div style="text-align:center; color:#e0e0e0; font-size:18px; margin-bottom:32px;">
Responda as perguntas e receba sugestões incríveis para sua bio no Instagram, LinkedIn e mais!
</div>
""", unsafe_allow_html=True)


# Perguntas para o usuário preencher 
nome = st.text_input("Seu nome (opcional):")  # Campo para digitar o nome (opcional)
profissao = st.text_input("Profissão ou área de atuação:")  # Campo da profissão
hobbies = st.text_input("Hobbies ou paixões:")  # Campo dos hobbies
frase = st.text_input("Uma frase favorita ou lema (opcional):")  # Campo para frase inspiradora (opcional)
adjetivo = st.text_input("Como você se define em uma palavra? (ex: criativo, dedicado)")  # Campo para um adjetivo

# Escolha da rede social desejada
rede = st.selectbox(
    "Para qual rede social você quer a bio?",
    ["Instagram", "LinkedIn", "Twitter/X", "TikTok", "Outra"]
)

# Botão para gerar as bios
if st.button("✨ Gerar Bios!"):
    bios = []  # Lista onde vão ficar as sugestões de bios

    # Monta as frases de acordo com a rede social escolhida
    if rede == "Instagram":
        bios.append(f"{adjetivo.capitalize()} | {profissao} | {hobbies}\n {frase}" if frase else f"{adjetivo.capitalize()} | {profissao} | {hobbies}")
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
        bios.append(f"{profissao} que ama {hobbies} \n{frase}" if frase else f"{profissao} que ama {hobbies} ")
        bios.append(f"Conteúdo: {profissao} & {hobbies}\nSiga para mais! ")
    else:
        bios.append(f"{adjetivo.capitalize()} {profissao} • {hobbies}\n{frase}" if frase else f"{adjetivo.capitalize()} {profissao} • {hobbies}")
  
    st.subheader("Suas bios criativas:")  # Título antes das bios

    # Mostra todas as bios geradas em caixas de código para copiar fácil
    for bio in bios:
        st.code(bio, language="markdown")

# --- Rodapé ---
st.markdown("""
---
<div style="text-align:center">
    <span style="color:#b8b8ff">@bia.nunexz</span>
</div>
""", unsafe_allow_html=True)

