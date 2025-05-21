# Weather API and Visualization

## Overview
This repository contains the deliverables for Task 1 of the CODTECH Python Internship. The script fetches weather data from the OpenWeatherMap API for a user-specified city and creates a bar plot using Matplotlib.

## Files
- **Script**: `task1_weather_api.py`
- **Output**: `weather_visualization.png`
- **Description**: The script prompts for a city name, fetches weather data (temperature, humidity, wind speed), and generates a bar plot saved as `weather_visualization.png`.

## How to Run
1. Install dependencies: `pip install requests matplotlib`
2. Replace `API_KEY` in `task1_weather_api.py` with a valid OpenWeatherMap API key.
3. Run the script: `python task1_weather_api.py`
4. Enter a city name (e.g., `Guntur`, `Visakhapatnam`) when prompted.
5. The script will display weather details and save a visualization as `weather_visualization.png`.

## Notes
- Ensure you have a valid OpenWeatherMap API key.
- The visualization includes temperature (°C), humidity (%), and wind speed (m/s).
