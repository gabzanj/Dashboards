import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Survey Results')
st.header('Survey Results 2021!')
st.subheader('Was the tutorial helpful?')

excel_file = r'../survey_results/Survey_Results.xlsx'
sheet_name = 'DATA'
df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='B:D',
                   header=3)

df_participants = pd.read_excel(excel_file,
                                sheet_name=sheet_name,
                                usecols='F:G',
                                header=3)

st.dataframe(df)
st.dataframe(df_participants)

pie_chart = px.pie(df_participants,
                   title='Total Number of Participants',
                   values='Participants',
                   names='Departments')
st.plotly_chart(pie_chart)

image = Image.open('../survey_results/images/survey.jpg')
st.image(image,
         caption='Designed by Slidesgo / Freepik - Coding Is Fun',
         use_column_width=True)
