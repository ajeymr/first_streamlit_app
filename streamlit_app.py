import streamlit
import pandas as pd

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
streamlit.multiselect('Pick some fruits:',list(my_fruits_list.index))

#display the table on the page
streamlit.dataframe(my_fruits_list)
