import streamlit as st
st.title("How to use the crop recommendation system")
st.write("1.Enter the required")
col1, col2 = st.columns(2)

original = Image.open(image)
col1.header("Original")
col1.image(original, use_column_width=True)