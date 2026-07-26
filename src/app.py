# src/app.py

import numpy as np
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

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
    client_id: int = Field(..., example=100)
    age: int = Field(..., example=42)
    job: str = Field(..., example="technician")
    marital: str = Field(..., example="married")
    education: str = Field(..., example="university.degree")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "client_id": 100,
                    "age": 42,
                    "job": "technician",
                    "marital": "married",
                    "education": "university.degree"
                }
            ]
        }
    }


# ==============================================================================
# Endpoints
# ==============================================================================

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Plataforma de Experimentação Adaptativa</title>
        <style>
            body {
                font-family: system-ui, -apple-system, sans-serif;
                background-color: #f4f6f8;
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: white;
                padding: 2.5rem;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
                text-align: center;
                max-width: 480px;
            }
            h1 {
                font-size: 1.5rem;
                margin-bottom: 0.5rem;
                color: #1a202c;
            }
            p {
                color: #4a5568;
                font-size: 0.95rem;
                margin-bottom: 1.5rem;
                line-height: 1.5;
            }
            a.btn {
                display: inline-block;
                background-color: #2563eb;
                color: white;
                padding: 0.75rem 1.5rem;
                border-radius: 6px;
                text-decoration: none;
                font-weight: 600;
                transition: background-color 0.2s ease;
            }
            a.btn:hover {
                background-color: #1d4ed8;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Plataforma de Experimentação Adaptativa</h1>
            <p>API para recomendação adaptativa do canal de contato utilizando Thompson Sampling (Datathon 7MLET).</p>
            <a href="/docs" class="btn">Acessar Documentação (Swagger)</a>
        </div>
    </body>
    </html>
    """
    return html_content


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