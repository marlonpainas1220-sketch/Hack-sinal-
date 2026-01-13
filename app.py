import streamlit as st
from openai import OpenAI

# --- CONFIGURAÇÃO DA CHAVE ---
# Substitua pela sua chave completa sk-proj-...
MINHA_CHAVE_API = "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"

client = OpenAI(api_key=MINHA_CHAVE_API)

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="AI Influencer Studio", page_icon="💃", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f0f13; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #6200ee; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: O MOLDE DA MODELO ---
with st.sidebar:
    st.header("🧬 DNA da Modelo (Referência)")
    st.write("Defina as características fixas para manter a consistência.")
    
    upload_ref = st.file_uploader("Upload da Foto Base (Opcional)", type=['jpg', 'png'])
    cabelo = st.text_input("Cabelo", "Longo, ondulado, cor rosa pastel")
    rosto = st.text_input("Rosto/Etnia", "Traços latinos, olhos amendoados verdes")
    corpo = st.text_input("Bio/Estilo", "Alta, estilo streetwear de luxo, tatuagem pequena no pescoço")
    
    st.divider()
    st.subheader("🎵 Estilo da Voz/Texto")
    tom = st.selectbox("Tom de voz", ["Sarcástica", "Doce/Meiga", "Empoderada", "Misteriosa"])

# --- ÁREA PRINCIPAL ---
st.title("🎤 AI Content Factory: Cantora & Influencer")
st.write("Crie fotos, legendas e roteiros em segundos mantendo a identidade da sua modelo.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Briefing do Post")
    tema = st.text_area("O que ela está fazendo agora?", 
                        placeholder="Ex: Saindo de uma limousine em Dubai chegando num show...",
                        height=150)
    
    tipo_conteudo = st.multiselect("Gerar para quais canais?", 
                                   ["Feed Instagram", "Stories (Foto)", "Roteiro de Reels"],
                                   default=["Feed Instagram"])

    gerar = st.button("🚀 GERAR CONTEÚDO COMPLETO")

with col2:
    st.subheader("🖼️ Visual & Copy")
    if gerar:
        if not tema:
            st.error("Por favor, descreva o que ela está fazendo!")
        else:
            with st.spinner('A IA está processando a produção...'):
                # 1. CONSTRUÇÃO DO PROMPT VISUAL (Injetando o DNA)
                prompt_visual = f"Photorealistic high-end fashion photography of a woman with {cabelo}, {rosto}, {corpo}. She is {tema}. Consistent facial features, 8k resolution, cinematic lighting, magazine style."

                try:
                    # Geração da Imagem
                    img_response = client.images.generate(
                        model="dall-e-3",
                        prompt=prompt_visual,
                        n=1,
                        size="1024x1024"
                    )
                    image_url = img_response.data[0].url
                    st.image(image_url, use_column_width=True)

                    # 2. GERAÇÃO DE TEXTO
                    texto_prompt = f"""
                    Você é o Social Media da influencer {tom}. 
                    Ela tem esse DNA: {cabelo}, {rosto}, {corpo}.
                    Crie conteúdo para: {tipo_conteudo}.
                    Ação do momento: {tema}.
                    Retorne uma legenda engajadora com emojis e um roteiro curto caso tenha Reels.
                    """
                    
                    text_response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{"role": "user", "content": texto_prompt}]
                    )
                    
                    st.success("Conteúdo Gerado!")
                    st.markdown(text_response.choices[0].message.content)
                    
                except Exception as e:
                    st.error(f"Erro na API: {e}")
    else:
        st.info("Aguardando seu comando para iniciar a produção.")

# --- FOOTER ---
st.divider()
st.caption("AI Content Factory - Powered by OpenAI & Streamlit")
