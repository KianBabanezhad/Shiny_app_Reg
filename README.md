# Regression Web Application

## Description
This is a Shiny web application in Python that enables users to upload a CSV file, select X and Y columns, and run polynomial regression analysis with adjustable regression order. The results are displayed in a table and a 2D regression plot.

## Features
- Upload a CSV file containing the dataset.
- Select `X` and `Y` columns from the CSV for regression analysis.
- Adjust the polynomial regression order (1 to 5).
- View data in a tabular format and plot the 2D regression results.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. **Install the Required Libraries**: Ensure you have Python 3 installed, and then install the necessary packages: 
   ```bash
   pip install -r requirements.txt

## Usage
1. **Run the Application**: Start the Shiny application by executing:
   ```bash
   shiny run --reload --launch-browser app_regression.py

2. **Interacting with the App**:

- Upload a CSV file with data.
- Choose the `X` and `Y` columns to use for the regression.
- Select the polynomial order for regression.
- View the table of data and the regression plot in the respective tabs.  

## File Structure
- `app_regression.py` : Main application file containing the web app code.

## Dependencies
- `pandas`
- `plotly`
- `shiny`
- `shinywidgets`
- `matplotlib`
- `seaborn`

This README provides a basic overview of the project, instructions for setup and use, and other relevant information. Let me know if there’s anything specific you’d like to add or modify. Feel free to contribute or reach out if you have any questions!


