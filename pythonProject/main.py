import streamlit as st

from BetWebsite.auth import sign_up, login

st.title("Welcome to BetNetGoal")

menu = ["Home", "Login", "SignUp", "Bet"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "SignUp":
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_email = st.text_input("Email")
    new_password = st.text_input("Password", type='password')

    if st.button("SignUp"):
        sign_up(new_user, new_email, new_password)
        st.success("Account created successfully!")

elif choice == "Login":
    st.subheader("Login Section")
    username = st.text_input("User Name")
    password = st.text_input("Password",type='password')

    if st.button("Login"):
        if login(username, password):
            st.success("Logged In as {}".format(username))
        else:
            st.warning("Incorrect Username/Password")

elif choice == "Home":
    st.subheader("Home")
    st.write("Welcome to BetNetGoal")
    st.write("You can login or sign up from the sidebar")
    st.write("If you don't have an account, please sign up")
    st.write("If you already have an account, please login")
    st.write("Enjoy!")

elif choice == "Bet":
    st.subheader("Bet")
    st.write("Welcome to the Bet page")
    st.write("Here you can bet on the matches of the English Premier League")
    st.write("Good Luck!")