# src/app.py
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# Inicializa o FastAPI
app = FastAPI(
    title="Plataforma de Experimentação Adaptativa - MLET Bancos",
    description="API para recomendação adaptativa de canais digitais usando Thompson Sampling."
)

# Parâmetros bayesianos extraídos e consolidados no seu experimento real (Sua Governança)
ALPHA_CELULAR = 3847
BETA_CELULAR = 22232
ALPHA_FIXO = 13
BETA_FIXO = 404

# Definição do formato de entrada de dados do Cliente (Schema)
class ClienteInput(BaseModel):
    client_id: int
    age: int
    job: str
    marital: str
    education: str

@app.get("/")
def home():
    return {"status": "Online", "projeto": "Datathon 7MLET - Canal Adaptativo"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/recomendar")
def recomendar_canal(cliente: ClienteInput):
    # Thompson Sampling: O modelo amostra as probabilidades baseado no conhecimento acumulado
    theta_celular = np.random.beta(ALPHA_CELULAR, BETA_CELULAR)
    theta_fixo = np.random.beta(ALPHA_FIXO, BETA_FIXO)
    
    # Tomada de decisão em tempo real (Explotação Inteligente)
    if theta_celular > theta_fixo:
        canal_escolhido = "Celular"
        probabilidade_amostrada = theta_celular
    else:
        canal_escolhido = "Telefone Fixo"
        probabilidade_amostrada = theta_fixo
        
    return {
        "client_id": cliente.client_id,
        "canal_recomendado": canal_escolhido,
        "score_amostrado": round(probabilidade_amostrada, 4),
        "justificativa": f"Canal selecionado via Thompson Sampling. Parâmetros atuais do modelo: Celular(α={ALPHA_CELULAR}), Fixo(α={ALPHA_FIXO})."
    }