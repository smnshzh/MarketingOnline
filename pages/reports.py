import streamlit as st
import pymysql
from setting import db_params_mysql as dpm
from moduals.ssoLogin import check_password

if check_password():
    connection = pymysql.Connect(
                host=dpm["host"],
                user=dpm['user'],
                password=dpm['password'],
                database=dpm['database']
            )

    # Create a cursor object
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM marketing.imagegather")
    results = cursor.fetchall()
    # Process the results
    for row in results:
        st.write(row)