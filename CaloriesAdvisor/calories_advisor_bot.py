import streamlit as st
from PIL import Image
import base64
import io
import os
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime
import shutil
from datetime import timedelta

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")

# Main application
def main():
    st.set_page_config(page_title="Nutritional Advisor")
    st.header("NutriBot")

    # Initialize chat_history if it's not already in the session state
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    
    with st.form(key='user_input_form'):
        input_text = st.text_input("Input: ", key="input_text")
        uploaded_file = st.file_uploader("Choose an image..", type=["jpeg", "png", "jpg"], key="uploaded_file")
        submit_button = st.form_submit_button("Analyze the Meal")

    if submit_button and uploaded_file and input_text:
        process_input(input_text, uploaded_file)
    elif submit_button:
        st.error("Please provide both an image and a description.")

def process_input(input_text, uploaded_file):
    st.image(st.session_state['uploaded_file'], caption="Uploaded Image", use_column_width=False,width=300)
    image = Image.open(uploaded_file)
    image_bytes = encode_image(image)
    
    # Instruction prompt for the model
    input_prompt = """
    Your role as an expert nutritionist involves conducting a detailed analysis of a meal from an image.
    Based on the nutritional summary of the meal based on the image identify this food as healthy or unhealthy. 
    Include only the below items as the response line by line:
    -Total calories
    -Protein X%, fat X%, carbohydrates X%, and fiber X%. 
    -End with a single statement on whether the meal is 'Healthy' or 'Unhealthy' for someone trying to lose weight."
    """
    
    bot_response = get_response(input_prompt, image_bytes, input_text)
    # Append user input along with the timestamp to chat history
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state['chat_history'].append(("NutriBot", bot_response,current_time))
    st.session_state['chat_history'].append(("User", input_text,current_time))
    

    # Display the chat history
    display_chat_history()

            
# Function to encode an image to base64
def encode_image(image):
     buffer = io.BytesIO()
     image_format = image.format
     image.save(buffer, format=image_format if image_format else 'JPEG')
     encoded_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
     return encoded_image

# Function to highlight specific words in the chat
def highlight_words(text, word_to_color):
    for word, color in word_to_color.items():
        text = text.replace(word, f'<span style="background-color:{color}; color:white; padding:0.3em;">{word}</span>')
    return text


# Keywords to highlight in the chatbot response
words_to_highlight = {
    "Healthy": "green",
    "Unhealthy": "red",
}

# Function to get a response from the model using provided content
def get_response(prompt, image_data, question):
    content = {
        "parts": [
            {"text": prompt},
            {"inline_data": {
                "mime_type": "image/jpeg",
                "data": image_data
            }},
            {"text": question}
        ]
    }
    response = model.generate_content(content)
    return response.text

# Function to display the chat history
def display_chat_history():
    for index, (speaker, text, timestamp) in reversed(list(enumerate(st.session_state['chat_history']))):
       
        key = f"{speaker}_{index}_{timestamp.replace(':', '').replace('-', '').replace(' ', '')}"

        if speaker == "NutriBot":
            highlighted_text = highlight_words(text, words_to_highlight)
            st.markdown(f"{timestamp} - {speaker} response:\n {highlighted_text}", unsafe_allow_html=True)
        else:
            st.text_area(f"{timestamp} - {speaker} said:", value=text, height=100, disabled=True, key=key)
         
if __name__ == "__main__":
    main()
