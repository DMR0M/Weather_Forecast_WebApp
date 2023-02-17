import streamlit as st
import plotly.express as px
from datetime import date, timedelta
from backend import get_data

DATE_NOW = date.today()


st.title('Weather Forecast for the Next Days ')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of days of forecasted days')

option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))


def create_data():
    dates = [DATE_NOW + timedelta(days=i) for i in range(5)]
    temperatures = [25, 24, 27, 23, 24]
    return dates, temperatures


st.subheader(f'{option} for the next {days} days in {place}')

d, t = create_data()
figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)

