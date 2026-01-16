# 🤖 AI Influencer Hub - Gerador de Conteúdo Mobile

![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Esta plataforma permite criar e gerenciar uma Influencer de IA com consistência de rosto (fisionomia) e clonagem de voz, tudo processado em nuvem e controlado via dispositivo móvel.

## 🏗️ Estrutura do Projeto

- **Frontend:** `index.html` (Dashboard interativo em HTML5/Tailwind)
- **Backend:** `api/main.py` (Serverless Functions em Python na Vercel)
- **Configuração:** `vercel.json` (Orquestração de rotas e build)
- **Dependências:** `requirements.txt` (Bibliotecas de IA necessárias)

## 🚀 Como Colocar no Ar

### 1. Deploy na Vercel
1. Conecte sua conta do GitHub à [Vercel](https://vercel.com).
2. Importe este repositório (`Gerado-02-`).
3. A Vercel detectará automaticamente as configurações do `vercel.json` e instalará o Python.

### 2. Integração com WordPress
Para exibir no seu site WordPress, use o bloco de **HTML Personalizado** com o seguinte iFrame:
```html
<iframe src="[https://seu-projeto.vercel.app](https://seu-projeto.vercel.app)" width="100%" height="700px" style="border:none;"></iframe>
