#!/bin/bash

export PYTHONPATH=$PYTHONPATH:/Users/aidan/Desktop/finance_agent
cd ETL

echo "Enter the stock symbol:"
read stock_symbol

echo "Enter the start date (YYYY-MM-DD):"
read start_date

echo "Enter the end date (YYYY-MM-DD):"
read end_date


python main.py "$stock_symbol" "$start_date" "$end_date"

echo "ETL process complete, extracted "$stock_symbol" data from "$start_date" to "$end_date""