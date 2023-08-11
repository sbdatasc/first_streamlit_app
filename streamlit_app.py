import streamlit as st
import pandas as pd
import snowflake.connector
import requests
from urllib.error import URLError

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    # write your own comment -what does the next line do? 
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    # write your own comment - what does this do?
  return fruityvice_normalized
  
  


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
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_function)
    
except URLError as e:
  st.error()
  

st.stop()    
# st.write('The user entered ', fruit_choice)
    

# import requests

#st.text(fruityvice_response.json())

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    my_data_rows = my_cur.fetchall()
    return my_data_rows

if st.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  st.dataframe(my_data_rows)
  
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list_values ('from streamlit)")
    return "Thanks for adding " + new_fruit
add_my_fruit = st.text_input("What fruit would you like to add?")
if st.button('Add a Fruit to the list'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = insert_row_snowflake(add_my_fruit)
  st.dataframe(my_data_rows)
  
  


#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

#my_data_row = my_cur.fetchone()


#st.text("Hello from Snowflake:")
st.text("The fruit load list contains:")
add_my_fruit = st.text_input('What fruit would you like information about?')

str_add_choice = "".join([s for s in add_my_fruit])
st.write('The user entered ', str_add_choice)
#my_data_rows.append(str_add_choice)
st.dataframe(my_data_rows)
st.text("Thanks for adding " + str_add_choice)


