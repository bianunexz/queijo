import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Título e instruções
st.title("🖼️ Gerador de Memes Simples")
st.write("Crie memes com imagem própria ou selecione uma das disponíveis!")

# Opções de imagens locais pré-carregadas
imagens_locais = {
    "Criança": "a7e444d5d84997933ae1b1a460b094d8.jpg",
    "Cachorro BONK": "download.jpg",
    "Gato gritando": "download.jpg"
}

# Opção de upload ou uso de imagem existente
opcao = st.radio("Escolha uma imagem ou envie a sua:", ("Usar imagem existente", "Enviar minha imagem"))

# Se for usar uma imagem existente
if opcao == "Usar imagem existente":
    imagem_escolhida = st.selectbox("Escolha a imagem:", list(imagens_locais.keys()))
    caminho_imagem = f"/mnt/data/{imagens_locais[imagem_escolhida]}"
else:
    imagem_upload = st.file_uploader("Envie uma imagem (JPEG ou PNG)", type=["jpg", "jpeg", "png"])
    if imagem_upload is not None:
        caminho_imagem = imagem_upload

# Textos do meme
texto_cima = st.text_input("Texto de cima:", "QUANDO O PROFESSOR")
texto_baixo = st.text_input("Texto de baixo:", "PEDE UM TRABALHO")
cor = st.color_picker("Cor do texto:", "#FFFFFF")

# Botão para criar meme
if st.button("Criar Meme"):
    if opcao == "Enviar minha imagem" and imagem_upload is None:
        st.warning("Por favor, envie uma imagem.")
    else:
        try:
            # Carrega a imagem
            img = Image.open(caminho_imagem).convert("RGB")
            draw = ImageDraw.Draw(img)

            # Usa fonte padrão
            fonte = ImageFont.load_default()

            # Desenha os textos
            draw.text((10, 10), texto_cima, fill=cor, font=fonte)
            draw.text((10, img.height - 30), texto_baixo, fill=cor, font=fonte)

            # Mostra o resultado
            st.image(img, caption="Seu Meme Pronto!")

            # Botão para baixar
            img_bytes = BytesIO()
            img.save(img_bytes, format='PNG')
            st.download_button(
                label="Baixar Meme",
                data=img_bytes.getvalue(),
                file_name="meu_meme.png",
                mime="image/png"
            )
        except Exception as e:
            st.error(f"Erro ao criar o meme: {e}")

