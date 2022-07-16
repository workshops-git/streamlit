import streamlit as st
import pandas as pd
import numpy as np

st.title("streamlit")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df

st.write("same as")
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame(
    {
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    }
))

dataframe = pd.DataFrame(
    np.random.randn(10,15),
    columns = (f"col: {i}" for i in range(15))
)


st.table(dataframe)

st.line_chart(dataframe)

c1, c2 = st.columns(2)

with c1:
    option=st.selectbox(
        "wtf ??",
        ["1","2","**","--"]
    )

with c2:
    breakpoint()
    " the value is :" , option
    if option != "1":
        st.write("not one")
    else:
        st.write("one")

