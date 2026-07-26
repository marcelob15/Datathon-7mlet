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
    # Informações do modelo
    # --------------------------------------------------------------------------

    mlflow.log_param("algoritmo", "Thompson Sampling (Multi-Armed Bandit)")
    mlflow.log_param("dataset", "Bank Marketing")
    mlflow.log_param("politica_baseline", "Escolha aleatória uniforme (50/50)")
    mlflow.log_param("metodo_avaliacao", "Replay Method")

    # --------------------------------------------------------------------------
    # Priors aprendidos
    # --------------------------------------------------------------------------

    mlflow.log_param("alpha_celular", 3854)
    mlflow.log_param("beta_celular", 22290)

    mlflow.log_param("alpha_telefone", 5)
    mlflow.log_param("beta_telefone", 319)

    mlflow.log_param("braco_0", "Celular")
    mlflow.log_param("braco_1", "Telefone Fixo")

    # --------------------------------------------------------------------------
    # Métricas finais
    # --------------------------------------------------------------------------

    mlflow.log_metric("eventos_baseline", 20632)
    mlflow.log_metric("eventos_thompson", 26464)

    mlflow.log_metric("taxa_conversao_baseline", 0.112737)
    mlflow.log_metric("taxa_conversao_thompson", 0.145745)

    mlflow.log_metric("uplift_percentual", 29.28)

    print("✅ Experimento registrado com sucesso no MLflow.")