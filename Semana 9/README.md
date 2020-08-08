# Descubra quem fez o ENEM 2016 apenas para treino

Neste desafio deverá descobrir quais estudantes estão fazendo a prova apenas para treino.

## Tópicos

Neste desafio você aprenderá:

- Python
- Pandas
- Sklearn
- Regression
- Classification

## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

Para instalar os requisitos, execute o comando como no exemplo abaixo:

    pip install -r requirements.txt

## Detalhes

O contexto do desafio gira em torno dos resultados do ENEM 2016 (disponíveis no arquivo train.csv). Este arquivo, e apenas ele, deve ser utilizado para todos os desafios. Qualquer dúvida a respeito das colunas, consulte o [Dicionário dos Microdados do Enem 2016](https://s3-us-west-1.amazonaws.com/acceleration-assets-highway/data-science/dicionario-de-dados.zip).
 
Alguns estudantes decidem realizar prova do ENEM de forma precoce, como um teste (coluna IN_TREINEIRO). Neste desafio, você deve criar um modelo de classificação binária para inferir a mesma. Os resultados possíveis da sua resposta devem ser “0” ou “1”.

Salve sua resposta em um arquivo chamado answer.csv com duas colunas: `NU_INSCRICAO` e `IN_TREINEIRO`.

## Material de apoio
* [Basic Concepts for Classification](https://www-users.cs.umn.edu/~kumar001/dmbook/ch4.pdf)
* [Nearest Neighbor Methods for Prediction](https://devavrat.mit.edu/wp-content/uploads/2018/03/nn_survey.pdf)
* [An Introduction to Logistic Regression](https://pdfs.semanticscholar.org/3305/2b1d2363aee3ad290612109dcea0aed2a89e.pdf)
    ___
* [Imbalanced datasets](https://www3.nd.edu/~dial/publications/chawla2005data.pdf)
* [Foundations of imbalanced learning](https://pdfs.semanticscholar.org/1678/7e213ed0a5c0cf9baabdb45f9df631248a91.pdf)
* [Handle imbalanced datasets](https://towardsdatascience.com/having-an-imbalanced-dataset-here-is-how-you-can-solve-it-1640568947eb)
    ___
* [Evaluating algorithms performance](https://www.kaggle.com/metetik/classification-algorithms-comparison)
* [AUC-ROC curve](https://medium.com/greyatom/lets-learn-about-auc-roc-curve-4a94b4d88152)
* [Confusion Matrix](https://medium.com/hugo-ferreiras-blog/confusion-matrix-and-other-metrics-in-machine-learning-894688cb1c0a)
    ___
*  [Introduction to TensorFlow](https://acceleration-assets-highway.s3-us-west-1.amazonaws.com/ds-online-1/TensorFlow_on_Google_Cloud.pdf)