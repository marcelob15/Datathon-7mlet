# src/mlflow_tracking.py

import mlflow

# ==============================================================================
# Configuração do MLflow
# ==============================================================================

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Datathon_7MLET_Ofertas")

# ==============================================================================
# Registro do experimento final
# ==============================================================================

with mlflow.start_run(run_name="Thompson_Sampling_Final_Run"):

    # --------------------------------------------------------------------------
    # Metadados do Projeto (Tags)
    # --------------------------------------------------------------------------
    mlflow.set_tags({
        "algoritmo": "Thompson Sampling (Multi-Armed Bandit)",
        "dataset": "Bank Marketing",
        "politica_baseline": "Escolha aleatória uniforme (50/50)",
        "metodo_avaliacao": "Replay Method"
    })

    # --------------------------------------------------------------------------
    # Priors / Hiperparâmetros
    # --------------------------------------------------------------------------
    mlflow.log_params({
        "alpha_celular": 3854,
        "beta_celular": 22290,
        "alpha_telefone": 5,
        "beta_telefone": 319,
        "braco_0": "Celular",
        "braco_1": "Telefone Fixo"
    })

    # --------------------------------------------------------------------------
    # Métricas finais
    # --------------------------------------------------------------------------
    mlflow.log_metrics({
        "eventos_baseline": 20632,
        "eventos_thompson": 26464,
        "taxa_conversao_baseline": 0.112737,
        "taxa_conversao_thompson": 0.145745,
        "uplift_percentual": 29.28
    })

    print("✅ Experimento registrado com sucesso no MLflow.")