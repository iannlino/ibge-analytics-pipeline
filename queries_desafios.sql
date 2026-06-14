-- Desafio 1 --
SELECT 
    uf,
    populacao_residente,
    area_territorial,
    ROUND((populacao_residente / area_territorial), 2) AS densidade_demografica,
    CASE 
        WHEN (populacao_residente / area_territorial) > 100 THEN 'ALTA - Foco: Transporte de Massa (Metrô/BRT)'
        WHEN (populacao_residente / area_territorial) BETWEEN 20 AND 100 THEN 'MODERADA - Foco: Integração Intermunicipal'
        ELSE 'BAIXA - Foco: Logística de Longa Distância'
    END AS status_planejamento_urbano
FROM 
    estatisticas_ibge
ORDER BY 
    densidade_demografica DESC;

-- Desafio 2 --
SELECT 
    regiao,
    ROUND(AVG(idh), 3) AS media_idh,
    ROUND(AVG(rendimento_per_capita), 2) AS media_rendimento,
    CASE 
        WHEN AVG(idh) < 0.700 THEN 'ALERTA VERMELHO - Prioridade Máxima para Repasses e Assistência'
        WHEN AVG(idh) BETWEEN 0.700 AND 0.750 THEN 'ATENÇÃO - Necessita de Incentivos Fiscais e Industriais'
        ELSE 'ESTÁVEL - Foco em Manutenção e Inovação Tecnológica'
    END AS status_alocacao_recursos
FROM 
    estatisticas_ibge
GROUP BY 
    regiao
ORDER BY 
    media_idh DESC;

-- Desafio 3 --

SELECT 
    uf,
    regiao,
    frota_veiculos,
    CASE 
        WHEN frota_veiculos > 5000000 THEN 'CRÍTICO - Risco Iminente de Colapso Logístico e Ambiental'
        WHEN frota_veiculos BETWEEN 3000000 AND 5000000 THEN 'ALTO - Necessidade de Expansão de Malha Metroviária'
        ELSE 'MODERADO - Viável para Políticas de Transição Energética Iniciais'
    END AS alerta_mobilidade_urbana
FROM 
    estatisticas_ibge
WHERE 
    frota_veiculos > (SELECT AVG(frota_veiculos) FROM estatisticas_ibge)
ORDER BY 
    frota_veiculos DESC;

-- Desafio 4 -- 

SELECT 
    uf,
    rendimento_per_capita,
    matriculas_ensino_fundamental,
    CASE 
        WHEN rendimento_per_capita < 1000.00 THEN 'INTERVENÇÃO IMEDIATA - Cesta Básica Escolar e Bolsa Família'
        ELSE 'SUPORTE CONTÍNUO - Manutenção de Merenda Reforçada e Repasses do Fundeb'
    END AS diretriz_ministerio_cidadania
FROM 
    estatisticas_ibge
WHERE 
    rendimento_per_capita < 1500.00 
    AND matriculas_ensino_fundamental > 200000
ORDER BY 
    rendimento_per_capita ASC;

-- Desafio 5 --

SELECT 
    uf,
    rendimento_per_capita,
    matriculas_ensino_fundamental,
    CASE 
        WHEN rendimento_per_capita < 1000.00 THEN 'INTERVENÇÃO IMEDIATA - Cesta Básica Escolar e Bolsa Família'
        ELSE 'SUPORTE CONTÍNUO - Manutenção de Merenda Reforçada e Repasses do Fundeb'
    END AS diretriz_ministerio_cidadania
FROM 
    estatisticas_ibge
WHERE 
    rendimento_per_capita < 1500.00 
    AND matriculas_ensino_fundamental > 200000
ORDER BY 
    rendimento_per_capita ASC;