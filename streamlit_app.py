import streamlit
import pandas as pd
import requests

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

# New section to display fruityvice api response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response.json()) # just writes the data to the screen

#take the json version of the response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)
