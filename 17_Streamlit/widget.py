import streamlit as st
import pandas as pd

st.title("Exploring Widgets")

name = st.text_input("Enter you name")

age = st.slider("Select your age:",0,100,25)

st.write("You age is:",age)



options = ["C", "C++", "Java", "Python"]
choose = st.selectbox("Choose your Favorite Programming Language", options)
st.write(f"You Selected {choose}")

if name:
    st.write("Hello",name) 

df = pd.read_csv('sales_data.csv')
st.write(df.head())

st.subheader("Plot of Date vs Unit Sold")
st.bar_chart(data=df,x='Date',x_label="Dates",y="Units Sold", y_label="Units Sold")

# Upload file
uploaded_file = st.file_uploader("Upload a CSV file: ",type='csv')

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)
    st.write(df1)