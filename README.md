# 📊 IBGE Analytics Pipeline - Engenharia de Dados
Equipe: Iann Luca Rocha Lino, Gustavo Peixoto De Oliveira Dias

Este projeto é um pipeline analítico automatizado focado na extração, higienização e visualização de dados socioeconômicos do IBGE, desenvolvido como requisito de avaliação em Engenharia de Software.

## 🏗️ Arquitetura do Projeto (Separação de Conceitos)
Diferente de aplicações web tradicionais, este projeto adota uma arquitetura de **Automação e Relatórios Executivos (ETL)**:

1. **Camada de Persistência (Back-end):** Utilização de `SQLite` para armazenamento embarcado e processamento das regras de negócio através de agregações (`GROUP BY`) e condicionais lógicas (`CASE WHEN`) em SQL puro.
2. **Camada de Tratamento de Dados (Data Cleansing):** Uso do `Pandas` e Expressões Regulares (`Regex`) no Python para higienizar falhas de codificação (*Mojibake* / ISO-8859-1 para UTF-8) nos dados originais do Governo em tempo de execução.
3. **Camada de Apresentação:** Utilização do `Matplotlib` para consumir os dados já estruturados do banco e exportar painéis gráficos estáticos em alta resolução, ideais para relatórios governamentais.

## 🚀 Como Executar

1. Clone o repositório.
2. Certifique-se de ter as bibliotecas de análise de dados instaladas:
   ```bash
   pip install pandas matplotlib
