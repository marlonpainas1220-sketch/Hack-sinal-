import streamlit as st
import google.generativeai as genai

# Configuração de Segurança para o Streamlit
# Ele vai tentar pegar a chave das 'Secrets'. Se não achar (local), usa a que você colar.
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    api_key = "COLE_SUA_CHAVE_AQUI_PARA_TESTE_LOCAL"

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="IA Influencer Manager", page_icon="🎤")

st.title("🎤 Studio de Automação: Cantora IA")

# Painel Lateral
st.sidebar.title("Configurações")
nome_ia = st.sidebar.text_input("Nome da Influenciadora", "Minha Cantora")
vibe = st.sidebar.selectbox("Estilo", ["Pop Star", "Indie Virtual", "Trap Futurista"])

# Funções de Geração
def gerar_conteudo(prompt_texto):
    response = model.generate_content(prompt_texto)
    return response.text

# Interface Principal
aba1, aba2 = st.tabs(["🚀 Gerar Conteúdo", "📅 Calendário"])

with aba1:
    tipo = st.selectbox("O que criar?", ["POV para Reels", "Ideia de Meme", "Story de Lançamento"])
    if st.button("Criar Agora"):
        with st.spinner("O Gemini está criando..."):
            roteiro = gerar_conteudo(f"Crie um {tipo} viral para a influenciadora {nome_ia} que tem o estilo {vibe}.")
            st.subheader("Conteúdo Gerado:")
            st.write(roteiro)

with aba2:
    st.subheader("Cronograma Automático")
    st.write("Segunda: Foto de Look do Dia")
    st.write("Terça: Vídeo de ensaio (POV)")
    st.write("Quarta: Meme sobre ser uma IA")
