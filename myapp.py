import streamlit as st
import pandas as pd

#sc = StatsCan("https://github.com/KevinJCbed/gdplookup/blob/main/stats_can.h5")

# st.image("https://github.com/KevinJCbed/gdplookup/blob/main/logo.png",
#          use_column_width=True)

df = pd.read_csv(
    "https://raw.githubusercontent.com/KevinJCbed/gdplookup/main/data.csv")

st.dataframe(df.head())
# df['Year'] = df.REF_DATE.astype(str).str[:4]

# prices_selection = st.sidebar.selectbox(
#     "What prices?",
#     df['Prices'].unique().tolist()
# )

# sa_selection = st.sidebar.selectbox(
#     "What seasonal adjustment?",
#     df['Seasonal adjustment'].unique().tolist()
# )


# estimate_selection = st.sidebar.selectbox(
#     "What GDP component?",
#     df.Estimates.unique().tolist()
# )

# df = df.groupby(['Year', 'Estimates', 'Prices',
#                 'Seasonal adjustment']).VALUE.sum().reset_index()

# st.title(f"{estimate_selection},{prices_selection},{sa_selection}")
# st.dataframe(df.query(
#     "`Prices` == @prices_selection & `Seasonal adjustment` == @sa_selection & `Estimates` == @estimate_selection")[['Year', 'VALUE']])
# st.caption("""
#            Data: Statistics Canada,
#            *2021 data not complete
#            """)

# st.balloons()
