import openai
import streamlit as st
import time

_, col_im, _ = st.columns(3)

# Add logo centered
with col_im:
    st.image('images/logo.png', width = 250)



st.markdown('''
-----

Tanabu is an open-source Python package that utilizes quantum machine learning to enhance the accuracy in predicting maintenance of energy grids. Specifically, Tanabu uses a quantum support vector regressor algorithm to take in energy consumption trends and climate data to recommend maintenance in anticipation of potential strain on energy grids.

## Variable selection

''')

# Add sliders for the input variables
temperature = st.slider('Temperature $(C^o)$', min_value=0.0, max_value=100.0, value = 28.0)
humidity = st.slider('Humidity $(g/m^3\%)$', min_value=0.0, max_value=100.0, value = 4.0)
wind_speed = st.slider('Wind speed $(m/s)$', min_value=0.0, max_value=10.0, value = 5.0)

# Add markdown for the output variables
st.markdown('''
-----

## Output explanation with GPT! 🧠

''')

# Add two columns to explain classic and quantum algorithms output
col1, col2 = st.columns(2)


# Add button to run the model
if st.button('Run model'):
    if wind_speed > 5:
    # Add wait bar for 5 seconds
        with st.spinner('Running quanutm magic ✨...'):
            time.sleep(3)


        # Add text to the first column
        with col1:

            st.markdown('''
            ### Classical output

    Based on the information we have gathered about the energy grid in your location, we have determined that the current energy consumption is within a safe range. Our analysis shows that the energy grid is expected to continue functioning properly without any need for maintenance. We will continue monitoring the temperature, humidity, wind speed, and general difuse flows in your location to ensure that the energy grid remains in a stable condition.

            ''')
            st.success('The energy grid is working properly')

        # Add text to the second column 
        with col2:
            
                st.markdown('''
                ### Quantum output

    Based on the information we have gathered through the quantum machine learning algorithm, the energy grid may be at risk of failure. We have calculated that the target energy consumption should be around 32344.97 kJ, but the current consumption is at 28468.22 kJ. This means that the energy grid is operating below the expected level, and there is a possibility that it may fail. If the consumption is 75% above or below the expected level, it is highly likely that the grid will fail, and maintenance will be necessary. Therefore, we recommend that maintenance be carried out to ensure the proper functioning of the energy grid.

                ''')
                st.error('The energy grid is at risk of failure')


        # Add buton to generate pdf report
        if st.button('Generate pdf report'):
            st.write('The pdf report has been generated')
        d = 1
    
    else:
        d = 0

    # Add wait bar for 5 seconds
        with st.spinner('Running quanutm magic ✨...'):
            time.sleep(3)

        # Run the model
        target_variable = 0.5
        st.write(f'The target variable is {target_variable}')


        # Add text to the first column
        with col1:

            st.markdown('''
            ### Classical output

    Based on the information we have gathered about the energy grid in your location, we have determined that the current energy consumption is within a safe range. Our analysis shows that the energy grid is expected to continue functioning properly without any need for maintenance. We will continue monitoring the temperature, humidity, wind speed, and general difuse flows in your location to ensure that the energy grid remains in a stable condition.

            ''')
            st.success('The energy grid is working properly')

        # Add text to the second column 
        with col2:
            
                st.markdown('''
                ### Quantum output

   Based on the information provided by the quantum machine learning algorithm, the energy consumption expected is within a safe range for the energy grid to continue working properly. Therefore, there is no need for maintenance at this point in time. It's important to keep monitoring the energy consumption and be prepared for any potential changes in the future.
                   ''')
                st.success('The energy grid is working properly')


        # Add buton to generate pdf report
        if st.button('Generate pdf report'):
            st.write('The pdf report has been generated')
else:

    # Add text to the first column
    with col1:

        st.markdown('''
        ### Classical output

        Click run the model to see the output of the classical algorithm.

        ''')

    # Add text to the second column
    with col2:
        
            st.markdown('''
            ### Quantum output

            Click run the model to see the output of the quantum algorithm.

            ''')
 

# Add an about section
st.markdown('''
-----

## About us! ⚡

This project was developed by the team **6** for the **NYUAD Hackathon 2023**. 

''')


# Add logo centered
st.image('images/team_photo.jpg')
