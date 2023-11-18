import pickle
import streamlit as st

model = pickle.load(open('model.pkl','rb'))

st.title("Optimal Path Recognition")

x1 = st.slider("Enter Wagon Weight in Ton",500,1500)

x2 = st.slider("Enter Cargo Weight in Ton",400,1600)

x3 = st.slider('Enter Minimum Distance',100,3000)

x4 = st.slider('Enter Distance Option',2,5)


if st.button("Check"):
    x = model.predict([[x1,x2,x3,x4]])[0][0]
    st.subheader(x)
    if x > 0.6:
        st.success("YES")
    else:
        st.error("NO")
