import streamlit as st
st.title(":red[HEllO EVERYONE] :sunglasses:")
st.header("I am :blue[Richa Sharma].:green[Welcome and thank you for visiting my initial web application.]")

st.subheader("I have created a Streamlit application to visualize and analyze the Diabetes dataset.")
st.markdown("This app allows to generate various types of plots and enable exploration and analysis of datasets through visualization.")
st.caption("please navigate to the next page to find out the details of dataset, we are working on .")
st.subheader("You can connect with me through :handshake::")

link= st.button('Linkedin')
github= st.button('Github')
if link == True:
    st.markdown('https://www.linkedin.com/in/richa-sharma-71903b224/')
elif github == True:
    st.markdown('https://github.com/richasharma-19')

st.markdown(' Thanks :red[Kanav Bansal] and :red[Innomatics Research Labs] for this oppurtunity')
st.balloons()

