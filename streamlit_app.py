import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents new Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free-Range Egg')
streamlit.text('🥑 🍞 Avocado Toast')

streamlit.header('🍌 🥭 Build Your Own Fruit Smoothie 🥝 🍇')

my_fruits_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruits_list = my_fruits_list.set_index('Fruit')

#let's put a pick list here so they can pick the fruits they want to include
fruits_selected = streamlit.multiselect('Pick some fruits:',list(my_fruits_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruits_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

# creating the reapeatable code block
def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
      return fruityvice_normalized
    
streamlit.header('Fruityvice Fruit Advice')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      stramlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# New section to display fruityvice api response
streamlit.text('What Fruit would you like to add')
fruit_choice_2 = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Thanks for adding', fruit_choice_2)

my_cur.execute("insert into fruit_load_list values('from streamlit')")
