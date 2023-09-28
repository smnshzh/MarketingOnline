import streamlit as st
import pymysql
from setting import db_params_mysql as dpm
from moduals.ssoLogin import check_password
from db_connector.db import connect_to_db

 
 # Create a cursor object
cursor = connect_to_db().cursor()

cursor.execute("SELECT * FROM imagegather")
results = cursor.fetchall()
# Process the results
for row in results:
    st.write(row)
   