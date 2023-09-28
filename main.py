import streamlit as st
import extra_streamlit_components as stx
from geopy import Nominatim
from streamlit.components.v1 import html

# Define a function to load and run JavaScript code


# Create a button to request location
if st.button("Get My Location"):
    
    
    # Run the JavaScript code
    def run_js_code(js_code):
        html(js_code)
    js_code = """

    <script>
    if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
    document.getElementById("demo").innerHTML =
    "Geolocation is not supported by this browser.";
    }

    function showPosition(position) {
    alert('posiosion geted')
    document.getElementById("demo").innerHTML =
    'Latitude: ' + position.coords.latitude + '<br>' +
    'Longitude: ' + position.coords.longitude;
    }
    </script>
          """
    
    st.markdown(js_code, unsafe_allow_html=True)   
    
    


@st.cache_resource(hash_funcs={"_thread.RlLock":lambda _:None})
def init_rout():
    page = {   
            "/home":home,
            "/outside":outside
            }


    return stx.Router(page)

def home():
    
    return st.write("this is home")

def outside():
    return st.write("this is outside")

router = init_rout()

st.sidebar.title("Navigation")
selected_route = st.sidebar.radio("Go to", ["home", "outside"])
# Create a top navigation menu


if selected_route == "home":
    home()

elif selected_route == "outside":
    outside()


    
    

