import sqlite3

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
from subprocess import call
import graphviz

# Connect to SQLite database
conn = sqlite3.connect('ETL_system.db')
c = conn.cursor()

# Select data from usuariosclas table
query = "SELECT total_emails, phishing_emails, clicados_emails, critico FROM usuariosclas"
data = pd.read_sql_query(query, conn)

# Separate features (X) and target variable (y)
X = data[['total_emails', 'phishing_emails', 'clicados_emails']]
y = data['critico']

# Create and fit RandomForestClassifier model
clf = RandomForestClassifier(max_depth=2, random_state=81, n_estimators=10)
clf.fit(X, y)

# Print the first instance and its prediction
print(str(X.iloc[0]) + " " + str(y.iloc[0]))
print(clf.predict([X.iloc[0]]))

# Calcular las predicciones del modelo
y_pred = clf.predict(X)

# Calcular el accuracy
accuracy = accuracy_score(y, y_pred)

# Imprimir el accuracy
print("Accuracy:", accuracy)

# Export and visualize each decision tree in the random forest
for i, estimator in enumerate(clf.estimators_):
    export_graphviz(estimator,
                    out_file=f'tree_{i}.dot',
                    feature_names=X.columns,
                    class_names=['No Crítico', 'Crítico'],
                    rounded=True,
                    proportion=False,
                    precision=2,
                    filled=True)
    call(['dot', '-Tpng', f'tree_{i}.dot', '-o', f'tree_{i}.png', '-Gdpi=600'])
