import streamlit as st
from traloi import translate

st.title("Demo trả lời câu hỏi")
name = st.text_input('Nhập câu hỏi')

if not name:
  st.warning('Vui lòng nhập câu hỏi')
  st.stop()

rs= translate(name)
st.success(rs.replace('_',' '))