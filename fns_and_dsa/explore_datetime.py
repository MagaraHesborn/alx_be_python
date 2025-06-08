from datetime import datetime, timedelta, date
def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_date}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = date.today()
    future_date = current_date + timedelta(days=number_of_days)
    print(f"{future_date.strftime("%Y-%m-%d")}")


display_current_datetime()
calculate_future_date()
