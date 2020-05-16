# https://streamlit.io/docs/getting_started.html
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy
import pandas

st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")
st.write(pandas.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

df = pandas.DataFrame({
    'my first column': [1, 2, 3, 4],
    'my second column': [10, 20, 30, 40]
})

df