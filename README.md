# Github-Copilot-Hackathon-
# Weather Forecasting Tool
## Introduction
The Weather Forecasting Tool is a simple Python program that retrieves weather information for a specified city using the OpenWeatherMap API. This project was developed as part of the Microsoft GitHub Hackathon, with the assistance of GitHub Copilot—a powerful AI-powered code completion tool developed by OpenAI and GitHub.

## Features
- Fetches current weather data for a specified city.
- Displays temperature in Kelvin unit.
- Provides atmospheric pressure in hPa unit.
- Shows humidity as a percentage.
- Retrieves a brief description of the weather conditions.

## Prerequisites
- Python installed
- Requests library (`pip install requests`)

## Usage
1. Clone the repository or download the `WeatherForecast.py` file.
2. Open a terminal or command prompt and navigate to the directory where the `WeatherForecast.py` file is located.
3. Run the following command to execute the program:
4. Enter the name of the city for which you want to retrieve weather information when prompted.

## Example Output
```city_name: London
{
"coord": {
"lon": -0.1257,
"lat": 51.5085
},
"weather": [
{
"id": 801,
"main": "Clouds",
"description": "few clouds",
"icon": "02d"
}
],
"base": "stations",
"main": {
"temp": 288.09,
"feels_like": 287.45,
"temp_min": 286.23,
"temp_max": 289.85,
"pressure": 1017,
"humidity": 73
},
}
