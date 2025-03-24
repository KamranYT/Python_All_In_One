# Plot Data Sweeper

A simple yet powerful data visualization dashboard built with Streamlit that allows users to explore and visualize CSV data interactively.

## Features

- **File Upload**: Supports CSV file upload for data analysis
- **Data Preview**: Shows the first few rows of the uploaded dataset
- **Data Summary**: Displays statistical summary of the numerical columns
- **Interactive Filtering**: Filter data based on any column and value
- **Data Visualization**: Generate line plots with customizable x and y axes

## Requirements

- Python 3.x
- Streamlit
- Pandas

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/plot-data-sweeper.git
cd plot-data-sweeper
```

2. Install the required packages:
```bash
pip install streamlit pandas
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Upload a CSV file using the file uploader

4. Explore your data using the various features:
   - View data preview and summary statistics
   - Filter data by selecting specific columns and values
   - Create line plots by selecting x and y axes

## How It Works

The application provides a user-friendly interface for data analysis and visualization:

1. Users can upload any CSV file through the interface
2. The app displays a preview of the data and basic statistical information
3. Users can filter the data by selecting specific columns and values
4. The filtered data can be visualized using line plots with user-selected axes

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
