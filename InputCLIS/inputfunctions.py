import openpyxl

def get_column_values(file_path, column_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # Assuming your data starts from the second row, adjust as needed
    column_data = [sheet[column_name][i].value for i in range(2, sheet.max_row + 1)]

    # Get unique values
    unique_values = set(column_data)

    return unique_values

def select_from_list(options):
    print("Select an option:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
