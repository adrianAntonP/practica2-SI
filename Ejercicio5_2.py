import pandas as pd
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz
import sqlite3

conn = sqlite3.connect('ETL_system.db')
c = conn.cursor()

query = "SELECT total_emails, phishing_emails, clicados_emails, critico FROM usuariosclas"
data = pd.read_sql_query(query, conn)

X = data[['total_emails', 'phishing_emails', 'clicados_emails']]
y = data['critico']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(X_train, y_train)

y_pred = dt_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy)

print('Error cuadrático: %.2f' % mean_squared_error(y_test, y_pred))

dot_data = export_graphviz(dt_classifier, out_file=None,
                           feature_names=X.columns,
                           class_names=['Non-Critical', 'Critical'],
                           filled=True, rounded=True,
                           special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('decision_tree_plot', format='png', view=True)
