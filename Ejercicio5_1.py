import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('ETL_system.db')
c = conn.cursor()

# Select data from usuariosclas table
query = "SELECT phishing_emails, clicados_emails, critico FROM usuariosclas"
data = pd.read_sql_query(query, conn)

data = data[data['phishing_emails'] != 0]
# Create a new feature by dividing 'clicados_emails' by 'phishing_emails'
data['clicados_phishing_ratio'] = data['clicados_emails'] / data['phishing_emails']

# Separate features (X) and target variable (y)
X = data[['clicados_phishing_ratio']]
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

# Plot outputs
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Clicados Emails / Phishing Emails')
plt.ylabel('Critico')
plt.title('Clicados Emails / Phishing Emails Ratio vs Critico')
plt.xticks(())
plt.yticks(())
plt.show()
