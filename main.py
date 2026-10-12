import streamlit as st

st.title("Hello Chai App")

st.subheader("Brewed with streamlit")

st.text("Welcome to first interactive app")

st.write("Choose your favorite variety of chai")

chai = st.selectbox("Your favorite chai:", ["Masala chai", "Lemon chai", "Adrak Chai", "Kesar Chai"])

st.write(f"You choose {chai}. Excellent choice!")

st.success("Your chai has been brewed")