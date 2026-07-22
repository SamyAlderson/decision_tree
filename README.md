# Decision Tree
Fast and simple decision tree implementation for Python

## What it does
This is a basic decision tree implementation to classify data. It's useful for prototyping or when you need a simple model. It supports node splitting and prediction.

## Install
```bash
pip install python-decision-tree
```
or install it directly from this repository:
```bash
pip install git+https://github.com/SamyAlderson/decision_tree.git
```
## Usage
```python
from decision_tree import DecisionTree

# create a dataset
X = [[1, 2], [3, 4], [5, 6]]
y = [0, 0, 1]

# create a decision tree
tree = DecisionTree()
tree.fit(X, y)

# make a prediction
print(tree.predict([[2, 2]]))
```
## Build from source
```bash
git clone https://github.com/SamyAlderson/decision_tree.git
cd decision_tree
python setup.py install
```
## Tests
```bash
python -m unittest discover -s tests
```
## Project structure
- `decision_tree.py`: main implementation file
- `tests/`: unit tests
- `setup.py`: setup file for installation
- `README.md`: this file
- `LICENSE`: license information

## License
Copyright (c) 2026 SamyAlderson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.