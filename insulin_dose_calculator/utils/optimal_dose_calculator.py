
import numpy as np
import pandas as pd
from insulin_dose_calculator.utils.trend_calculator import TrendCalculator

class OptimalDoseCalculator:

    def __init__(self,
                 correction,
                 carbs,
                 ratio,
                 glycemic_index,
                 starting_bg):

        self.correction = correction
        self.carbs = carbs
        self.ratio = ratio
        self.glycemic_index = glycemic_index
        self.starting_bg = starting_bg

    def calculate_trends(self):

        unit_range = range(0,31)
        delay_range = range(0, 90, 5)

        time_range = np.arange(0, 6, 1 / 12)

        headers = [(str(u), str(d)) for u in unit_range for d in delay_range]

        all_trends = pd.DataFrame(index=time_range, columns=headers)

        print('here')
        for unit in unit_range:
            for delay in delay_range:
                trend_calculator = TrendCalculator(
                    unit,
                    self.correction,
                    self.carbs,
                    self.ratio,
                    delay,
                    self.glycemic_index,
                    self.starting_bg
                )

                times, trend = trend_calculator.total_effect()

                all_trends[(str(unit),str(delay))] = trend

        return all_trends

    def find_optimal(self, trends):

        # remove all hypos
        filtered_trends = trends.loc[:, (trends >=4.).all()]

        # remove all which finish above 8
        closest_to_optimal = min(abs(filtered_trends.iloc[-1] - 6 )) + 6
        print(closest_to_optimal)

        filtered_trends = filtered_trends.loc[:, filtered_trends.iloc[-1] == closest_to_optimal]


        print(filtered_trends)

