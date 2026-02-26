
import pandas as pd
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['label'] = iris.target

# Check for labeled data
if 'label' in data.columns:
    model_type = "Supervised Learning - Classification Model"
else:
    model_type = "Unsupervised Learning"

print("AI Model Selected:", model_type)
OUTPUT:
AI Model Selected: Supervised Learning - Classification Model
