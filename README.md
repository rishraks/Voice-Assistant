# Tess - Personal Voice Assistant

Tess is a personal voice assistant built entirely in Python. It is compatible with Python version 3.3 and above, providing an intuitive interface for users to interact through voice commands.

## Features

- **Voice Commands:** Perform various tasks by simply speaking commands.
- **Google Search:** Initiate web searches with phrases like "search for [query]."
- **Greeting Messages:** Tess greets you based on the time of day with random messages.
- **Mathematical Calculations:** Execute complex calculations effortlessly.
- **Weather Forecasts:** Get real-time weather updates and forecasts.
- **Word Definitions:** Retrieve meanings of words through voice queries.
- **Memory Functionality:** Tess can remember personal information like your name or birthday. Retrieve stored information with the command "what do you know."

## Modules Used

- **pyttsx3:** Text-to-speech conversion.
- **speech_recognition:** Speech-to-text functionality.
- **pyaudio:** Capturing audio input from the microphone.
- **wikipedia:** Accessing Wikipedia for information.
- **datetime:** Handling date and time functionalities.
- **webbrowser:** Performing web searches and opening websites.
- **os:** Interacting with the operating system.
- **wolframalpha:** For mathematical calculations, definitions, and weather forecasts.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rishraks/Voice-Assistant.git
   cd Voice-Assistant
   ```
2. Install required packages:
   ```bash
   pip install pyttsx3 SpeechRecognition pyaudio wikipedia-api wolframalpha
   ```
3. Run the application:
   ```bash
   python tess.py
   ```

## Usage  
  Simply run the application and speak commands to Tess. The assistant will respond based on your input, making it a powerful tool for everyday tasks and inquiries.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
