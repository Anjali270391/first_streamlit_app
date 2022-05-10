import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Mom\'s new healthy Diner')
streamlit.header('Breakfast Favorites') 
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)
streamlit.dataframe(my_fruit_list)

# New section to display fruitvice api response
#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

# New section to display fruitvice api response
streamlit.header('fruiytvice fruit advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
    
except URLError as e:
    streamlit.error()
    
    
#streamlit.write('The user entered', fruit_choice)

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# Take the json version of the response and normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#output it the screen as a table changed:
#streamlit.dataframe(fruityvice_normalized)

# don't run anything past here while we troubleshoot
streamlit.stop()

#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("Fruit_load_list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
streamlit.write('Thanks for adding',add_my_fruit)
# This will not work correctly, but go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
