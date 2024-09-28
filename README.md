# Language Detection App

A simple language detection application that uses a Naive Bayes model and CountVectorizer to predict the language of a given text. The model is trained on multilingual text data and deployed using [Streamlit](https://streamlit.io/).

## Features

- Supports multiple languages.
- Provides instant language prediction for user input text.
- Deployed on Hugging Face Spaces: [Try the app here](https://huggingface.co/spaces/zafermbilen/language-detection)

## Usage

1. Enter any text into the input box.
2. Click "Predict" to see the detected language.

## Project Structure

- `app.py`: Streamlit app for the user interface and predictions.
- `language_detection_model.joblib`: Pre-trained model saved using `joblib`.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation (this file).

## Model

The app utilizes a pipeline consisting of:

- **CountVectorizer**: Converts text into numerical feature vectors.
- **Multinomial Naive Bayes**: A probabilistic model for text classification.

## Live Demo

You can try the application live at Hugging Face Spaces:  
[Language Detection App](https://huggingface.co/spaces/zafermbilen/language-detection)
