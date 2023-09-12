
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

        headers = [str(d) for d in delay_range]

        all_trends = pd.DataFrame(index=time_range, columns=headers)

        # calculate ideal dose
        peak_bg = self.starting_bg + (self.carbs*self.correction)/self.ratio
        final_bgs = [(peak_bg - u*self.correction) for u in range(30)]
        optimal_dose = np.argmin([abs(i-6) for i in final_bgs])

        for delay in delay_range:
            trend_calculator = TrendCalculator(
                optimal_dose,
                self.correction,
                self.carbs,
                self.ratio,
                delay,
                self.glycemic_index,
                self.starting_bg
            )

            times, trend = trend_calculator.total_effect()

            all_trends[str(delay)] = trend

        return all_trends, optimal_dose

    def find_optimal(self, trends):

        # remove all hypos
        filtered_trends = trends.loc[:, (trends >=4.).all()]

        # identify ts with lowest standard deviation

        std_devs = filtered_trends.std()

        optimal_ind = std_devs.idxmin()

        return optimal_ind, filtered_trends[optimal_ind]



