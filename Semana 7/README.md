# Feature engineering

Neste desafio vamos praticar _feature engineering_, a arte de processar
variáveis do _data set_ a fim de torná-las mais adequadas aos algoritmos
de ML e produzir melhores resultados.

## Objetivo

O objetivo deste desafio é adquirir conhecimento e prática nas ferramentas
mais usuais de engenharia de variáveis. Com o domínio apropriado das
técnicas básicas, como _one-hot encoding_, normalização e padroniação,
o analista está mais bem preparado para conduzir uma etapa de preprocessamento
dos dados que traga bons resultados da aplicação dos algoritmos de ML.

Para isso, vamos contar com o _data set_ [Countries of the world](https://www.kaggle.com/fernandol/countries-of-the-world)
que contém 20 variáveis, como população, área costeira e tamanho dos setores de produção, de 227 países.

## Tópicos

Neste desafios nós vamos explorar:

* Feature engineering
* Processamento de texto

## Material de apoio
* [Feature Scaling](https://benalexkeen.com/feature-scaling-with-scikit-learn/)
* [Diferentes métodos para Feature Scaling - 1](https://www.trainindata.com/post/feature-engineering-comprehensive-overview)
* [Diferentes métodos para Feature Scaling - 2](https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114)
* [Para saber mais...](https://www.trainindata.com/post/best-resources-to-learn-feature-engineering) 

    ___

* [Lidando com texto, scikit tutorial](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)
* [Column transformer](https://jorisvandenbossche.github.io/blog/2018/05/28/scikit-learn-columntransformer/)
* [One Hot Encoding](https://towardsdatascience.com/categorical-encoding-using-label-encoding-and-one-hot-encoder-911ef77fb5bd)
* [What is TF-IDF](https://programmerbackpack.com/tf-idf-explained-and-python-implementation/)


## Requisitos

Você precisará de Python 3 e pip. É altamente recomendado utilizar ambientes virtuais
com o virtualenv e o arquivo `requirements.txt` para instalar os pacotes dependências
do desafio:

```bash
$ pip3 install virtualenv
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Windows

```bash
> pip3 install virtualenv
> virtualenv ..\venv -p python3
> ..\venv\Scripts\activate
> pip install -r requirements.txt
```

Quando finalizado, você pode desativar o ambiente virtual do virtualenv com:

```bash
$ deactivate
```

