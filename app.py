import streamlit as st
from openai import OpenAI

# Configuração da Interface
st.set_page_config(page_title="Luna Star AI - Manager", page_icon="🎤")
st.title("🎤 Dashboard da Cantora IA")
st.markdown("Gerencie os posts e o estilo da sua influenciadora.")

# Conexão com sua Chave (Usando a que você forneceu)
client = OpenAI(api_key="sk-proj-WRo...RJgA") # Chave encurtada por segurança

# Painel Lateral - Personalidade da Cantora
with st.sidebar:
    st.header("Personalidade")
    nome = st.text_input("Nome da IA", "Luna Star")
    estilo = st.selectbox("Mood de Hoje", ["Animada", "Melancólica", "Empoderada", "Misteriosa"])

# Área Central
tema = st.text_area("O que ela está fazendo hoje?", "Gravando um videoclipe no topo de um prédio em SP")

if st.button("Gerar Conteúdo Completo"):
    with st.spinner('A IA está criando o mundo da Luna...'):
        
        prompt_base = f"""
        Você é um estrategista de conteúdo para a {nome}, uma influenciadora e cantora de IA.
        O mood de hoje é {estilo}.
        Tarefa: Crie um post para Instagram baseado em: {tema}.
        
        Retorne no seguinte formato:
        ---
        📸 **PROMPT PARA IMAGEM (Inglês):** (Descreva o visual dela com realismo, roupas e cenário)
        ---
        ✍️ **LEGENDA (Português):** (Use gírias e a voz da personagem)
        ---
        💡 **SUGESTÃO DE STORY:** (O que ela deve falar ou mostrar)
        """

        response = client.chat.completions.create(
            model="gpt-4o", # Usando o modelo mais recente disponível na sua chave
            messages=[{"role": "user", "content": prompt_base}]
        )
        
        resultado = response.choices[0].message.content
        st.markdown(resultado)

st.divider()
st.info("Próximo passo: Conectar a API de imagem para gerar a foto automaticamente aqui.")
