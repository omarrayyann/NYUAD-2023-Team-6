import openai
import streamlit as st

def create_promt(target_variable):
    text = f"""
    You are an expert in SDG 7 (about energy), quantum computing and energy grids.

    There is a quantum machine learning algorithm which gives you a variable called target_variable,
    which is a good predictor for failures in the energy grid.

    The target variable is a number between 0 and 1. The threshold for failure is 0.5. If the target_variable
    is higher than 0.5, the energy grid will probably fail, and maintenance is needed. Otherwise, the energy grid
    is probably going to keep working properly.

    The algorithm takes as input temperature, humidity, wind speed, and general difuse flows in a
    given location.

    The current target_variable is {target_variable}. Based on this, should we do maintenance?
    Explain your answer step by step, making use of the information given above.

    Do not repeat the information given above, but use it to explain your answer.
    """
    return text

# Get the target variable from the user (float input)
target_variable = st.number_input('Target variable', min_value=0.0, max_value=1.0, value = 0.5)

# Recieve OPENAI API key from the user
openai.api_key = st.text_input('OpenAI API key')

# Add button to generate the answer
if st.button('Generate answer'):
    prompt = create_promt(target_variable)

    # Refine the image description using ChatGPT 4
    def get_answer(prompt):
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": str(prompt)}
        ],
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.8,
        )
        return response.choices[0]

    answer = get_answer(prompt)
    text = answer["message"]["content"]

    # Show the answer as quote
    st.markdown(f'> {text}')

else:
    st.write('Click the button to generate the answer')
