# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# CardioIA 

## 👨‍🎓 Integrantes: 
<p align="left">
  <a href="https://github.com/Luiz-Frederico" target="_blank">
    <img src="https://github.com/Luiz-Frederico.png" width="64" height="64" alt="@Luiz-Frederico" />
  </a>
  </a>
  <a href="https://github.com/henriquehsilva" target="_blank">
    <img src="https://github.com/henriquehsilva.png" width="64" height="64" alt="@henriquehsilva" />
  </a>
  <a href="https://github.com/manoellaweiser-gif" target="_blank">
    <img src="https://github.com/manoellaweiser-gif.png" width="64" height="64" alt="@manoellaweiser-gif" />
  </a>
  <a href="https://github.com/JoaoMDPaiva" target="_blank">
    <img src="https://github.com/JoaoMDPaiva.png" width="64" height="64" alt="@JoaoMDPaiva" />
  </a>
  <a href="https://github.com/younmariana-create" target="_blank">
    <img src="https://github.com/younmariana-create.png" width="64" height="64" alt="@younmariana-create" />
  </a>
</p>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Orabona</a>

<p align="left">
  <a href="https://github.com/leoruiz197" target="_blank">
    <img src="https://github.com/leoruiz197.png" width="64" height="64" alt="@leoruiz197" />
  </a>
  
  </p>

### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">André Godoi</a>

<p align="left">
  <a href="https://github.com/agodoi" target="_blank">
    <img src="https://github.com/agodoi.png" width="64" height="64" alt="@agodoi" />
  </a>
  
  </p>


## 📜 Descrição

O CardioIA é um projeto voltado à exploração do uso de Inteligência Artificial na área da saúde cardiovascular. A proposta consiste em trabalhar com diferentes tipos de dados relacionados à cardiologia, incluindo dados numéricos, textuais e visuais, buscando compreender como técnicas de Ciência de Dados, Machine Learning, Processamento de Linguagem Natural e Visão Computacional podem ser aplicadas nesse contexto.

Na primeira fase do projeto, foram selecionados e organizados diferentes conjuntos de dados. Para os dados numéricos, foi utilizado o conjunto Heart Disease, disponibilizado pelo UCI Machine Learning Repository, contendo informações clínicas estruturadas de pacientes. Para os dados textuais, foram selecionados artigos científicos relacionados à saúde cardiovascular, fatores de risco, determinantes sociais e envelhecimento populacional. Para os dados visuais, foi utilizado o conjunto de radiografias de tórax do NIH Chest X-ray, disponibilizado por meio do Google Cloud.

O projeto busca explorar a integração desses diferentes formatos de dados como uma possibilidade para o desenvolvimento futuro de soluções inteligentes voltadas à análise de informações cardiovasculares.

Nesta primeira etapa, o foco está na identificação, organização, documentação e análise inicial dos dados, considerando aspectos como qualidade, valores ausentes, origem, relevância, possíveis vieses e governança. Em etapas posteriores, os dados poderão ser utilizados para o desenvolvimento e avaliação de modelos de Inteligência Artificial.

O CardioIA possui caráter acadêmico e experimental, tendo como objetivo desenvolver conhecimentos e aplicações práticas de Ciência de Dados e Inteligência Artificial no contexto da saúde cardiovascular.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:
Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- **.github**: arquivos de configuração e suporte ao gerenciamento do projeto no GitHub.
- **analise**: scripts utilizados para análise e exploração dos dados, incluindo análises estatísticas do conjunto de dados numéricos.
- **artigos**: arquivos de texto utilizados na etapa de dados textuais do projeto.
- **dados**: conjuntos de dados utilizados no projeto, incluindo os dados numéricos do CardioIA.
- **images**: imagens utilizadas na etapa de dados visuais do projeto.
- **assets**: arquivos relacionados a elementos visuais e recursos complementares do projeto.
- **config**: arquivos relacionados a configurações do projeto.
- **document**: documentos relacionados às atividades e à documentação do projeto.
- **scripts**: scripts auxiliares utilizados no desenvolvimento do projeto.
- **src**: espaço destinado ao código-fonte desenvolvido nas diferentes fases do projeto.
- **.gitignore**: arquivo que define arquivos e pastas que não devem ser versionados pelo Git.
- **README.md**: documento principal de apresentação, organização e documentação do projeto.


---  

# Fase 1 - Batimentos de Dados (IoT)

## 1. Parte 1 — Dados Numéricos

### Origem dos dados
Os dados numéricos utilizados nesta etapa são provenientes do dataset Heart Disease, disponibilizado pelo UCI Machine Learning Repository. A base utilizada corresponde ao conjunto Cleveland e contém 303 registros e 14 variáveis relacionadas a características clínicas dos pacientes e ao diagnóstico de doença cardíaca.

Os dados são provenientes de registros clínicos utilizados para pesquisas relacionadas a doenças cardíacas. Para esta atividade, o arquivo original foi organizado e convertido para o formato CSV, resultando no arquivo heart_disease_final.csv.

Fonte: UCI Machine Learning Repository – Heart Disease:
https://archive.ics.uci.edu/dataset/45/heart+disease

### Variáveis

O dataset contém 14 variáveis:

- idade
- sexo
- tipo_dor_peito
- pressao_arterial
- colesterol
- glicemia
- ecg
- frequencia_cardiaca_max
- angina_exercicio
- oldpeak
- inclinacao_st
- vasos_principais
- thal
- diagnostico

### Relevância clínica

As variáveis consideradas mais relevantes para um projeto de Inteligência Artificial aplicado à cardiologia são idade, tipo de dor no peito, pressão arterial, colesterol, frequência cardíaca máxima, resultado do eletrocardiograma e angina induzida por exercício.

Essas variáveis representam diferentes características clínicas dos pacientes e podem ser utilizadas em conjunto para identificar padrões nos dados. Em etapas futuras do projeto CardioIA, essas informações poderão servir como características de entrada para modelos de Machine Learning voltados à análise e classificação de padrões associados às doenças cardíacas.

### Link para os dados

O conjunto de dados preparado está disponível publicamente no Google Drive:

https://drive.google.com/drive/folders/10wjLggSbvHDbi6sunj_NVcDA0hr7Yb_B?hl=pt-br

## 2. Parte 2 – Dados Textuais (NLP)

### Como os dados podem ser utilizados em NLP

Os textos podem ser utilizados em técnicas de Processamento de Linguagem Natural (NLP) para identificar e organizar informações relevantes relacionadas à saúde cardiovascular.

Entre as possíveis aplicações estão a extração de sintomas e fatores de risco, classificação de textos por temas, identificação de informações relacionadas a tratamentos e medicamentos e extração de entidades relevantes presentes nos documentos.

Essas técnicas podem permitir que grandes volumes de informações textuais sejam processados automaticamente, facilitando a identificação de padrões e informações relevantes para as etapas futuras do projeto CardioIA.

### Relevância para o projeto

Os dados textuais são relevantes para o CardioIA porque complementam os dados numéricos e visuais utilizados no projeto. Enquanto os dados numéricos apresentam características clínicas estruturadas e as imagens permitem análises por Visão Computacional, os textos fornecem informações em linguagem natural relacionadas a sintomas, doenças, tratamentos e aspectos da saúde cardiovascular.

Em etapas futuras, técnicas de NLP poderão ser utilizadas para transformar essas informações textuais em dados estruturados, permitindo sua utilização em sistemas inteligentes e contribuindo para uma análise mais ampla das informações relacionadas à cardiologia.

### Links

O conjunto de dados preparado está disponível publicamente no Google Drive:

https://drive.google.com/drive/folders/1MeP-nTlPJNDzYhA6_vgPYbJDdyuNySoy

Os textos utilizados no projeto estão disponíveis na pasta artigos do repositório (dados textuais) .

As versões originais dos textos podem ser consultadas nas respectivas fontes acadêmicas.

### Fontes

Foram selecionados textos científicos relacionados às doenças cardiovasculares e seus fatores associados.

1. Precisamos Falar de Determinantes Sociais de Saúde Cardiovascular
   Fonte: SciELO / Arquivos Brasileiros de Cardiologia
   Link: https://www.scielo.br/j/abc/a/wNjCYTGGrxJCPDTBJ3qB64n/?format=html&lang=pt

2. Impacto do Envelhecimento Populacional na Prevalência de Doenças Cardiovasculares nas Macrorregiões do Brasil: Previsões para 2050
   Fonte: SciELO / Arquivos Brasileiros de Cardiologia
   Link: https://www.scielo.br/j/abc/a/nFdVjRPRbdjy5hZgwB3ByFy/?lang=pt
   Link alternativo: https://www.researchgate.net/publication/408051438_Impacto_do_Envelhecimento_Populacional_na_Prevalencia_de_Doencas_Cardiovasculares_nas_Macrorregioes_do_Brasil_Previsoes_para_2050


## 3. Parte 3 – Dados Visuais (VC)

### Tipo de exame

Para a etapa de dados visuais do CardioIA, foi selecionado o conjunto de dados de radiografias de tórax do NIH (NIH Chest X-ray).

As imagens são radiografias de tórax e podem apresentar diferentes alterações e condições torácicas. O conjunto é adequado para exploração de técnicas de Visão Computacional e Inteligência Artificial aplicadas à análise de imagens médicas.

### Origem das imagens

As imagens foram obtidas por meio do conjunto de dados público disponibilizado pelo Google Cloud, baseado no conjunto de dados de radiografias de tórax do NIH e estão disponíveis na pasta images do repositório.

O conjunto é fornecido pelo NIH Clinical Center e contém imagens desidentificadas de radiografias de tórax em formato PNG.

Fonte: Google Cloud / NIH Clinical Center

### Aplicações de Visão Computacional

As imagens podem ser utilizadas em técnicas de Visão Computacional e Machine Learning para:

- classificação automática de imagens;
- identificação de padrões presentes nas radiografias;
- detecção de alterações torácicas;
- extração de características visuais;
- treinamento de modelos de Deep Learning;
- desenvolvimento de sistemas de apoio à análise de imagens médicas.

### Relevância para o projeto

Os dados visuais complementam os dados numéricos e textuais utilizados no CardioIA.

Enquanto os dados numéricos representam características clínicas estruturadas e os dados textuais fornecem informações em linguagem natural, as imagens acrescentam informações visuais que podem ser analisadas por técnicas de Visão Computacional.

A utilização dessas imagens permite explorar, em etapas futuras, modelos de Inteligência Artificial capazes de identificar padrões em radiografias de tórax e contribuir para uma análise mais ampla de informações relacionadas à saúde cardiovascular.

### Link para as imagens

O conjunto de dados utilizado está disponível por meio da documentação do Google Cloud:

https://docs.cloud.google.com/healthcare-api/docs/resources/public-datasets/nih-chest?hl=pt-br

Fonte original: NIH Clinical Center.

O conjunto de dados preparado está disponível publicamente no Google Drive:

https://drive.google.com/drive/folders/14zE-ZroFioYjiMi5eaRgsNaMwgGx0aWa?hl=pt-br

## 4. Considerações sobre Governança de Dados

O projeto CardioIA utiliza diferentes tipos de dados — numéricos, textuais e visuais — para explorar aplicações de Inteligência Artificial na área da saúde cardiovascular. Dessa forma, aspectos relacionados à qualidade, privacidade, segurança, representatividade e possíveis vieses dos dados devem ser considerados durante o desenvolvimento do projeto.

### Qualidade dos dados

No conjunto de dados numéricos utilizado, foram identificados 303 registros e 14 variáveis. Durante a análise inicial, foram encontrados 4 valores ausentes na variável `vasos_principais` e 2 valores ausentes na variável `thal`. Esses valores foram mantidos no conjunto de dados original, sem preenchimento artificial, para preservar as características do dataset.

Também não foram identificadas duplicatas nos dados analisados.

Os dados textuais foram organizados individualmente em arquivos `.txt`, mantendo seu conteúdo para posterior utilização em técnicas de Processamento de Linguagem Natural.

No conjunto de dados visuais, foram utilizadas imagens provenientes do NIH Chest X-ray, disponibilizadas de forma desidentificada.

### Privacidade e proteção de dados

Os conjuntos de dados utilizados no projeto são provenientes de fontes públicas e acadêmicas. Os dados utilizados devem ser tratados de acordo com as condições de uso e licenciamento estabelecidas pelas respectivas fontes.

No caso das imagens médicas utilizadas, a utilização de dados desidentificados reduz os riscos relacionados à exposição de informações pessoais dos pacientes.

O CardioIA não tem como objetivo armazenar ou divulgar informações pessoais identificáveis de pacientes.

### Possíveis vieses

Os conjuntos de dados utilizados podem apresentar vieses relacionados à população representada, à origem dos dados e à forma como as informações foram coletadas ou classificadas.

O conjunto de dados numéricos possui uma quantidade limitada de registros e pode não representar adequadamente diferentes populações.

Os dados textuais também podem refletir perspectivas específicas dos autores e das fontes utilizadas.

No caso das imagens, os resultados de modelos de Inteligência Artificial podem ser influenciados pela distribuição da população, pelos equipamentos utilizados, pela qualidade das imagens e pela forma como os rótulos foram obtidos.

Por esse motivo, eventuais modelos desenvolvidos futuramente a partir desses dados não devem ser considerados automaticamente generalizáveis para toda a população.

### Uso responsável da Inteligência Artificial

Os dados utilizados no projeto têm finalidade acadêmica e de pesquisa. Eventuais modelos desenvolvidos nas etapas futuras devem ser considerados ferramentas de apoio à análise e não substitutos da avaliação realizada por profissionais de saúde.

Resultados produzidos por modelos de Inteligência Artificial devem ser interpretados considerando as limitações dos dados utilizados para seu treinamento e validação.

### Limitações

Entre as principais limitações identificadas estão:

- quantidade limitada de registros no conjunto de dados numéricos;
- presença de valores ausentes em algumas variáveis;
- possibilidade de vieses na composição dos datasets;
- diferenças entre as populações representadas pelos diferentes conjuntos de dados;
- limitações inerentes à classificação e anotação dos dados;
- necessidade de validação adequada antes de qualquer aplicação prática.

Essas limitações deverão ser consideradas nas próximas etapas do desenvolvimento do CardioIA.

## 5. Referências

### Dados numéricos


UCI MACHINE LEARNING REPOSITORY. **Heart Disease Dataset**. University of California, Irvine. Disponível em: https://archive.ics.uci.edu/dataset/45/heart+disease. Acesso em: 24 ago. 2026.

### Dados textuais

ARQUIVOS BRASILEIROS DE CARDIOLOGIA. **Precisamos Falar de Determinantes Sociais de Saúde Cardiovascular**. SciELO. Disponível em: https://www.scielo.br/j/abc/a/wNjCYTGGrxJCPDTBJ3qB64n/?format=html&lang=pt. Acesso em: 24 ago. 2026.

ARQUIVOS BRASILEIROS DE CARDIOLOGIA. **Impacto do Envelhecimento Populacional na Prevalência de Doenças Cardiovasculares nas Macrorregiões do Brasil: Previsões para 2050**. SciELO. Disponível em: https://www.scielo.br/j/abc/a/nFdVjRPRbdjy5hZgwB3ByFy/?lang=pt. Acesso em: 24 ago. 2026.

### Dados visuais

GOOGLE CLOUD. **NIH Chest X-ray Dataset**. Google Cloud Healthcare API. Disponível em: https://docs.cloud.google.com/healthcare-api/docs/resources/public-datasets/nih-chest?hl=pt-br. Acesso em: 24 ago. 2026.

NATIONAL INSTITUTES OF HEALTH. **NIH Clinical Center Chest X-ray Dataset**. NIH Clinical Center.

---

## 🔧 Como executar o código


### Pré-requisitos

Para executar os scripts de análise dos dados numéricos, são necessários:

- Python 3;
- Pandas;
- NumPy;
- ambiente de desenvolvimento como VS Code ou similar.

### Execução

Após clonar o repositório, acesse a pasta do projeto:

```bash
cd CardioIA
```

## 🗃 Histórico de lançamentos

    
* 0.1.0 - 24/08/2026
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
