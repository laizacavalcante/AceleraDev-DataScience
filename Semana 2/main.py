#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


# Checking dataset
black_friday.head(5)


# In[58]:


# Retrieving missing data
missing = pd.DataFrame({'Columns': black_friday.columns,
                        'dtype': black_friday.dtypes,
                        'missing nan': black_friday.isna().sum(),
                        'missing null': black_friday.isnull().sum(),
                        'percentage nan': (black_friday.isna().sum()/black_friday.shape[0])*100 })

missing


# In[23]:


# Retrieving sum of gender occurences by age
black_friday.groupby('Age')['Gender'].value_counts()


# In[24]:


# Getting occurances of Woman between Age 26-35 
df_woman_age = black_friday[ (black_friday['Gender'] == 'F' ) & (black_friday['Age'] == '26-35')]
df_woman_age['Age'].count()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[8]:


def q1():
    shape = black_friday.shape
    return shape
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[5]:


def q2():
    # Retorne aqui o resultado da questão 2.
    woman_filter = black_friday[ (black_friday['Gender'] == 'F' ) & (black_friday['Age'] == '26-35')]
    woman_num = woman_filter['Age'].count()
    return woman_num
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[6]:


def q3():
    # Retorne aqui o resultado da questão 3.
    user_unique = black_friday['User_ID'].nunique()
    return user_unique
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    dtypes_list = black_friday.dtypes.to_list()
    return dtypes_list
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[8]:


def q5():
    # Retorne aqui o resultado da questão 5.
    missing_percentage = black_friday.isnull().sum().max()/black_friday.shape[0]
    return missing_percentage
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    missing_max = black_friday.isnull().sum().max()
    return missing_max
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    product3_mode = black_friday['Product_Category_3'].mode(dropna=True)
    return product3_mode[0]
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    # Retorne aqui o resultado da questão 8.
    normalized = (black_friday['Purchase'] - black_friday['Purchase'].mean()) / (black_friday['Purchase'].std())
    normalized_mean = normalized.mean()
    return normalized_mean
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    # Retorne aqui o resultado da questão 9.
    padronized = (black_friday['Purchase'] - black_friday['Purchase'].min()) / (black_friday['Purchase'].max() - black_friday['Purchase'].min())
    occurences = padronized.shape[0]
    return occurences
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    # Retorne aqui o resultado da questão 10.
    products_missing = black_friday[ (black_friday['Product_Category_2'].isnull()) 
                                & (black_friday['Product_Category_3'].isnull())]

    result = products_missing[['Product_Category_2', 'Product_Category_3']].isnull().all()
    return result[0]
    pass


# In[197]:





# In[ ]:




