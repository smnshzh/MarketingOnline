import streamlit as st
import pymysql
from setting import db_params_mysql as dpm
from moduals.ssoLogin import check_password
import os
from db_connector.db import connect_to_db
st.write(os.listdir())
 
 # Create a cursor object
cursor = connect_to_db().cursor()

cursor.execute("SELECT * FROM imagegather")
results = cursor.fetchall()
# Process the results
col1 , col2 , col3 = st.columns(3)
i = 1
for row in results:
    if i % 3 ==0 :
        with col3:
            st.header(row[0])
            st.image(row[1])
    elif i% 2 ==0:
        with col3:
            st.header(row[0])
            st.image(row[1])
    else:
        with col1:
            st.header(row[0])
            st.image(row[1])
   