from functools import reduce


def convert_celsius_to_fahrenheit(celsius_temperatures):
    """Convert a list of temperatures from Celsius to Fahrenheit."""
    return list(map(lambda x: x * 9 / 5 + 32, celsius_temperatures))


def filter_temperatures(temperatures, threshold):
    """Filter out temperatures above the given threshold."""
    return list(filter(lambda x: x <= threshold, temperatures))


def calculate_average_temperature(temperatures):
    """Calculate the average of a list of temperatures using reduce."""
    total_sum = reduce(lambda acc, x: acc + x, temperatures, 0)
    return total_sum / len(temperatures) if temperatures else 0


def convert_and_filter_temperatures():
    celsius_temperatures = [20, 22, 25, 27, 30, 33]

    # Part 1: Convert Celsius to Fahrenheit
    fahrenheit_temperatures = convert_celsius_to_fahrenheit(celsius_temperatures)

    # Part 2: Filter temperatures that are 75 degrees Fahrenheit or lower
    filtered_temperatures = filter_temperatures(fahrenheit_temperatures, 75)

    # Calculate the average temperature
    average_temperature = calculate_average_temperature(fahrenheit_temperatures)

    # Print the results
    print(f"Converted Fahrenheit temperatures: {fahrenheit_temperatures}")
    print(f"Filtered Fahrenheit temperatures (75 degrees or lower): {filtered_temperatures}")
    print(f"Average Fahrenheit temperature: {average_temperature}")

    return average_temperature


average_temp = convert_and_filter_temperatures()
print("Returned average temperature:", average_temp)
