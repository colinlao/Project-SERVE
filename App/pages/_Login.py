import streamlit as st
import requests
from Home import set_session_tabs
from st_pages import Page, show_pages, hide_pages

#hide_pages(["Home"])

#st.set_page_config(page_title="Login", page_icon="🏐")
st.sidebar.image("logo.png")
st.sidebar.markdown("<h1 style='text-align: center;'>UW SERVE</h1>", unsafe_allow_html=True)

if 'Login' not in st.session_state:
    st.session_state['Login'] = False

if 'Email' not in st.session_state:
    st.session_state['Email'] = False

if 'Exec' not in st.session_state:
    st.session_state['Exec'] = False

st.title("SERVE Member Login")

with st.form("Form", clear_on_submit=False):
    email = st.text_input("Email")
    if st.form_submit_button("Send Code"):
        res = requests.get("http://127.0.0.1:5000/sendcode?email="+email).json()
        st.write(res["status"])

    password = st.text_input("Code (Sent To Email)")
    if st.form_submit_button("Login with Code"):
        res = requests.get("http://127.0.0.1:5000/checkpassword?password=%s&email=%s"%(password, email)).json()
        if res["status"] == 1:
            st.session_state["Login"] = True
            st.session_state["Email"] = email
            st.session_state["Exec"] = res["exec"] == 1
            st.write("Login Successful!")
        else:
            st.write("Error. Please try again.")

st.warning("Account will be logged out on refresh.")
set_session_tabs()



# https://myaccount.google.com/u/3/apppasswords
# CS338DATABASE!
