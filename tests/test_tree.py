import unittest
import numpy as np
from decision_tree import DecisionTree

class TestDecisionTree(unittest.TestCase):
    def test_init(self):
        """Test DecisionTree initialization"""
        # Create a sample dataset
        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([0, 0, 1])

        # Create a decision tree
        tree = DecisionTree(X, y)

        # Check that the tree is not None
        self.assertIsNotNone(tree)

    def test_train(self):
        """Test DecisionTree training"""
        # Create a sample dataset
        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([0, 0, 1])

        # Create a decision tree
        tree = DecisionTree(X, y)

        # Train the tree
        tree.train()

        # Check that the tree has been trained
        self.assertIsNotNone(tree.root)

    def test_predict(self):
        """Test DecisionTree prediction"""
        # Create a sample dataset
        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([0, 0, 1])

        # Create a decision tree
        tree = DecisionTree(X, y)

        # Train the tree
        tree.train()

        # Create a sample prediction
        X_pred = np.array([[2, 3]])

        # Make a prediction
        prediction = tree.predict(X_pred)

        # Check that the prediction is correct
        self.assertEqual(prediction, 0)

    def test_predict_multiple(self):
        """Test DecisionTree prediction for multiple samples"""
        # Create a sample dataset
        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([0, 0, 1])

        # Create a decision tree
        tree = DecisionTree(X, y)

        # Train the tree
        tree.train()

        # Create multiple sample predictions
        X_pred = np.array([[2, 3], [4, 5]])

        # Make predictions
        predictions = tree.predict(X_pred)

        # Check that the predictions are correct
        self.assertEqual(predictions, [0, 0])

if __name__ == '__main__':
    unittest.main()