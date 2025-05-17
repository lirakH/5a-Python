"""
Streamlit layouts and containers 


Ways you can organize your app:
1.  Using Columns
2.  Using Containers 
3.  Using Sidebar 
4.  Using Forms
5.  Using tabs 


1.
st.columns(spec,gap="small",vertica_aligment="top")

spec - number of columns and width


2.
st.container(height=None,border=True)

3.
st.sidebar.funksioni()

funksioni - mund te jet header() write() selectbox() etj


4.
st.form(key, clear_on_submit=True, border=True)

Forms in Streamlit have a few constraints: 
● Every form should contain the st.form_submit_button.
The st.button and st.download_button cannot be added
to a form. 

● Forms can't be integrated inside other forms, but they
can display anywhere in your program (sidebar, columns,
etc.). 


5.
st.tabs(tabs)

tabs - list of str - each str is name of tab


"""


