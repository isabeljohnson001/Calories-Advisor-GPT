# NutriBot - Nutritional Analysis App

NutriBot is an innovative web application designed to provide expert nutritional advice based on meal images. It integrates Streamlit for the web interface and leverages Google's generative AI model, Gemini Pro Vision, to analyze the nutritional content of meals from images. This application aims to assist users in making informed dietary choices by identifying whether a meal is healthy or unhealthy based on its nutritional composition.

## Features

- **Image Upload:** Users can upload images of their meals in JPEG or PNG formats.
- **Nutritional Analysis:** The app analyzes the uploaded meal image and provides a detailed nutritional summary, including total calories, percentages of protein, fat, carbohydrates, and fiber.
- **Health Assessment:** Based on the nutritional analysis, the app categorizes the meal as either "Healthy" or "Unhealthy" for individuals aiming to lose weight.
- **Interactive Chat:** Users can interact with NutriBot through a chat interface, where they can submit meal descriptions and receive tailored nutritional advice.

## Technologies Used

- **Streamlit:** For creating the web interface.
- **Pillow (PIL):** For image processing.
- **Google Generative AI (Gemini Pro Vision):** For conducting image-based nutritional analysis.
- **dotenv:** For managing environment variables.
 
## Installation

To run NutriBot locally, you will need Python installed on your machine. Follow these steps:

1. Clone the repository

2. Install dependencies

```
pip install -r requirements.txt
```

3. Set up environment variables:
 Create a `.env` file in the root directory.Get the api keys from https://ai.google.dev/ and add the below line

```
GOOGLE_API_KEY=your_google_api_key_here
```

4. Run the application:
```
streamlit run app.py
```
## Results


