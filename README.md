# NLP Maps - Automatic selection of task-optimal embedding models

## Backgroud

This repository is for a Data Science Capstone Project collaborated between Dow Inc. and University of Washington and associated with course CHEM E 547 offered at UW.

This project is developed by Meenal Rawlani, Andrew Simon and Shijie Zhang. We appreciate the advice from Dr. Ivan Castillo (Dow Inc.), Dr. You Peng (Dow Inc.), Prof. David Beck (UW) and Evan Komp (UW).

## Overview

When trying to incorporate non-structured information in the model, word-embedding is always a key step in the process. However, it is often non-trivial to select the right word embedding method to transform text data into numerical representation that can be fed to any modeling frameworks for a task at hand. With new embedding techniques getting actively published, choosing the optimal embedding model also becomes more complicated.

NLP Maps is an algorithm designed to select the optimal word embedding method for a given task. Current state of the package takes as input text data and a metrics defined by user, automatically selects the best word embedding model from seven different models with a variety of complexity for a sentiment analysis task or text classification task. The package outputs the model chosen, embeddings of the data, and a classifier wich performs best with the embeddings generated.

The `.py` scripts in the [nlpmaps](./nlpmaps/) are modular and can be applied to any sentiment analysis task or text classification task. Demontration of each model based on benchmark dataset (IMDB) and industrial dataset (Dow) can be found in the Jupyter notebooks located in the [examples](./examples/). Demonstrations on how to fine tune the model to a given data set, as well as a demo of data preprocessing and model selection can also be found in the [examples](./examples/).

## Environment setup and installation

To create and activate an environment for this package, run the following commands:

```
conda env create -f environment.yml
conda activate nlpmaps
pip install .
```

The minimum version of Python requried for this package is Python 3.6.

## Tutorial

### Data preprocessing

The `data_preprocessing.py` script preprocesses your data by removing a customized list of stop words, removing punctuations, converting all letters to lowercase, and removing date and time in your data, based on a specific format, if applicable. The format can be easily changed based on the user's need. The use of `data_precessing.py` is optional. Note that it is not recommended to remove stop words for contextual embedding models.

To realize the preprocessing step, first get the data ready in `pd.DataFrame` format, then in a Jupyter notebook, run the following code:

```
custom_words = set("word_a", "word_b") # customize the stop words on your need
from data_preprocessing import preprocessing
preprocessing(your_data, "column name of text", custom_words)
```

The script will output a dataframe of the preprecessed data.

### Word embedding models

A total of seven embedding models are included in this package:
  - No machine learning models: Bag-of-words, TF-IDF
  - Machine learning models: Word2Vec, GloVe, FastText
  - RNN based model: ELMo
  - Transformer-based model: BERT

Note that ELMo and BERT are contextual embedding models and the rest are contextual independent.

If there is need to only get embeddings from a specific model, one can simply use the model script in [nlpmaps](./nlpmaps/) by running the following code in a Jupyter notebook (use GloVe as an example here):

```
from glove import glove_embedding
glove_embedding(your_data, "column name of text")
```

Make sure your data is in a `pd.DataFrame`. The script will output a list of embeddings generated by the model.

### Model selection

Users can easily get a summarized table of the selected metrics from seven embedding models and four ML classifiers (Random Forest, Decision Tree, Logistic Regression and SVM) based on imput data. Currently the package is able to deal with sentiment analysis and text classification tasks, but it can be easily modified for other downstream NLP tasks, and more ML models can be included if necessary.

In a Jupyter notebook, run the following code to get the table of metrics:

```
from selection import find_optimal_method
find_optimal_method(
  your_data, "column name of text", "column name of label", scoring_metric='your_metrics')
```

Based on the generated table, user can choose the model they want and run the respective model script in [nlpmaps](./nlpmaps/) to get the embeddings.

## Future direction

The package currently is able to deal with sentiment analysis and text classification tasks, but it can be easily modified for other downstream NLP tasks, and more ML models can be included if necessary.