import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
	iris = load_iris()
	df = pd.DataFrame(iris.data, columns = iris.feature_names)
	df['species'] = iris.target
	return df, iris.target_names


df, target_name = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider('Sepal length', float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))
sepal_width = st.sidebar.slider('Sepal width', float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))
petal_length = st.sidebar.slider('Petal length', float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))
petal_width = st.sidebar.slider('Petal width', float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))

input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=df.columns[:-1])
prediction = model.predict(input_data)
prediction_proba = model.predict_proba(input_data)
prediction_proba_df = pd.DataFrame(prediction_proba, columns=target_name)

st.write(f"Prediction: {target_name[prediction[0]]}")
st.write("Prediction Probability:")
st.dataframe(prediction_proba_df)