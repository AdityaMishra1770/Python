import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


data = pd.read_csv("data.csv")
# Assume 'data' is your dataset with features and labels
# 'features' are your top four predictor variables, and 'labels' are the corresponding class labels (genuine or counterfeit)

# Extracting top four features
top_four_features = ['See_through_register', 'Latent_image', 'Denominational_numeral_Devnagari', 'Portrait_of_Gandhi']
data_top_four = data[top_four_features]

# Step 3: Labeling
data_top_four['label'] = 0, 1, 0, 0

# Step 4: Data Splitting
X_train, X_test, y_train, y_test = train_test_split(data_top_four, data_top_four['label'], test_size=0.2, random_state=42)

# Step 5: Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{classification_rep}')
