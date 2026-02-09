Project Overview

This project was developed as part of a data engineering and visualization assessment for Soul Foods, a fictional food company. The goal was to process transaction data for their Pink Morsels product line, build an interactive dashboard to visualize sales trends, and implement automated testing for continuous integration.

The solution answers the key business question:
“Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?”

Tasks Completed

1. Environment Setup & Repository Initialization
   
-Forked and cloned the starter repository from vagabond-systems/quantium-starter-repo.

-Set up a Python virtual environment using Python 3.14.3 (compatible with the project requirements).

Installed required dependencies:

-dash, pandas, plotly, pytest, selenium, webdriver-manager, and dash[testing].

2. Data Processing & Cleaning
   
Script: process_sales.py

Input: Three raw CSV files (daily_sales_data_0.csv, daily_sales_data_1.csv, daily_sales_data_2.csv) located in the data/ folder.

Processing Steps:

-Filtered rows to keep only Pink Morsels transactions.

-Cleaned the price column (removed $ symbols and redundant values).

-Created a sales column by multiplying quantity and price.

-Extracted only the required columns: sales, date, region.

-Merged data from all three files into a single cleaned dataset.

-Output: final_sales.csv – a consolidated, cleaned dataset ready for visualization.

<img width="1920" height="1036" alt="Screenshot (591)" src="https://github.com/user-attachments/assets/b96320a4-a924-40d6-88b6-e7adcb5d489e" />


3. Interactive Dashboard Development
   
Script: app.py (Dash application)

Features:

-Header: “Pink Morsel Sales Visualizer” with custom CSS styling.

-Line Chart: Displays sales over time, with date-sorted data and labeled axes.

-Region Filter: Radio buttons allow users to filter data by region (north, east, south, west, all).

-Dynamic Updates: The chart updates in real time based on the selected region.

-Styling: Custom CSS applied for a clean, professional interface.

Purpose: Enables Soul Foods to visually compare sales before and after the January 15, 2021 price increase and to drill down into region-specific trends.

<img width="1920" height="1041" alt="Screenshot (592)" src="https://github.com/user-attachments/assets/3521b2b0-3b8c-4d9a-a920-760e3a36dda5" />


4. Automated Testing
   
Test File: test_app.py

Testing Framework: pytest with Dash testing utilities.

Test Cases:

-Header Presence: Verifies that the dashboard title is correctly displayed.

-Visualization Presence: Ensures the line chart component is rendered.

-Region Picker Presence: Confirms that all five radio button options are available.

Result: All three tests pass successfully, confirming the core functionality of the Dash app.

<img width="1920" height="1036" alt="Screenshot (593)" src="https://github.com/user-attachments/assets/ea2ff3c6-2718-493c-adc7-47c1a10247e9" />


5. Continuous Integration (CI) Readiness:
   
-Script: run_tests.ps1 (PowerShell) / run_tests.sh (Bash)

Functionality:

-Activates the project’s virtual environment.

-Executes the test suite using pytest.

-Returns exit code 0 if all tests pass, 1 otherwise.

Purpose: This script can be integrated into a CI/CD pipeline (e.g., GitHub Actions, Jenkins) to automatically validate changes before merging.

<img width="1920" height="1038" alt="Screenshot (587)" src="https://github.com/user-attachments/assets/87c71ef5-ab18-400e-82bb-cc114f1c3f50" />

Key Insights from Visualization:

-The line chart clearly shows a noticeable drop in sales immediately after January 15, 2021, indicating that the price increase had a negative impact on sales volume.

-Regional filtering reveals that the trend is consistent across all regions, with the south region experiencing the most pronounced decline.

Technologies Used:

-Python 3.14.3

-Pandas – data manipulation

-Dash & Plotly – interactive web dashboard

-Pytest & Selenium – automated testing

-Git & GitHub – version control and collaboration

<img width="1920" height="1043" alt="Screenshot (589)" src="https://github.com/user-attachments/assets/6aaa8adc-c51e-4710-96d9-9f0bbe462156" />
