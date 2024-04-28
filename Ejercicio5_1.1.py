import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import sqlite3

conn = sqlite3.connect('ETL_system.db')
c = conn.cursor()

query = "SELECT permisos, total_emails, phishing_emails, clicados_emails, critico FROM usuariosclas"
data = pd.read_sql_query(query, conn)

X = data[['total_emails', 'phishing_emails', 'clicados_emails']]
y = data['critico']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

regr = LinearRegression()

regr.fit(X_train, y_train)

y_pred = regr.predict(X_test)

print('Coeficientes:', regr.coef_)

print('Error Cuadrático: %.2f' % mean_squared_error(y_test, y_pred))

sorted_indices = X_test['phishing_emails'].argsort()
X_test_sorted = X_test.iloc[sorted_indices]
y_test_sorted = y_test.iloc[sorted_indices]
y_pred_sorted = pd.Series(y_pred).iloc[sorted_indices]

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.scatter(X_test_sorted['total_emails'], y_test_sorted, color='black')
plt.plot(X_test_sorted['total_emails'], y_pred_sorted, color='blue', linewidth=3)
plt.xlabel('Total Emails')
plt.ylabel('Critico')
plt.title('Total Emails vs Critico')

plt.subplot(1, 3, 2)
plt.scatter(X_test_sorted['phishing_emails'], y_test_sorted, color='black')
plt.plot(X_test_sorted['phishing_emails'], y_pred_sorted, color='blue', linewidth=3)
plt.xlabel('Phishing Emails')
plt.ylabel('Critico')
plt.title('Phishing Emails vs Critico')

plt.subplot(1, 3, 3)
plt.scatter(X_test_sorted['clicados_emails'], y_test_sorted, color='black')
plt.plot(X_test_sorted['clicados_emails'], y_pred_sorted, color='blue', linewidth=3)
plt.xlabel('Clicados Emails')
plt.ylabel('Critico')
plt.title('Clicados Emails vs Critico')

plt.tight_layout()
plt.show()



