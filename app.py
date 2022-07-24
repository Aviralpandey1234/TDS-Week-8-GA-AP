import streamlit as st

string = "Division Of Two Numbers"
st.set_page_config(page_title=string, page_icon="➗")


st.title('Division Of Two Numbers')
a = st.number_input('Enter a number')
b = st.number_input('Enter another number')
if b!=0:
    st.write("Result is " + str(a/b))
else:
    st.write("Cant Divide by Zero" )
