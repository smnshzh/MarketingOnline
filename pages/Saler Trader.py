import streamlit as st
import os
import pymysql
from setting import db_params_mysql as dpm
from db_connector.db import connect_to_db
from moduals.ssoLogin import check_password
import extra_streamlit_components as stx

@st.cache_resource(hash_funcs={"_thread.RlLock":lambda _:None})
def init_rout():
    page = {   
            "Pricing":price_survayer,
            "Shelfing":shelf_survayer
            }


    return stx.Router(page)

def price_survayer():
    if check_password():
        st.title("Marketing Online")
        st.write("Data Gathering")
        
        with st.form("get data", clear_on_submit=True):
            image_files = st.file_uploader(type=["png", "jpg"], label="Image", accept_multiple_files=False, key="img")
            name = st.text_input(label="Customer Code", placeholder="Leave blank if you don't know", key="name")
            buy_price = st.number_input(label="Buy Price", key="bp")
            sale_price = st.number_input(label="Sell Price", key="sp")
            description = st.text_area(label="Description", key="dsc")

            items = {
                "images": image_files,
                "name": name,
                "bp": buy_price,
                "sp": sale_price,
                "dsc": description
            }

            if st.form_submit_button("Enter"):
                # Create a database connection
                connection = connect_to_db()
                
                # Create a cursor object
                cursor = connection.cursor()

                if not items["images"]:
                    st.warning("No Image")
                elif items["name"] and items["bp"] and items["sp"]:
                    # Save the image to the uploads directory
                    image_path = os.path.join("uploads", items["images"].name)
                    with open(image_path, "wb") as f:
                        f.write(items["images"].getbuffer())
                    items["images"] = image_path

                    # Use parameterized queries to avoid SQL injection
                    query = "INSERT INTO imagegather (name, image, buyPrice, salePrice, description) VALUES (%s, %s, %s, %s, %s)"
                    values = (str(items['name']), items['images'], float(items['bp']), float(items['sp']), items['dsc'])

                    cursor.execute(query, values)
                    connection.commit()
                    st.success("Saved")
                    
                else:
                    st.warning("All Fields Required")

                # Close the cursor and connection
                cursor.close()
                connection.close()

    else:
        pass    
        
def shelf_survayer():

    if check_password():
        st.title("Marketing Online")
        st.write("Data Gathering")
        
        with st.form("get data", clear_on_submit=True):
            image_files = st.file_uploader(type=["png", "jpg"], label="Image", accept_multiple_files=False, key="img")
            name = st.text_input(label="Customer Name", placeholder="Leave blank if you don't know", key="name")
            code = st.text_input(label="Customer Code", key="bp")
            loc = st.text_input(label="Location", key="loc")
            description = st.text_area(label="Description", key="dsc")

            items = {
                "images": image_files,
                "name": name,
                "code": code,
                "loc": loc,
                "dsc": description
            }

            if st.form_submit_button("Enter"):
                # Create a database connection
                connection = connect_to_db()
                
                # Create a cursor object
                cursor = connection.cursor()

                if not items["images"]:
                    st.warning("No Image")
                elif items["name"] and items["bp"] and items["sp"]:
                    # Save the image to the uploads directory
                    image_path = os.path.join("uploads", items["images"].name)
                    with open(image_path, "wb") as f:
                        f.write(items["images"].getbuffer())
                    items["images"] = image_path

                    # Use parameterized queries to avoid SQL injection
                    query = "INSERT INTO shelfgathering (customer_name, customer_id,img_path,loc,description) VALUES (%s, %s, %s, %s, %s)"
                    values = (str(items['name']), items['code'], items['images'], items['loc'], items['dsc'])

                    cursor.execute(query, values)
                    connection.commit()
                    st.success("Saved")
                    
                else:
                    st.warning("All Fields Required")

                # Close the cursor and connection
                cursor.close()
                connection.close()

    else:
        pass    
        

router = init_rout()

navigate = stx.tab_bar(data=[
    stx.TabBarItemData(id=1, title="Price Gathering",
                       description="FOR COMPANY"),
    stx.TabBarItemData(id=2, title="Shelf Gathering",
                       description="FOR CUSTOMERS"),
], default=1, return_type=int)

# Display the selected route
if navigate == 1:
    price_survayer()
elif navigate == 2:
    shelf_survayer()




