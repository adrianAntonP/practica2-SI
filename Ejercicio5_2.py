import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz
import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('ETL_system.db')
c = conn.cursor()

# Seleccionar datos de la tabla usuariosclas
query = "SELECT total_emails, phishing_emails, clicados_emails, critico FROM usuariosclas"
data = pd.read_sql_query(query, conn)

# Separate features (X) and target variable (y)
X = data[['total_emails', 'phishing_emails', 'clicados_emails']]
y = data['critico']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create Decision Tree classifier object
dt_classifier = DecisionTreeClassifier()

# Train the model using the training sets
dt_classifier.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = dt_classifier.predict(X_test)

# Print the mean squared error
print('Mean squared error: %.2f' % mean_squared_error(y_test, y_pred))

# Export decision tree plot
dot_data = export_graphviz(dt_classifier, out_file=None,
                           feature_names=X.columns,
                           class_names=['Non-Critical', 'Critical'],
                           filled=True, rounded=True,
                           special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('decision_tree_plot', format='png', view=True)
