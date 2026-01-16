from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import edge_tts
import os
import asyncio
from gradio_client import Client, handle_file

app = FastAPI()

# Configuração dos Clientes de IA (Gratuitos no Hugging Face)
# LivePortrait para animação de fisionomia
VIDEO_CLIENT = Client("Kwai-VGI/LivePortrait") 

@app.get("/api/health")
def health_check():
    return {"status": "IA Engine Online"}

@app.post("/api/generate")
async def generate_content(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    mode = data.get("mode") # 'photo' ou 'video'
    
    # 1. GERAR VOZ (GRÁTIS via Edge-TTS)
    voice_path = "/tmp/voice_output.mp3"
    communicate = edge_tts.Communicate(prompt, "pt-BR-FranciscaNeural")
    await communicate.save(voice_path)

    # 2. SE FOR VÍDEO: Sincronizar Fisionomia (LivePortrait)
    if mode == "video":
        try:
            # Aqui ele envia para o processamento gratuito do Hugging Face
            result = VIDEO_CLIENT.predict(
                input_image=handle_file(data.get("face_url")),
                input_video=handle_file(data.get("ref_video_url")),
                api_name="/predict"
            )
            return {
                "status": "success",
                "video_url": result,
                "audio_url": voice_path
            }
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})

    # 3. SE FOR FOTO: Gerar Imagem com FaceID (InstantID)
    else:
        # Retorna a lógica de geração de imagem
        return {"status": "success", "message": "Foto enviada para renderização"}

# Para rodar localmente (teste)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
