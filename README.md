Currency Converter (Python CLI)

A straightforward command-line currency converter built in Python.
It reads predefined exchange rates, lets users pick two currencies,
accepts an amount, and outputs the converted value.

This project is structured for readability and experimentation,
including optional UI elements like loading animations and delays.









🚀 Features

Supports 20+ global currencies

Interactive CLI interface

Input validation for currency codes and amounts

Optional visual elements (loading animation, slow lists, summaries)

Simple conversion logic using predefined exchange rates

Looping menu to perform multiple conversions




📂 Project Structure
.
├── converter.py       # Main program (your code)
├── README.md          # This file









🧠 How It Works

1  Exchange rates are loaded from a static dictionary.

2  User selects:

.  Currency to convert from

.  Currency to convert to

3 User enters the amount.

4 Program calculates:
amount * rate[from] / rate[to]

5 Result is displayed with formatting










📦 Requirements

.  Python 3.x

.  Standard library only (no external packages required)










▶️ Running the Program

python converter.py


You’ll see this:

==============================
      CURRENCY MACHINE        
==============================

Available Currencies:
1. USD  

2. EUR

3. GBP

4. JPY

5. AUD

6. CAD

7.CNY

8.AED

9.SGD

10.NZD

11.ZAR

12.CHF

13.RUB

14.KRW

15.THB

16.PHP

17.IDR

18.HKD

19.DKK

20.SEK

Total: 20 currencies

.


























