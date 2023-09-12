import numpy as np
import matplotlib.pyplot as plt
import copy

class TrendCalculator:

    def __init__(self,
                 dose,
                 correction,
                 carbs,
                 ratio,
                 delay,
                 glycemic_index,
                 starting_bg):
        self.dose = dose
        self.correction = correction
        self.carbs = carbs
        self.ratio = ratio
        self.delay = delay
        self.glycemic_index = glycemic_index
        self.starting_bg = starting_bg

    def insulin_effect(self, time_step_minutes=5):
        """

        :param time_step_minutes:
        :return:
        """
        # Convert the time limits to hours
        end_time_hours = 6

        # Initialize time and values lists
        time_values = []
        series_values = []

        decrease = self.dose * self.correction

        # Generate time series values
        for t in np.arange(0, end_time_hours, time_step_minutes / 60):

            if 0 <= t <= 4:
                # Sigmoid function between 0 and 4 hours
                sigmoid_value = (1 / (1 + np.exp(-4 * (t - 2))))*(-decrease)  # Adjust the 10 for the steepness of the sigmoid
                time_values.append(t)
                series_values.append(sigmoid_value)
            else:
                # Constant after t=4
                time_values.append(t)
                series_values.append(-decrease)

        return time_values, series_values

    def food_effect(self, time_step_minutes=5):
        """

        :param ratio:
        :param correction:
        :param delay:
        :param glycemic_index:
        :param starting_bg:
        :param time_step_minutes:
        :return:
        """
        # Convert the time limits to hours
        delay_hours = self.delay / 60
        end_time_hours = 6

        # Initialize time and values lists
        time_values = []
        series_values = []

        increase = (self.carbs*self.correction)/self.ratio

        # Generate time series values
        for t in np.arange(0, end_time_hours, time_step_minutes / 60):

            if t < delay_hours:
                time_values.append(t)
                series_values.append(self.starting_bg)
            elif delay_hours <= t <= delay_hours + 16/self.glycemic_index:
                # Sigmoid function between 0 and 4 hours
                exponent = -self.glycemic_index * (t - ((8/self.glycemic_index) + delay_hours))
                sigmoid_value = self.starting_bg + (1 / (1 + np.exp(exponent)))*(increase)  # Adjust the 10 for the steepness of the sigmoid
                time_values.append(t)
                series_values.append(sigmoid_value)
            else:
                time_values.append(t)
                series_values.append(self.starting_bg + increase)

        return time_values, series_values

    def total_effect(self):
        """

        :param correction:
        :param carbs:
        :param ratio:
        :param delay:
        :param glycemic_index:
        :param starting_bg:
        :return:
        """

        _, food_change = self.food_effect()

        time_values, insulin_change = self.insulin_effect()

        total_change = np.add(food_change, insulin_change)

        return time_values, total_change

