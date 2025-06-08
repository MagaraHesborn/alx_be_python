from datetime import datetime, timedelta, date
def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_date}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add: "))
    current_date = date.today()
    futrure_date = current_date + timedelta(days=number_of_days)
    futrure_date = futrure_date.strftime("%Y-%m-%d")
    print(f"{futrure_date}")



   

display_current_datetime()
calculate_future_date()
