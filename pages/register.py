import streamlit as st
import hashlib
from moduals.ssoLogin import save_credentials

# اصلی
st.title("User Registration Form")
# ورودی‌های مربوط به ثبت نام
username = st.text_input("Username")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Register"):
    # بررسی معتبر بودن رمز عبور
    if password == confirm_password:
        

        # ذخیره نام کاربری و رمز عبور در دیتابیس
        save_credentials( username, password)
        
    else:
        st.error("Passwords do not match. Please try again.")