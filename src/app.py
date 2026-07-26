# src/app.py

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# ==============================================================================
# API - Plataforma de Experimentação Adaptativa
# ==============================================================================

app = FastAPI(
    title="Plataforma de Experimentação Adaptativa - MLET Bancos",
    description="API para recomendação adaptativa do canal de contato utilizando Thompson Sampling."
)

# ==============================================================================
# Priors aprendidos durante o treinamento
# ==============================================================================

ALPHA_CELULAR = 3854
BETA_CELULAR = 22290

ALPHA_FIXO = 5
BETA_FIXO = 319


# ==============================================================================
# Modelo de Entrada
# ==============================================================================

class ClienteInput(BaseModel):
    client_id: int
    age: int
    job: str
    marital: str
    education: str


# ==============================================================================
# Endpoints
# ==============================================================================

@app.get("/")
def home():
    return {
        "status": "Online",
        "projeto": "Datathon 7MLET - Thompson Sampling"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/recomendar")
def recomendar_canal(cliente: ClienteInput):

    # Amostragem Thompson Sampling
    theta_celular = np.random.beta(ALPHA_CELULAR, BETA_CELULAR)
    theta_fixo = np.random.beta(ALPHA_FIXO, BETA_FIXO)

    # Escolha do braço com maior recompensa amostrada
    if theta_celular >= theta_fixo:
        canal = "Celular"
        score = theta_celular
    else:
        canal = "Telefone Fixo"
        score = theta_fixo

    return {
        "client_id": cliente.client_id,
        "canal_recomendado": canal,
        "score_amostrado": round(score, 4),
        "modelo": "Thompson Sampling",
        "priors": {
            "celular": {
                "alpha": ALPHA_CELULAR,
                "beta": BETA_CELULAR
            },
            "telefone": {
                "alpha": ALPHA_FIXO,
                "beta": BETA_FIXO
            }
        },
        "observacao": (
            "A recomendação utiliza os parâmetros aprendidos durante o treinamento "
            "e seleciona o canal com maior recompensa amostrada."
        )
    }