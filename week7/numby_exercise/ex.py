import numpy as np
import pandas as pd


class TemperatureData:
    def __init__(self, days, min_temp=20, max_temp=30):
        self.days = days
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.temperatures = self._generate_temperatures()
        self.temperature_data = self._create_dataframe()

    def _generate_temperatures(self):
        """
        Generate random temperatures between min_temp and max_temp for the given days.
        """
        return np.random.randint(self.min_temp, self.max_temp + 1, size=len(self.days))

    def _create_dataframe(self):
        """
        Create a Pandas DataFrame from the generated temperature data.
        """
        temperature_df = pd.DataFrame({
            'Day': self.days,
            'Temperature': self.temperatures
        })
        temperature_df.set_index('Day', inplace=True)
        return temperature_df

    def get_temperature_data(self):
        """
        Return the temperature data as a Pandas DataFrame.
        """
        return self.temperature_data

    def print_temperature_data(self):
        """
        Print the temperature data to the console with aligned headers.
        """
        # Print the header
        header = f"{'Day':<10} {'Temperature':<12}"
        print(header)
        print('-' * len(header))

        # Print the DataFrame
        for day, temp in self.temperature_data.itertuples():
            print(f"{day:<10} {temp:<12}")

