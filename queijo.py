import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Configuração básica
st.title(" Gerador de Memes Simples")
st.write("Crie memes rapidamente sem precisar de APIs!")

# Imagens online de exemplo (sem precisar baixar)
imagens = {
    "Gato": "https://raw.githubusercontent.com/username/repo/main/cat.jpg",
    "Criança": "https://raw.githubusercontent.com/username/repo/main/kid.jpg",
    "Cachorro": "https://raw.githubusercontent.com/username/repo/main/dog.jpg"
}

# Seleciona imagem
opcao = st.selectbox("Escolha a imagem:", list(imagens.keys()))

# Textos do meme
texto_cima = st.text_input("Texto de cima:", "QUANDO O PROFESSOR")
texto_baixo = st.text_input("Texto de baixo:", "PEDE UM TRABALHO")

# Cor do texto
cor = st.color_picker("Cor do texto:", "#FFFFFF")

# Botão para criar
if st.button("Criar Meme"):
    try:
        # Pega a imagem da internet
        response = requests.get(imagens[opcao])
        img = Image.open(BytesIO(response.content))
        
        # Prepara para editar
        draw = ImageDraw.Draw(img)
        
        # Usa fonte básica
        fonte = ImageFont.load_default()
        
        # Adiciona textos
        draw.text((10, 10), texto_cima, fill=cor, font=fonte)
        draw.text((10, img.height-30), texto_baixo, fill=cor, font=fonte)
        
        # Mostra o resultado
        st.image(img, caption="Seu Meme Pronto!")
        
        # Prepara para download
        img_bytes = BytesIO()
        img.save(img_bytes, format='PNG')
        
        st.download_button(
            label="Baixar Meme",
            data=img_bytes.getvalue(),
            file_name="meu_meme.png",
            mime="image/png"
        )
    except:
        st.error("Algo deu errado. Tente outra imagem ou texto.")
