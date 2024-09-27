## Project Overview

**Note:** This project is not complete.

### Introduction

The motivation behind this project is to create an AI agent capable of providing analysis on stock data of interest, particularly for those that may have difficulty or lack the required background to do so such as the elderly or children.

### Description

The directory 'ETL' contains an ETL pipeline that pulls stock data from 12 Data's time-series API. Upon running `./exe_etl.sh` in the main directory, one will be prompted to provide a stock symbol, start date, and end date, after which the program pulls the data and loads it into a PostgreSQL table labeled 'stock_prices'.

In addition to an ETL pipeline, I've also created a Dash data app, the code for which is contained in 'dash_app'. After running the ETL pipeline, running `./exe_dash.sh` will start the Dash app where one can see visualizations of the data pulled. The app currently contains an OHLC plot, price ratio, and moving average of the data provided.

Finally, I've created a simple AI agent that is able to interact with my PostgreSQL database and interpret natural language queries about the data using LangChain and the OpenAI API. Upon running `./exe_agent.sh` in the terminal, one is prompted to provide a query that can be answered given the data available in the stock_prices table.


