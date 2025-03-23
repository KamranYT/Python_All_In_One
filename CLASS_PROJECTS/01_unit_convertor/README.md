# Unit Converter Application

A versatile and user-friendly unit converter built with Streamlit that allows you to convert between various units of measurement. This application provides a simple interface for converting different types of measurements including length, weight, temperature, area, volume, speed, and time.

## Features

- **Multiple Conversion Types:**
  - Length (meters, kilometers, inches, feet, miles, centimeters, millimeters)
  - Weight (grams, kilograms, pounds, ounces, stones, milligrams)
  - Temperature (Celsius, Fahrenheit, Kelvin)
  - Area (square meters, square kilometers, hectares, acres, square feet, square inches)
  - Volume (liters, milliliters, cubic meters, cubic centimeters, gallons, quarts, pints)
  - Speed (meters per second, kilometers per hour, miles per hour, feet per second)
  - Time (seconds, minutes, hours, days)

- **User-Friendly Interface:**
  - Clean and intuitive design
  - Easy-to-use dropdown menus for unit selection
  - Precise conversion results with 6 decimal places
  - Conversion history tracking
  - Option to clear conversion history

## Installation

1. Clone this repository to your local machine
2. Install the required dependencies:
   ```bash
   pip install streamlit
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run main.py
   ```
2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)
3. Select the type of conversion you want to perform
4. Enter the value you want to convert
5. Choose the source unit and target unit
6. Click the "Convert" button to see the result

## Features in Detail

### Length Conversion
Convert between various length units including metric and imperial measurements.

### Weight Conversion
Convert between different weight units, supporting both metric and imperial systems.

### Temperature Conversion
Convert between Celsius, Fahrenheit, and Kelvin temperature scales.

### Area Conversion
Convert between different area units, useful for real estate and construction calculations.

### Volume Conversion
Convert between various volume units, including liquid measurements.

### Speed Conversion
Convert between different speed units, useful for transportation and physics calculations.

### Time Conversion
Convert between different time units, from seconds to days.

## Technical Details

The application is built using:
- Python 3.x
- Streamlit framework
- Session state management for history tracking
- Modular conversion functions for each unit type

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.
