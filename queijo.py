import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# Título do app
st.title("🖼️ Gerador de Memes Simples")

# Opções de imagens salvas (as que você já enviou)
imagens_salvas = {
    "Criança com tédio": "/mnt/data/a7e444d5d84997933ae1b1a460b094d8.jpg",
    "Cachorro Bonk": "/mnt/data/download.jpg",
    "Gato gritando": "/mnt/data/download.jpg"  # É o mesmo nome do segundo, então sobrescreveu
}

# Opção de usar imagem salva ou fazer upload
opcao = st.radio("Escolha uma imagem:", ["Usar imagem salva", "Enviar minha imagem"])

# Se for imagem salva
if opcao == "Usar imagem salva":
    escolha = st.selectbox("Escolha:", list(imagens_salvas.keys()))
    caminho_imagem = imagens_salvas[escolha]
    imagem = Image.open(caminho_imagem)

# Se for upload
else:
    uploaded_file = st.file_uploader("Envie sua imagem (jpg ou png)", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        imagem = Image.open(uploaded_file)
    else:
        imagem = None

# Campos de texto do meme
texto_cima = st.text_input("Texto de cima", "QUANDO O PROFESSOR")
texto_baixo = st.text_input("Texto de baixo", "PEDE UM TRABALHO")
cor = st.color_picker("Cor do texto", "#FFFFFF")

# Criar Meme
if st.button("Criar Meme"):
    if imagem:
        # Copia a imagem original
        img = imagem.copy()
        draw = ImageDraw.Draw(img)

        # Fonte padrão (pode melhorar com .ttf depois)
        fonte = ImageFont.load_default()

        # Posição dos textos
        draw.text((10, 10), texto_cima.upper(), font=fonte, fill=cor)
        draw.text((10, img.height - 20), texto_baixo.upper(), font=fonte, fill=cor)

        # Exibe imagem
        st.image(img, caption="Seu meme pronto!", use_column_width=True)

        # Botão de download
        img_bytes = BytesIO()
        img.save(img_bytes, format="PNG")
        st.download_button(
            label="Baixar Meme",
            data=img_bytes.getvalue(),
            file_name="meu_meme.png",
            mime="image/png"
        )
    else:
        st.warning("Por favor, envie ou selecione uma imagem.")


