import streamlit as st
import pandas as pd

st.title("My Parents New Healthy Diner")

st.header("Breakfast Favorites")

st.text(" 🥣 Omega 3 & Blueberry Oatmeal")
st.text(" 🥗 Kale , Spinach & Rocket Smoothie")
st.text(" 🐔 Hard-Boiled Free-Range Egg")
st.text(" 🥑🍞 Avacado Toast")


st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# display the table on the page and allow user to select fruits
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list[fruits_selected]

st.dataframe(fruits_to_show)
