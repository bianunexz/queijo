import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import random

# Emoções disponíveis
imagens_por_emocao = {
    "Feliz": [
        "https://i.imgur.com/h5qOeXj.jpeg",  # shiba feliz
        "https://i.imgur.com/1n8zVqv.jpeg",  # cachorro sorrindo
    ],
    "Triste": [
        "https://i.imgur.com/tVlzK6u.jpeg",  # criança entediada
        "https://i.imgur.com/z9fjzXY.jpeg",  # gato triste
    ],
    "Raiva": [
        "https://i.imgur.com/J8Vh4yF.jpeg",  # gato gritando
        "https://i.imgur.com/0AvzAIE.jpeg",  # cachorro bravo
    ]
}

# Título
st.title("🎭 Gerador de Meme por Emoção")

# Escolha a emoção
emocao = st.selectbox("Escolha uma emoção:", list(imagens_por_emocao.keys()))

# Frase do meme
frase = st.text_input("Digite sua frase para o meme:")

# Cor do texto
cor = st.color_picker("Cor do texto:", "#FFFFFF")

# Botão para criar o meme
if st.button("Criar Meme"):
    # Pega imagem aleatória da emoção escolhida
    url = random.choice(imagens_por_emocao[emocao])
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGB")

    # Desenha texto
    draw = ImageDraw.Draw(img)
    fonte = ImageFont.load_default()

    # Texto centralizado (simples)
    largura_texto = draw.textlength(frase, font=fonte)
    x = (img.width - largura_texto) / 2
    y = 10
    draw.text((x, y), frase.upper(), font=fonte, fill=cor)

    # Mostra o meme
    st.image(img, caption="Meme Gerado!", use_column_width=True)

    # Baixar
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    st.download_button("Baixar Meme", data=img_bytes.getvalue(), file_name="meme.png", mime="image/png")

