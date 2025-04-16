import pandas as pd
import os
import gdown
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_curve
import joblib

file_id = "1XWydcU314PzUnerMD-aznUHrDcwSKuqM"
output = 'creditcard.csv'
url = f"https://drive.google.com/uc?id={file_id}"
gdown.download(url, output, quiet=False)

if not os.path.exists('data'):
    os.makedirs('data')

# reading the dataset
df = pd.read_csv('creditcard.csv')


print('Missing values per column:')
print(df.isnull().sum())

print("Zero values per column:")
print((df == 0).sum())

# Dropping duplicate rows if any
df = df.drop_duplicates()

# In the dataset, time and Amount have different scales. ML models work
# best when they have a similar scale. Therefore, we normalize it.

scaler = StandardScaler()
df[['Amount', 'Time']] = scaler.fit_transform(df[['Amount', 'Time']])


# We need to separate input from output. The values stored in class represent if
# it's a fraud transaction or not. We need to store this as y for testing.

# we want all the features except for class to use to predict fraud
X = df.drop(columns=['Class'])
y = df['Class']

# we need to break the data into training and testing sets
# 70% of the data is used to train the model through X_train and y_train

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Second split: 50% validation, 50% test from the temp set (because 50% of 30% = 15% each)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=42)


# My dataset is highly imbalanced :(
# When I parsed out the number of fraud cases vs not: its 492/ 284315 (normal data)
# Now there should be equal representation of the data

smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

print("\nOriginal class distribution:")
print(y.value_counts())

print("\nResampled class distribution:")
print(pd.Series(y_train_resampled).value_counts())

print(f"x_train_vec shape: {X_train_resampled.shape}, y_train shape: {y_train_resampled.shape}")
print(f"x_val_vec shape: {X_val.shape}, y_val shape: {y_val.shape}")
print(f"x_test_vec shape: {X_test.shape}, y_test shape: {y_test.shape}")


print('My dataset is clean and ready to go!')


#Train model
model = LogisticRegression(max_iter=500, solver='saga')
model.fit(X_train_resampled, y_train_resampled)

#predict_proba preditcs the risk score instead of binary output
y_probs = model.predict_proba(X_val)[:, 1]

print('Im training rn :)')


precision, recall, thresholds = precision_recall_curve(y_val, y_probs)
#f1 score is a mean of precision and recall which judges models ability better for
#imbalanced datasets (our case)
f1_scores = 2 * (precision * recall) / (precision + recall)

#since fraud cases are rare, 0.5 can lead to misssed fraud so we pick the best threshold
best_threshold = thresholds[f1_scores.argmax()]
# best threshold
y_pred = (y_probs > best_threshold).astype(int)

df_val = X_val.copy()
df_val["Risk_Score"] = y_probs * 100
accuracy = accuracy_score(y_val, y_pred)
conf_matrix = confusion_matrix(y_val, y_pred)
print(f"Validation Accuracy: {accuracy}")
print(f"Confusion Matrix: \n{conf_matrix}")
print("\nClassification Report:\n", classification_report(y_val, y_pred))



joblib.dump(model, 'fraud_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

os.remove('creditcard.csv')
