from datetime import datetime, timedelta

def display_current_datetime():
  current_datetime = datetime.now()
  current_date = current_datetime.date()
  formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted_datetime}")

  def calculate_future_date():
    nonlocal current_date
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days = number_of_days)
    print(future_date) 
  calculate_future_date()

display_current_datetime()