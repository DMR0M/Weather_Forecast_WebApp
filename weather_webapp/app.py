import streamlit as st
import plotly.express as px
import backend


st.title('Weather Forecast for the Next Days ')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of days of forecasted days')

option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))

st.subheader(f'{option} for the next {days} day(s) in {place.title()}')

try:
    if place:
        filtered_data = backend.get_data(place, days)

        if option == 'Temperature':
            # Filter the selected data
            temperatures = [float(w_data['main']['temp']) * 0.1 for w_data in filtered_data]
            dates = [date['dt_txt'] for date in filtered_data]

            # Create temperature plot
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if option == 'Sky':
            images = {
                'Clear': 'images/clear.png',
                'Clouds': 'images/cloud.png',
                'Rain': 'images/rain.png',
                'Snow': 'images/snow.png',
            }
            # Create column for each data point
            column_list = [col_1, col_2, col_3, col_4, col_5] =\
                st.columns([0.5, 0.5, 0.5, 0.5, 0.5])

            # Filtered list to get sky conditions from API request
            sky_conditions = [w_data['weather'][0]['main'] for w_data in filtered_data]

            # List of image paths
            image_paths = [images[condition] for condition in sky_conditions]

            for img, sky_condition in zip(image_paths, sky_conditions):
                for col in column_list:
                    with col:
                        st.image(img, width=120)
                        st.text(sky_condition)


except KeyError:
    st.info('Place does not exist')