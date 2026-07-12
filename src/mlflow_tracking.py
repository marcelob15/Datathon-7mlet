# src/mlflow_tracking.py
import mlflow

# Configura o MLflow para rodar e salvar os dados localmente usando SQLite
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Datathon_7MLET_Ofertas")

with mlflow.start_run(run_name="Thompson_Sampling_Final_Run"):
    
    # 1. Registro de Parâmetros de Produção (Seus Priors Finais Reais)
    mlflow.log_param("algoritmo", "Thompson Sampling (Multi-Armed Bandit)")
    mlflow.log_param("alpha_celular", 3847)
    mlflow.log_param("beta_celular", 22232)
    mlflow.log_param("alpha_telefone_fixo", 13)
    mlflow.log_param("beta_telefone_fixo", 404)
    mlflow.log_param("braço_0", "Celular")
    mlflow.log_param("braço_1", "Telefone Fixo")
    
    # 2. Registro de Métricas Consolidadas Reais do Ambiente
    mlflow.log_metric("taxa_conversao_modelo_adaptativo", 0.145629)
    mlflow.log_metric("taxa_conversao_baseline_estatico", 0.111982)
    mlflow.log_metric("uplift_percentual", 30.05)
    
    print("✅ Sucesso: Experimento e governança registrados localmente na base do MLflow com os dados reais!")