# src/utils.py

import numpy as np

def entropy(y):
    """
    Calculate the entropy of a given array of labels.

    :param y: Array of labels (0s and 1s)
    :return: Entropy of the array
    """
    # Ensure labels are binary
    if not np.all(np.isin(y, [0, 1])):
        raise ValueError("Labels must be binary (0s and 1s)")

    # Calculate entropy using Shannon formula
    p0 = np.mean(y == 0)
    p1 = np.mean(y == 1)
    return -p0 * np.log2(p0) - p1 * np.log2(p1)

def gini(y):
    """
    Calculate the Gini impurity of a given array of labels.

    :param y: Array of labels (0s and 1s)
    :return: Gini impurity of the array
    """
    # Ensure labels are binary
    if not np.all(np.isin(y, [0, 1])):
        raise ValueError("Labels must be binary (0s and 1s)")

    # Calculate Gini impurity
    p0 = np.mean(y == 0)
    p1 = np.mean(y == 1)
    return 1 - (p0 ** 2 + p1 ** 2)

def split_data(X, y, feature, threshold):
    """
    Split the data into two subsets based on a given feature and threshold.

    :param X: Feature matrix
    :param y: Array of labels
    :param feature: Index of the feature to split on
    :param threshold: Threshold value for splitting
    :return: Two subsets of the data
    """
    # Split data into two subsets
    left_indices = X[:, feature] < threshold
    right_indices = X[:, feature] >= threshold

    # Return the two subsets
    return X[left_indices], X[right_indices], y[left_indices], y[right_indices]

# This was tricky, but we need to handle the case where the split results in empty subsets
def handle_empty_splits(X, y):
    """
    Handle the case where the split results in empty subsets.

    :param X: Feature matrix
    :param y: Array of labels
    :return: The original data, since the split resulted in empty subsets
    """
    # Check if the split resulted in empty subsets
    if len(X) == 0 or len(y) == 0:
        # Not proud of this but it works
        return X, y