# 🏦 Plataforma de Experimentação Adaptativa com Multi-Armed Bandits

## 📋 Resumo Executivo

Este projeto apresenta o desenvolvimento de uma plataforma de recomendação adaptativa baseada no algoritmo **Thompson Sampling (Multi-Armed Bandit)** para seleção dinâmica do canal de comunicação mais adequado em campanhas de marketing bancário.

Como base experimental foi utilizado o **Bank Marketing Dataset**, disponibilizado no Kaggle e originalmente proveniente do UCI Machine Learning Repository. O conjunto de dados contém informações de campanhas de marketing realizadas por uma instituição financeira portuguesa, incluindo características dos clientes e o resultado das campanhas.

O objetivo do projeto é demonstrar como algoritmos de **Online Learning** podem aprender continuamente a selecionar a melhor ação utilizando apenas o histórico de recompensas observadas, reduzindo a necessidade de regras fixas de decisão.

Durante o desenvolvimento foram contempladas todas as etapas normalmente presentes em um projeto de **Machine Learning Engineering**, incluindo:

- 📊 Análise Exploratória dos Dados (EDA);
- 🧹 Preparação e limpeza da base;
- ⚠️ Tratamento de Data Leakage;
- 📈 Implementação de uma política de referência (Baseline);
- 🤖 Implementação do algoritmo Thompson Sampling;
- 📉 Avaliação utilizando Replay Method;
- 🎯 Construção de um Golden Set para validação qualitativa;
- 🌐 Desenvolvimento de uma API REST utilizando FastAPI;
- ☁️ Proposta de arquitetura em Microsoft Azure;
- 📈 Governança e rastreabilidade dos experimentos utilizando MLflow.

Ao final dos experimentos, a política adaptativa baseada em Thompson Sampling apresentou desempenho superior à política de referência, obtendo um **uplift de aproximadamente 29,28%** na taxa média de conversão.

---

# 📊 1. Base Factual e Dicionário de Dados

## Dataset utilizado

**Bank Marketing Dataset (Kaggle)**

https://www.kaggle.com/datasets/henriqueyamahata/bank-marketing

O conjunto de dados contém informações referentes a campanhas de marketing realizadas por telefone, cujo objetivo era oferecer um produto financeiro (depósito a prazo).

Cada registro representa um contato realizado com um cliente e contém informações cadastrais, financeiras e históricas utilizadas durante a campanha.

Ao todo são **41.188 registros**, contendo atributos relacionados ao perfil do cliente e ao resultado da campanha.

## Principais atributos

| Campo | Descrição |
|--------|-----------|
| age | Idade do cliente |
| job | Profissão |
| marital | Estado civil |
| education | Escolaridade |
| default | Possui inadimplência |
| housing | Possui financiamento imobiliário |
| loan | Possui empréstimo pessoal |
| contact | Canal utilizado na campanha |
| poutcome | Resultado da campanha anterior |
| y | Conversão da campanha |

---

# 📈 2. Análise Exploratória dos Dados (EDA)

## Variável alvo

O dataset original possui a variável **y**, indicando se o cliente aceitou ou não a oferta de depósito a prazo.

Para utilização em um algoritmo Multi-Armed Bandit, essa variável foi convertida para uma recompensa binária denominada **reward**, onde:

| Valor | Significado |
|--------|-------------|
| 1 | Conversão |
| 0 | Não conversão |

A distribuição observada foi:

| Resultado | Quantidade |
|-----------|-----------:|
| Conversões | 4.640 |
| Não conversões | 36.548 |

Taxa histórica de conversão:

**11,2654%**

![Distribuição Histórica](image/historica.png)

---

## Principais observações

Durante a análise exploratória foram identificadas as seguintes características:

- maior concentração de clientes entre 30 e 45 anos;
- distribuição assimétrica das variáveis financeiras;
- inexistência de valores nulos (NaN);
- manutenção dos valores "unknown", representando informações ausentes do cadastro original;
- preservação dos outliers para manter o comportamento real da base.

Essas características tornam o conjunto de dados adequado para avaliação de algoritmos de aprendizado online.

---

## Tratamento de Data Leakage

Antes da etapa de treinamento foi removida a variável:

```
duration
```

Essa variável representa a duração da ligação telefônica.

Entretanto, ela somente é conhecida **após** a realização do contato com o cliente.

Sua utilização durante o treinamento produziria um modelo impossível de ser utilizado em ambiente real, caracterizando **Data Leakage**.

Por esse motivo, a variável foi removida antes de qualquer treinamento.

---

# 🤖 3. Modelo de Recomendação

O problema foi modelado como um **Multi-Armed Bandit** de dois braços.

Cada braço representa um canal de comunicação disponível para contato com o cliente.

| Braço | Canal |
|------:|--------|
| 0 | Celular |
| 1 | Telefone Fixo |

O algoritmo utilizado foi o **Thompson Sampling**, um método Bayesiano que equilibra continuamente dois objetivos:

- **Explotação**: selecionar o canal com maior probabilidade estimada de sucesso;
- **Exploração**: testar ocasionalmente alternativas para reduzir a incerteza estatística e continuar aprendendo.

Dessa forma, o algoritmo adapta sua política conforme novas recompensas são observadas.

---

# 📉 4. Política de Referência (Baseline)

Antes da implementação do Thompson Sampling foi construída uma política de referência (Baseline).

Essa política realiza uma escolha **aleatória uniforme** entre os dois canais disponíveis.

```python
chosen_arm = random.choice([0, 1])
```

Essa estratégia representa um cenário onde não existe qualquer conhecimento prévio sobre qual canal possui melhor desempenho.

Ela serve como referência para medir o ganho obtido pelo algoritmo adaptativo.

---

# 🔄 5. Replay Method

Como o conjunto de dados utilizado é histórico, não é possível executar experimentos online reais.

Por esse motivo foi utilizada a técnica conhecida como **Replay Method**.

Essa metodologia percorre os registros históricos simulando como o algoritmo teria tomado decisões caso estivesse operando em produção.

A recompensa somente é considerada quando o canal escolhido pelo algoritmo coincide com o canal realmente utilizado no registro histórico.

Essa estratégia permite avaliar algoritmos de aprendizado online utilizando dados observacionais sem necessidade de novas campanhas.

---

# 📊 6. Resultados Experimentais

## Baseline

| Métrica | Valor |
|---------|------:|
| Eventos avaliados | **20.632** |
| Recomendações Celular | **13.153** |
| Recomendações Telefone | **7.479** |
| Taxa média de conversão | **11,2737%** |

---

## Thompson Sampling

| Métrica | Valor |
|---------|------:|
| Eventos avaliados | **26.464** |
| Recomendações Celular | **26.142** |
| Recomendações Telefone | **322** |
| Taxa média de conversão | **14,5745%** |
| Uplift | **29,28%** |

---

## Parâmetros Bayesianos Aprendidos

Após o treinamento, o algoritmo convergiu para os seguintes parâmetros:

| Canal | α | β |
|-------|---:|---:|
| Celular | **3854** | **22290** |
| Telefone Fixo | **5** | **319** |

Esses parâmetros representam o conhecimento acumulado pelo algoritmo após observar as recompensas disponíveis no conjunto de dados.

São exatamente esses valores que alimentam a API de recomendação desenvolvida neste projeto.

---

## Resultado

Comparando os dois modelos, observa-se que o Thompson Sampling foi capaz de aumentar a taxa média de conversão em aproximadamente **29,28%**, concentrando progressivamente suas recomendações no canal com maior retorno esperado.

Esse comportamento demonstra a capacidade do algoritmo de aprender continuamente a partir das recompensas observadas, reduzindo sua incerteza estatística ao longo do processo de decisão.

![Distribuições Finais](image/final.png)

