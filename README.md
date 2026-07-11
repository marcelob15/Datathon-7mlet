
```markdown
# 🏦 Plataforma de Experimentação Adaptativa - Datathon 7MLET

Solução end-to-end de Machine Learning Engineering para otimização adaptativa de ofertas e canais de contato bancários, utilizando conceitos de Multi-Armed Bandit (Thompson Sampling).

## 📊 Link da Base de Dados Factuais
* **Referência:** [Kaggle Bank Marketing Dataset (Henrique Yamahata)](https://www.kaggle.com/datasets/henriqueyamahata/bank-marketing)

---

## 🛠️ Como Executar o Projeto Localmente

### 1. Configurar o Ambiente e Dependências
```bash
# Criar e ativar o ambiente virtual
python -m venv venv
./venv/Scripts/Activate.ps1  # No Windows (PowerShell)

# Instalar dependências requisitadas
pip install -r requirements.txt

```

### 2. Executar o Tracking de Governança (MLflow)

```bash
python src/mlflow_tracking.py
mlflow server --backend-store-uri sqlite:///mlflow.db --host 127.0.0.1 --port 5000

```

### 3. Subir a API de Recomendação em Tempo Real

```bash
uvicorn src.app:app --reload --host 127.0.0.1 --port 9000

```

Acesse a interface interativa em: `http://127.0.0.1:9000/docs`

---

## ☁️ Etapa 6 - Arquitetura-Alvo Sugerida em Nuvem (AWS)

Para levar esta plataforma adaptativa a um ambiente produtivo resiliente, escalável e de baixa latência na **AWS**, adotaríamos a seguinte topologia serverless e elástica:

1. **Camada de Serviço (Serviço/API):** A API desenvolvida em FastAPI seria empacotada em uma imagem Docker e hospedada no **AWS ECS (Elastic Container Service) com AWS Fargate**, eliminando a necessidade de gerenciar servidores. Um **Application Load Balancer (ALB)** distribuiria a carga entre as instâncias, garantindo alta disponibilidade.
2. **Armazenamento e Estado do Modelo (MAB Parameters):** Como o Thompson Sampling precisa atualizar seus *priors* (Alpha e Beta) continuamente a cada feedback, os estados dos braços seriam persistidos em um banco de dados NoSQL de ultra-baixa latência, o **Amazon DynamoDB**, garantindo respostas em milissegundos para a API.
3. **Maturidade MLOps (Governança e Pipeline):** O ciclo de vida e tracking, hoje local, seria centralizado utilizando o **AWS SageMaker Pipelines** em conjunto com uma instância gerenciada do **MLflow no AWS SageMaker**, permitindo o monitoramento de drift, auditoria de decisões e governança responsável com Human-in-the-loop.

```

---

## 📹 Etapa 8 - Apresentação Final (Demo Day)

O seu checklist técnico está 100% preenchido[cite: 1]! Para o vídeo final de **até 5 minutos**[cite: 1], siga este roteiro simples e focado, sem necessidade de slides complexos[cite: 1]:

1. **Problema de Negócio (1 min):** Explique que regras fixas e testes A/B longos desperdiçam tráfego bancário[cite: 1]. A abordagem adaptativa do Thompson Sampling resolve isso equilibrando exploração e explotação em tempo real[cite: 1].
2. **O Experimento (1.5 min):** Mostre rapidamente o gráfico das curvas Beta gerado no seu notebook[cite: 1]. Explique que o modelo aprendeu que o canal Celular performa drasticamente melhor que o Telefone Fixo, trazendo um **uplift de 28.24%**[cite: 1].
3. **Demonstração Prática (2 min):** Abra o Swagger da sua API (`[http://127.0.0.1:9000/docs](http://127.0.0.1:9000/docs)`), mande o comando `curl` (exatamente como você colou aqui) e mostre o JSON retornando a decisão em tempo real de forma inteligente[cite: 1].
4. **Encerramento (30 seg):** Cite rapidamente a arquitetura sugerida na AWS (FastAPI no ECS Fargate + DynamoDB) para mostrar a visão de engenharia de produção[cite: 1].

Parabéns pelo excelente trabalho no desenvolvimento de ponta a ponta do projeto! Se precisar de qualquer ajuste fino final na documentação, conte comigo.

```