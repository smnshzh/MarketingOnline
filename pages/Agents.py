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
            "Agent Inventory":agent_iventory,
            "Agent Sales":agent_sales
            }


    return stx.Router(page)

def agent_iventory():
    if check_password():
        st.write("get agent inventory")
    else:
        pass    
        
def agent_sales():

    if check_password():
        st.write("get agent sales")
        
    else:
        pass    
        

router = init_rout()

navigate = stx.tab_bar(data=[
    stx.TabBarItemData(id=1, title="Agent Inventory",
                       description=""),
    stx.TabBarItemData(id=2, title="Agent Sales",
                       description=""),
], default=1, return_type=int)

# Display the selected route
if navigate == 1:
    agent_iventory()
elif navigate == 2:
    agent_sales()
