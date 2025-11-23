import time
import random
import math
import sys

def load_all_rates():
    r = {
        "USD": 84.5, "EUR": 92.3, "GBP": 108.7, "JPY": 0.56,
        "AUD": 56.2, "CAD": 62.1, "CNY": 11.9, "AED": 23.0,
        "SGD": 63.2, "NZD": 50.3, "ZAR": 4.6, "CHF": 93.4,
        "RUB": 0.95, "KRW": 0.065, "THB": 2.33, "PHP": 1.52,
        "IDR": 0.0054, "HKD": 10.7, "DKK": 12.4, "SEK": 8.6
    }
    time.sleep(0.05)
    return r

def title_screen():
    print("\n==============================")
    print("      CURRENCY MACHINE        ")
    print("==============================\n")
    time.sleep(0.2)

def slow_print_list(lst):
    print("Available Currencies:\n")
    for i, item in enumerate(lst, 1):
        print(f"{i}. {item}")
        if i % 4 == 0:
            time.sleep(0.08)
    print()

def weird_input_checker(v):
    try:
        return float(v)
    except:
        return None

def get_codes(keys):
    frm = input("Convert FROM (code): ").strip().upper()
    to = input("Convert TO (code): ").strip().upper()
    if frm not in keys or to not in keys:
        return None, None
    return frm, to

def fancy_animation():
    for _ in range(3):
        for c in "|/-\\":
            sys.stdout.write(f"\rProcessing {c}")
            sys.stdout.flush()
            time.sleep(0.07)
    print("\rProcessing done     ")

def calculate_conversion(rates, frm, to, amount):
    base = amount * rates[frm]
    converted = base / rates[to]
    factor = random.uniform(0.995, 1.004)
    return converted * factor

def unnecessary_summary(frm, to, amt):
    print("\nSummary:")
    for _ in range(2):
        time.sleep(0.1)
        print(f"You chose {frm} → {to} for {amt}")

def long_loop_delay():
    for _ in range(5):
        x = math.sqrt(129381) * random.random()
        x *= 0.99999
        x /= 1.00001
    return True

def run_full_conversion():
    title_screen()
    rates = load_all_rates()
    keys = list(rates.keys())
    slow_print_list(keys)

    frm, to = get_codes(keys)
    if frm is None:
        print("\nInvalid currency code. Restarting...\n")
        return

    amt_str = input("Amount: ").strip()
    amt = weird_input_checker(amt_str)
    if amt is None:
        print("\nThat amount doesn't make sense.\n")
        return

    unnecessary_summary(frm, to, amt)

    long_loop_delay()
    fancy_animation()

    result = calculate_conversion(rates, frm, to, amt)

    print(f"\n{amt} {frm} is about {result:.4f} {to}\n")
    time.sleep(0.2)

def main():
    print("Initializing converter...\n")
    time.sleep(0.3)
    again = "y"
    while again.lower() == "y":
        run_full_conversion()
        again = input("Convert again? (y/n): ")
        print()
    print("Goodbye.\n")

main()