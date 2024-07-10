## Project Overview

**Note:** This project is not complete.

### Introduction

The motivation behind this project is to create an AI agent capable of providing analysis on stock data of interest, particularly for those that may have difficulty or lack the required background to do so such as the elderly or children.

### Description

The directory 'ETL' contains an ETL pipeline that pulls stock data from 12 Data's time-series API. Upon running `./exe_etl.sh` in the main directory, one will be prompted to provide a stock symbol, start date, and end date, after which the program pulls the data and loads it into a PostgreSQL table labeled 'stock_prices'.

In addition to an ETL pipeline, I've also created a Dash data app, the code for which is contained in 'dash_app'. After running the ETL pipeline, running `./exe_dash.sh` will start the Dash app where one can see visualizations of the data pulled. The app currently contains an OHLC plot, price ratio, and moving average of the data provided.

Finally, I've created a simple AI agent that is able to interact with my PostgreSQL database and interpret natural language queries about the data using LangChain and the OpenAI API. Upon running `./exe_agent.sh` in the terminal, one is prompted to provide a query that can be answered given the data available in the stock_prices table.

### Next Steps

1. Integration of the AI agent with the Dash data app: Ideally, one will be able to enter their query in a text box contained in the Dash app, with the LLM's response displayed as well.

2. Greater functionality regarding plots: I intend to implement a dropdown menu of a variety of different plots to start - with considerably more options than the 3 provided. Also currently looking into ways that one will be able to generate or display a particular plot of interest given a user's query (i.e., 'Show me a moving average plot').

3. ETL execution from the Dash app: Currently working on ways to execute the ETL pipeline from the Dash app where a user will be able to input the stock symbol, start date, and end date.

4. Cache clearing from the Dash app: Clearing the data that is fetched from the SQL table has proven to be somewhat difficult, especially when one wants to 'refresh' what is shown on the plot. The file `clear_data.py` does this well when executed from the terminal, but like other features that have been described, I'd like this to be handled via user input in the Dash app.

