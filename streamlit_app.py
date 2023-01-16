import streamlit

streamlit.title('Breakfast Favorites')

streamlit.header('Breakfast Menu')

streamlit.text('Omega 3 & Blueberry Oatmeal ')
streamlit.text('Kale spinach cucumber smoothie')
streamlit.text('Hard boiled egg')
streamlit.text('Avocado Toast ')

streamlit.title('Build your own fruit smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
