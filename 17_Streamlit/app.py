import streamlit as st
import pandas as pd
import numpy as np


## Title of the Application
st.title("Welcome Everyone! Myself Thanu Prasad.D")

# Display simple Text
st.write("This the a simple text.")

# create a simple dataframe
df = pd.DataFrame({
    'First Column': [1,2,3,4,5],
    'Second Column': [10,20,20,35,40]
})

## Display the dataframe
st.write("Here is the Datafram:")
st.write(df)

## Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.subheader("Line Chart")
st.line_chart(
    chart_data,
    x_label='Row Data',
    y_label="Column Data"
    )
