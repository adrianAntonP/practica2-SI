import sqlite3

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
from subprocess import call
import graphviz

conn = sqlite3.connect('ETL_system.db')
c = conn.cursor()

query = "SELECT total_emails, phishing_emails, clicados_emails, critico FROM usuariosclas"
data = pd.read_sql_query(query, conn)

X = data[['total_emails', 'phishing_emails', 'clicados_emails']]
y = data['critico']

clf = RandomForestClassifier(max_depth=2, random_state=42, n_estimators=10)
clf.fit(X, y)

print(str(X.iloc[0]) + " " + str(y.iloc[0]))
print(clf.predict([X.iloc[0]]))

y_pred = clf.predict(X)

accuracy = accuracy_score(y, y_pred)

print("Exactitud:", accuracy)

#Creación de imagenes
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
