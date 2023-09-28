import streamlit as st
import pymysql
import hashlib
from db_connector.db import connect_to_db
from setting import db_params_mysql as dpm
import extra_streamlit_components as stx
import jwt
import datetime
from datetime import timedelta




# this function will create the token
# for particular data
def create_access_token(data: dict):
    
    to_encode = data.copy()
    SECRET_KEY='3d032dd24ebcf44630f80cbb616cdcce957a68f5b3756deda067ddc7bd5dfb95'
    # expire time of the token
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
     
    # return the generated token
    return encoded_jwt
# تابع برای ذخیره نام کاربری و رمز عبور در دیتابیس
def save_credentials(username, password):
    try:
        cnx = connect_to_db()
        connection = cnx
        with connection.cursor() as cursor:
            insert_query = "INSERT INTO user (username, password) VALUES (%s, %s)"
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute(insert_query, (username, hashed_password))
        connection.commit()
        st.success("User credentials saved successfully.")
    except Exception as e:
        st.error(f"Error: {str(e)}")
    finally:
        cnx.close()    

# تابع برای بررسی تایید هویت
def check_password():
    cookie = stx.CookieManager(key="MainCookie")  
    cnx = connect_to_db()
    connection = cnx
    # تابع برای اعتبارسنجی نام کاربری و رمز عبور
    def validate_credentials(username, password):
        try:
            with connection.cursor() as cursor:
                # جستجو در دیتابیس برای نام کاربری و رمز عبور
                select_query = "SELECT * FROM user WHERE username = %s AND password = %s"
                cursor.execute(select_query, (username, password))
                user_data = cursor.fetchone()
                if user_data:
                    return True
                else:
                    return False
        except Exception as e:
            st.error(f"Error: {str(e)}")
        finally:
            connection.close()


    if not cookie.get(cookie="autherized"):
        # First run or previous login attempt failed, show inputs for username + password.
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            # هش کردن رمز عبور
            hashed_password = hashlib.sha256(password.encode()).hexdigest()   
            # اعتبارسنجی نام کاربری و رمز عبور
            if validate_credentials(username, hashed_password):
                cookie.set("autherized", True,key="set_autherized")
                cookie.set("username",username,key="set_username")
                print("loged in")
                st.success("😀 Login successful.")
                return True
                
            else:
                st.error("😕 User not known or password incorrect")

    else:
        # User is already logged in.
        st.success(f"Welcome  {stx.CookieManager().cookies.get('username')}")
        
        log_out = st.sidebar.button("log out",key="logOut")
        if log_out :
            cookie.set("autherized",False,key="set_false")
            cookie.set("username",None)
        return True
