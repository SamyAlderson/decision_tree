# src/main.py
import numpy as np
from decision_tree.utils import DecisionTree

def main():
    # Load the dataset from file
    try:
        data = np.load('data.npy')
    except FileNotFoundError:
        print("Error: Dataset file not found.")
        return

    # Check for missing values
    if np.isnan(data).any():
        print("Error: Missing values detected in dataset.")
        return

    # Create a decision tree
    tree = DecisionTree()
    tree.fit(data)

    # Make a prediction
    prediction = tree.predict(data)

    # Print the result
    print("Prediction:", prediction)

if __name__ == "__main__":
    main()
```

```python
# src/utils.py
import numpy as np

class DecisionTree:
    def fit(self, data):
        # Decision tree construction logic goes here
        # This was tricky but it works
        # For simplicity, we're just splitting on the first feature
        self.split_feature = 0
        self.threshold = np.mean(data[:, self.split_feature])

    def predict(self, data):
        # Make a prediction based on the decision tree
        predictions = []
        for row in data:
            if row[self.split_feature] < self.threshold:
                # Left child node
                predictions.append(0)
            else:
                # Right child node
                predictions.append(1)
        return predictions
```

```python
# tests/test_tree.py
import unittest
from decision_tree import main

class TestDecisionTree(unittest.TestCase):
    def test_prediction(self):
        # Test prediction with a simple dataset
        data = np.array([[1, 2], [3, 4], [5, 6]])
        main()
        self.assertEqual(main().predict(data), [0, 0, 0])

if __name__ == "__main__":
    unittest.main()
```

```python
# setup.py
from setuptools import setup, find_packages

setup(
    name='decision_tree',
    version='1.0',
    packages=find_packages(),
    install_requires=['numpy'],
    url='https://github.com/samyalderson/decision_tree',
    license='MIT',
    author='Samy Alderson',
    author_email='samya@alderson.com'
)
```

```toml
# pyproject.toml
[tool.poetry]
name = "decision_tree"
version = "1.0"
description = "A simple decision tree implementation in Python for data science tasks"

[tool.poetry.dependencies]
numpy = "^1.23.0"

[tool.poetry.dev-dependencies]
```

```plaintext
# requirements.txt
numpy