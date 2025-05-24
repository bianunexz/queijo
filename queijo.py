import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

# Configuração da página
st.set_page_config(page_title="Gerador de Memes", page_icon="😂")

# Título
st.title("📸 Gerador de Memes para Comunicação Digital")
st.write("Crie memes rapidamente para suas campanhas!")

# Sidebar com instruções
with st.sidebar:
    st.header("Como usar:")
    st.write("1. Escolha uma imagem base")
    st.write("2. Digite o texto do meme")
    st.write("3. Ajuste a posição e cor")
    st.write("4. Baixe seu meme pronto!")
    st.markdown("---")
    st.caption("Feito com ❤️ para impressionar o professor")

# Imagens de exemplo (embutidas no código)
imagens = {
    "Gato Surpreso": "cat.jpg",
    "Criança Feliz": "kid.jpg",
    "Dog Filosofo": "dog.jpg"
}

# Seleção de imagem
opcao = st.selectbox("Escolha uma imagem base:", list(imagens.keys()))

# Texto do meme
texto_superior = st.text_input("Texto superior:", "QUANDO O PROFESSOR")
texto_inferior = st.text_input("Texto inferior:", "PEDE UM PROJETO INCRÍVEL")

# Personalização
col1, col2, col3 = st.columns(3)
cor = col1.color_picker("Cor do texto:", "#FFFFFF")
tamanho = col2.slider("Tamanho do texto:", 10, 100, 40)
posicao_sup = col3.slider("Posição texto superior:", 0, 100, 10)
posicao_inf = col3.slider("Posição texto inferior:", 0, 100, 90)

# Gerar meme
if st.button("Criar Meme"):
    # Usando uma imagem de exemplo (substitua por suas próprias imagens)
    img = Image.new('RGB', (600, 500), color='black')
    d = ImageDraw.Draw(img)
    
    try:
        # Tentando usar fonte local ou padrão
        try:
            fonte = ImageFont.truetype("impact.ttf", tamanho)
        except:
            fonte = ImageFont.load_default()
        
        # Adicionando textos
        d.text((50, posicao_sup), texto_superior, fill=cor, font=fonte)
        d.text((50, img.height-posicao_inf), texto_inferior, fill=cor, font=fonte)
        
        # Mostrar resultado
        st.image(img, caption="Seu Meme Pronto!")
        
        # Botão para download
        img.save("meme_gerado.png")
        with open("meme_gerado.png", "rb") as file:
            btn = st.download_button(
                label="Baixar Meme",
                data=file,
                file_name="meu_meme.png",
                mime="image/png"
            )
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")

# Rodapé
st.markdown("---")
st.caption("Projeto simples mas eficaz para demonstrar conceitos de Comunicação Digital")
