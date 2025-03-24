# BMI Calculator

A simple, interactive Body Mass Index (BMI) calculator built with Streamlit.

## Description

This BMI Calculator is a web application that helps users calculate their Body Mass Index (BMI), a measure of body fat based on height and weight. The application provides an easy-to-use interface with slider inputs and instant BMI calculation.

## Features

- Interactive sliders for height and weight input
- Instant BMI calculation
- Clear display of BMI categories
- User-friendly interface

## BMI Categories

The calculator provides information about different BMI categories:
- **Underweight**: BMI less than 18.5
- **Normal weight**: BMI between 18.5 and 24.9
- **Overweight**: BMI between 25 and 29.9
- **Obesity**: BMI 30 or greater

## How to Use

1. Adjust the height slider to input your height in inches
2. Adjust the weight slider to input your weight in kilograms
3. Click the "Generate BMI" button to calculate your BMI
4. Your BMI result will be displayed instantly

## Technical Details

- Built with Python using Streamlit framework
- Uses pandas for data handling
- Provides real-time BMI calculation

## Formula Used

BMI is calculated using the formula:
weight / ((height/100) ** 2)