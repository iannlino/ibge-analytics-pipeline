import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================================
# 0. INICIALIZAÇÃO E LIGAÇÃO À BASE DE DADOS
# =====================================================================
print("A ligar à base de dados e a iniciar a extração de dados...")
caminho_banco = r'projeto_ibge.sqlite'
conexao = sqlite3.connect(r'projeto_ibge.sqlite')


# =====================================================================
# DESAFIO 1: Densidade Demográfica (Top 10 Estados mais densos)
# =====================================================================
query_densidade = """
SELECT 
    uf, 
    (populacao_residente / area_territorial) AS densidade
FROM estatisticas_ibge
ORDER BY densidade DESC
LIMIT 10;
"""
df_densidade = pd.read_sql_query(query_densidade, conexao)

plt.figure(figsize=(12, 6))
barras_densidade = plt.bar(df_densidade['uf'], df_densidade['densidade'], color='#0284c7')
plt.title('Top 10 UFs com Maior Densidade Demográfica', fontweight='bold')
plt.ylabel('Habitantes por km²')

plt.xticks(rotation=45, ha='right')

for barra in barras_densidade:
    yval = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2, yval + 10, f'{yval:.1f}', ha='center', va='bottom', fontsize=9)

plt.savefig('grafico_1_densidade.png', bbox_inches='tight')
plt.close()
print("- Gráfico 1 (Densidade) gerado com sucesso!")


# =====================================================================
# DESAFIO 2: Agregação Macrorregional (Média de IDH por Região)
# =====================================================================
query_regiao = """
SELECT 
    regiao, 
    AVG(idh) AS media_idh
FROM estatisticas_ibge
GROUP BY regiao
ORDER BY media_idh DESC;
"""
df_regiao = pd.read_sql_query(query_regiao, conexao)

plt.figure(figsize=(8, 5))
barras_regiao = plt.bar(df_regiao['regiao'], df_regiao['media_idh'], color='#10b981', edgecolor='black')
plt.title('Desenvolvimento Regional: Média de IDH por Grande Região', fontweight='bold')
plt.ylabel('Índice de Desenvolvimento Humano (IDH)')
plt.ylim(0, 1.0) 

for barra in barras_regiao:
    yval = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2, yval + 0.01, f'{yval:.3f}', ha='center', va='bottom', fontweight='bold')

plt.savefig('grafico_2_regioes.png', bbox_inches='tight')
plt.close()
print("- Gráfico 2 (IDH Regiões) gerado com sucesso!")


# =====================================================================
# DESAFIO 3: Mobilidade Urbana (Frota acima da Média Nacional)
# =====================================================================
query_frota = """
SELECT 
    uf, 
    frota_veiculos
FROM estatisticas_ibge
WHERE frota_veiculos > (SELECT AVG(frota_veiculos) FROM estatisticas_ibge)
ORDER BY frota_veiculos DESC;
"""
df_frota = pd.read_sql_query(query_frota, conexao)

plt.figure(figsize=(12, 6))
barras_frota = plt.bar(df_frota['uf'], df_frota['frota_veiculos'] / 1000000, color='#ea580c')
plt.title('Pressão Logística: Estados com Frota Acima da Média Nacional', fontweight='bold')
plt.ylabel('Volume da Frota (em Milhões)')

plt.xticks (rotation=45, ha='right')

for barra in barras_frota:
    yval = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2, yval + 0.5, f'{yval:.1f}M', ha='center', va='bottom', fontsize=9)

plt.savefig('grafico_3_frota.png', bbox_inches='tight')
plt.close()
print("- Gráfico 3 (Frota de Veículos) gerado com sucesso!")


# =====================================================================
# DESAFIO 4: Vulnerabilidade Social (Baixa Renda + Alta Matrícula)
# =====================================================================
query_vulnerabilidade = """
SELECT 
    uf, 
    rendimento_per_capita, 
    matriculas_ensino_fundamental
FROM estatisticas_ibge
WHERE rendimento_per_capita < 1500.00 AND matriculas_ensino_fundamental > 200000
ORDER BY rendimento_per_capita ASC;
"""
df_vuln = pd.read_sql_query(query_vulnerabilidade, conexao)

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel('Estados (UFs)')
ax1.set_ylabel('Rendimento Per Capita (R$)', color='#dc2626', fontweight='bold')
ax1.plot(df_vuln['uf'], df_vuln['rendimento_per_capita'], color='#dc2626', marker='o', linewidth=2, label='Renda')
ax1.tick_params(axis='y', labelcolor='#dc2626')
ax1.set_ylim(0, 1600)

plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')

ax2 = ax1.twinx()  
ax2.set_ylabel('Qtd. Matrículas no Ens. Fundamental', color='#3b82f6', fontweight='bold')
ax2.bar(df_vuln['uf'], df_vuln['matriculas_ensino_fundamental'], color='#3b82f6', alpha=0.3, label='Matrículas')
ax2.tick_params(axis='y', labelcolor='#3b82f6')

plt.title('Zonas de Vulnerabilidade: Renda < R$ 1.500 E Matrículas > 200k', fontweight='bold')
plt.savefig('grafico_4_vulnerabilidade.png', bbox_inches='tight')
plt.close()
print("- Gráfico 4 (Vulnerabilidade) gerado com sucesso!")


# =====================================================================
# 5. FINALIZAÇÃO
# =====================================================================
conexao.close()
print("\nMissão cumprida! Todos os 4 gráficos estão guardados na sua pasta.")
