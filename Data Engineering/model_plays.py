import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Define file paths
file_path = r'C:\Users\jjohn\Desktop\AI Apps\NFL - Data App\plays.csv'  # Input file path
output_path = r'C:\Users\jjohn\Desktop\AI Apps\NFL - Data App\feature_importance.csv'  # Output file path

# Load the dataset
data = pd.read_csv(file_path)

# Preprocessing
# Drop rows with missing values in critical columns
data = data.dropna(subset=['yardsGained', 'offenseFormation', 'pff_passCoverage', 'expectedPoints'])

# Encode categorical variables
categorical_features = ['offenseFormation', 'receiverAlignment', 'pff_passCoverage', 'pff_manZone']
encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded_features = encoder.fit_transform(data[categorical_features])

# Combine encoded features with numerical features
# Exclude 'penaltyYards' and 'prePenaltyYardsGained' from numerical features
numerical_features = [
    'quarter', 'down', 'yardsToGo', 'absoluteYardlineNumber',
    'expectedPoints', 'preSnapHomeScore', 'preSnapVisitorScore',
    'timeToThrow', 'timeInTackleBox'
]
X = np.hstack([data[numerical_features].values, encoded_features])
y = data['yardsGained'].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a regression model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Determine feature importance
feature_names = numerical_features + encoder.get_feature_names_out(categorical_features).tolist()
feature_importance = model.feature_importances_

# Create a DataFrame for feature importance
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Display top features
print("Top 10 Most Important Features:")
print(importance_df.head(10))

# Plot feature importance
plt.figure(figsize=(10, 6))
plt.barh(importance_df['Feature'][:10], importance_df['Importance'][:10], color='blue')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Top 10 Features for Predicting Offensive Yardage')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Save feature importance to a CSV file
importance_df.to_csv(output_path, index=False)
print(f"Feature importance saved to: {output_path}")
