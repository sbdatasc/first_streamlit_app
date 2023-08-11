import streamlit as st
import pandas as pd
import snowflake.connector


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
fruits_to_show = my_fruit_list.loc[fruits_selected]

st.dataframe(fruits_to_show)

st.header("Fruityvice Fruit Advice!")

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#st.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()

#st.text("Hello from Snowflake:")
st.text("The fruit load list contains:")
add_my_fruit_choice = st.text_input('What fruit would you like information about?')
st.write('The user entered ', add_my_fruit_choice)
my_data_rows.append(add_my_fruit_choice)
st.dataframe(my_data_rows)
st.text("Thanks for adding " + add_my_fruit_choice)

