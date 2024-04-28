import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
import sqlite3

conn = sqlite3.connect('ETL_system.db')
c = conn.cursor()

query = "SELECT phishing_emails, clicados_emails, critico FROM usuariosclas"
data = pd.read_sql_query(query, conn)

data = data[data['phishing_emails'] != 0]
# Creamos la variable independiente
data['clicados_phishing_ratio'] = data['clicados_emails'] / data['phishing_emails']
X = data[['clicados_phishing_ratio']]
y = data['critico']
# Separamos los datos de entrenamiento y de testeo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
regr = LinearRegression()
# Entrenamos el modelo
regr.fit(X_train, y_train)

# Hacemos prediciones con los datos de testeo
y_pred = regr.predict(X_test)

print('Coeficiente:', regr.coef_)

print('Error cuadrático: %.2f' % mean_squared_error(y_test, y_pred))

# Gráfico
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Clicados Emails / Phishing Emails')
plt.ylabel('Critico')
plt.title('Clicados Emails / Phishing Emails Ratio vs Critico')
plt.xticks(())
plt.yticks(())
plt.show()
