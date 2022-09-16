# Desafio realizado no Segundo Challenge DataScience da Alura

## INFORMAÇÕES GERAIS
**EMPRESA**: banco digital internacional chamado Alura Cash

**OBJETIVO**: Diminuir as perdas financeiras por conta de pessoas mutuarias que não quitam suas dívidas.

**COMO FAZER**: Encontrar padrões para identificar os clientes que sejam potenciais inadimplentes. Para isso, deseja-se desenvolver um modelo de **Machine-Learning** para classificar os solicitantes de empréstimo que possívelmente se tornem inadiMplentes e apresentar os resultados em um dashboard para os tomadores de decisão da empresa. 


## 01 - Consulta e Manipulação da Base de Dados

A empresa disponibilizou os dados referentes às informações dos clientes através de um [dump](Dados/dumps), o que possibilitou a criação de um no Banco de Dados usando o MySQL. O primeiro passo foi tratar o conjunto de dados para deixá-los padronizados no texto, bem como, corrigir inconsistências relacionadas ao tipo e estruturação. Após o tratamento dos dados, optou-se por juntar todas as tabelas conforme ID do solicitante, ID da solicitação e ID do score de cada solicitante.

O desenvolvimento desta primeira etapa está neste [script](1-Consulta-e-Manipulacao-dos-dados-no-MySQL.sql), e a partir disso todos os dados foram exportados para um único [arquivo](Dados/dados_unificados.csv) CSV.

Mais detalhes sobre as informações fornecidas estão no dicionário a seguir: 

### dados_mutuarios
Tabela contendo os dados pessoais de cada solicitante

| Feature | Característica |
| --- | --- |
|`person_id`|ID da pessoa solicitante|
| `person_age` | Idade da pessoa - em anos - que solicita empréstimo |
| `person_income` | Salário anual da pessoa solicitante |
| `person_home_ownership` | Situação da propriedade que a pessoa possui: *Alugada* (`Rent`), *Própria* (`Own`), *Hipotecada* (`Mortgage`) e *Outros casos* (`Other`) |
| `person_emp_length` | Tempo - em anos - que a pessoa trabalhou |

### emprestimos

Tabela contendo as informações do empréstimo solicitado

| Feature | Característica |
| --- | --- |
|`loan_id`|ID da solicitação de empréstico de cada solicitante|
| `loan_intent` | Motivo do empréstimo: *Pessoal* (`Personal`), *Educativo* (`Education`), *Médico* (`Medical`), *Empreendimento* (`Venture`), *Melhora do lar* (`Homeimprovement`), *Pagamento de débitos* (`Debtconsolidation`) |
| `loan_grade` | Pontuação de empréstimos, por nível variando de `A` a `G` |
| `loan_amnt` | Valor total do empréstimo solicitado |
| `loan_int_rate` | Taxa de juros |
| `loan_status` | Possibilidade de inadimplência |
| `loan_percent_income` | Renda percentual entre o *valor total do empréstimo* e o *salário anual* |


### historicos_banco

Histório de emprétimos de cada cliente

| Feature | Característica |
| --- | --- |
|`cb_id`|ID do histórico de cada solicitante|
| `cb_person_default_on_file` | Indica se a pessoa já foi inadimplente: sim (`Y`,`YES`) e não (`N`,`NO`) |
| `cb_person_cred_hist_length` | Tempo - em anos - desde a primeira solicitação de crédito ou aquisição de um cartão de crédito |

### id

Tabela que relaciona os IDs de cada informação da pessoa solicitante

| Feature | Característica |
| --- | --- |
|`person_id`|ID da pessoa solicitante|
|`loan_id`|ID da solicitação de empréstico de cada solicitante|
|`cb_id`|ID do histórico de cada solicitante|


## 02 - Modelo preditivo para classificar cliente inadimplentes

O desenvolvimento do modelo está neste [notebook](2-Machine-Learning-para-Classificacao-de-Inadimplentes.ipynb).
