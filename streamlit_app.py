import streamlit

streamlit.title('My Mom\'s new healthy Diner')
streamlit.header('Breakfast Favorites') 
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)
streamlit.dataframe(my_fruit_list)

# New section to display fruitvice api response

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

# New section to display fruitvice api response
streamlit.header('fruiytvice fruit advice!')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# Take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#output it the screen as a table
streamlit.dataframe(fruityvice_normalized)
