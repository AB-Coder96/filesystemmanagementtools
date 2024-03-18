import openpyxl
from datetime import datetime 
###############################
def get_date_input(self):
        while True:
            try:
                year = int(input("Enter the year: "))
                month = int(input("Enter the month (1-12): "))
                day = int(input("Enter the day of the month: "))
                
                # Check if the entered values form a valid date
                datetime(year=year, month=month, day=day)
                
                # Combine the values into 'YYYY-MM-DD' format
                date = f"{year:04d}-{month:02d}-{day:02d}"
                return date
            except ValueError:
                print("Invalid input. Please enter valid numerical values.")
def get_date_time_input():
        while True:
            try:
                year = int(input("Enter the year: "))
                month = int(input("Enter the month (1-12): "))
                day = int(input("Enter the day of the month: "))
                hour=int(input("Enter the hour of the day (0-23): "))
                # Check if the entered values form a valid date
                datetime(year=year, month=month, day=day, hour=hour)
                
                # Combine the values into 'YYYY-MM-DD' format
                date = f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:00:00"
                return date
            except ValueError:
                print("Invalid input. Please enter valid numerical values.")
def select_type(List):
    # Calculate the midpoint of the list
    midpoint = len(List) // 2
    
    # Print the first half of the list in the first row
    for idx, List_type in enumerate(List[:midpoint], start=1):
        print(f"{idx}. {List_type}", end='\t')
    
    print()  # Print a newline to move to the next row
    
    # Print the second half of the list in the second row
    for idx, List_type in enumerate(List[midpoint:], start=midpoint + 1):
        print(f"{idx}. {List_type}", end='\t')
    
    print()  # Print a newline to move to the next row
    
    while True:
        selection = input(f"Enter the number corresponding to the List type: ")
        try:
            selection = int(selection)
            if 1 <= selection <= len(List):
                selected_type = List[selection - 1]
                return selected_type
            else:
                print("Please enter a valid number from the list.")
        except ValueError:
            print("Please enter a valid number.")