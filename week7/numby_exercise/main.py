from week7.numby_exercise.ex import TemperatureData

if __name__ == "__main__":
    # Define the days of the week
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Create an instance of the TemperatureData class
    temp_data = TemperatureData(days_of_week)

    # Print the temperature data
    temp_data.print_temperature_data()
