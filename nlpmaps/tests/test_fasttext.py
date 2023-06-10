from gensim.models.fasttext import load_facebook_model
from gensim.models.fasttext import load_facebook_vectors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np
import pandas as pd
import sklearn.ensemble
import sklearn
import optuna
import os
import sys

import unittest
from unittest.mock import MagicMock, patch

sys.path.insert(0, "..")

from fasttext import FastTextVectorizer, fasttext_embedding

class TestFastTextVectorizer(unittest.TestCase):
    def setUp(self):
        self.fasttext_model = MagicMock()  # Mock the FastText model
        self.fasttext_model.vector_size = 300  # Assume 300D vectors
        self.vectorizer = FastTextVectorizer(self.fasttext_model)

    def test_transform(self):
        data = ['This is a test sentence.', 'This is another test sentence.']
        transformed_data = self.vectorizer.transform(data)

        # Check the shape of the returned data
        self.assertEqual(transformed_data.shape[0], len(data))
        self.assertEqual(transformed_data.shape[1], 300)  # The dimensionality we set

        # Check that the returned data is a numpy array
        self.assertIsInstance(transformed_data, np.ndarray)

class TestFastTextEmbedding(unittest.TestCase):
    @patch('os.path.exists')
    @patch('gensim.models.fasttext.load_facebook_vectors')

    def test_fasttext_embedding(
        self, mock_load_facebook_vectors, mock_exists):
        
        # Mock the return values of the functions we're not testing
        mock_exists.return_value = False
        mock_load_facebook_vectors.return_value = MagicMock()  # Mock the FastText model
        
        # Creating a mock DataFrame
        data = pd.DataFrame({
            'text_column': ['This is a test sentence', 'Another test sentence'],
            'label_column': ['label1', 'label2']
        })

        # Running the fasttext_embedding function
        embeddings = fasttext_embedding(data, 'text_column', 'label_column')

        # Checking that the function returns an array of the right shape
        self.assertIsInstance(embeddings, np.ndarray)
        self.assertEqual(embeddings.shape[0], len(data))
        self.assertEqual(embeddings.shape[1], 300)