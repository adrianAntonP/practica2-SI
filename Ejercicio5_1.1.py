import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('ETL_system.db')
c = conn.cursor()

# Select data from usuariosclas table
query = "SELECT permisos, total_emails, phishing_emails, clicados_emails, critico FROM usuariosclas"
data = pd.read_sql_query(query, conn)

# Separate features (X) and target variable (y)
X = data[['total_emails', 'phishing_emails', 'clicados_emails']]
y = data['critico']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create linear regression object
regr = LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(X_test)

# Print the coefficients
print('Coefficients:', regr.coef_)

# Print the mean squared error
print('Mean squared error: %.2f' % mean_squared_error(y_test, y_pred))

# Sort the data based on phishing_emails
sorted_indices = X_test['phishing_emails'].argsort()
X_test_sorted = X_test.iloc[sorted_indices]
y_test_sorted = y_test.iloc[sorted_indices]
y_pred_sorted = pd.Series(y_pred).iloc[sorted_indices]

# Plot outputs
# Plot outputs for total_emails
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.scatter(X_test_sorted['total_emails'], y_test_sorted, color='black')
plt.plot(X_test_sorted['total_emails'], y_pred_sorted, color='blue', linewidth=3)
plt.xlabel('Total Emails')
plt.ylabel('Critico')
plt.title('Total Emails vs Critico')

# Plot outputs for phishing_emails
plt.subplot(1, 3, 2)
plt.scatter(X_test_sorted['phishing_emails'], y_test_sorted, color='black')
plt.plot(X_test_sorted['phishing_emails'], y_pred_sorted, color='blue', linewidth=3)
plt.xlabel('Phishing Emails')
plt.ylabel('Critico')
plt.title('Phishing Emails vs Critico')

# Plot outputs for clicados_emails
plt.subplot(1, 3, 3)
plt.scatter(X_test_sorted['clicados_emails'], y_test_sorted, color='black')
plt.plot(X_test_sorted['clicados_emails'], y_pred_sorted, color='blue', linewidth=3)
plt.xlabel('Clicados Emails')
plt.ylabel('Critico')
plt.title('Clicados Emails vs Critico')

plt.tight_layout()
plt.show()



