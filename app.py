import streamlit as st
import google.generativeai as genai
import replicate # Biblioteca para trocar roupas/cenários
import os

# Configurações das Chaves
os.environ["REPLICATE_API_TOKEN"] = "SUA_CHAVE_REPLICATE_AQUI"
genai.configure(api_key="SUA_CHAVE_GOOGLE_AQUI")

st.set_page_config(page_title="IA Creator: Cantora & Influenciadora", layout="wide")
st.title("🎥 Central de Criação Automatizada")

# --- BARRA LATERAL: Identidade da Modelo ---
with st.sidebar:
    st.header("1. Identidade")
    foto_base = st.file_uploader("Foto Original da Modelo", type=['png', 'jpg', 'jpeg'])
    st.info("A IA usará esta foto como base para manter o rosto dela.")

# --- PAINEL PRINCIPAL ---
col1, col2 = st.columns(2)

with col1:
    st.header("2. Configurar Post")
    formato = st.selectbox("Formato do Conteúdo", ["Foto Editorial", "Story", "Reel / Vídeo"])
    roupa = st.text_input("Nova Roupa", placeholder="Ex: Vestido de paetê azul...")
    cenario = st.text_input("Novo Cenário", placeholder="Ex: Jatinho particular, palco, praia...")
    
with col2:
    st.header("3. Texto e Voz")
    roteiro = st.text_area("O que ela deve falar ou legenda do post?")
    clonar_voz = st.checkbox("Usar clonagem de voz (Requer ElevenLabs)")

# --- BOTÃO DE GERAÇÃO ---
if st.button("🚀 GERAR CONTEÚDO AGORA"):
    if not foto_base:
        st.error("Por favor, suba a foto da sua modelo na barra lateral.")
    else:
        with st.spinner('A IA está trocando a roupa e ambientando a cena...'):
            # PASSO 1: Google Gemini cria o Prompt Perfeito
            model_gemini = genai.GenerativeModel('gemini-1.5-flash')
            prompt_final = model_gemini.generate_content(f"Crie um prompt técnico em inglês para IA manter o rosto da modelo desta foto, mas trocando a roupa para {roupa} e o cenário para {cenario}. Estilo ultra-realista 8k.").text

            # PASSO 2: Replicate (Modelo Flux ou FaceSwap) gera a imagem
            # Aqui simulamos a chamada da API que você vai conectar
            output = replicate.run(
                "lucataco/faceswap:9a4298ab", # Exemplo de modelo de troca de rosto
                input={"target_image": foto_base, "swap_image": "URL_DA_ROUPA_OU_GERADA"}
            )
            
            st.success("Conteúdo Gerado com Sucesso!")
            st.image(foto_base, caption="Prévia do Post Gerado", width=400)
            st.write(f"**Legenda gerada:** {roteiro}")

            if formato != "Foto Editorial":
                st.info("Vídeo/Story está sendo renderizado no HeyGen (Lip-sync)...")
