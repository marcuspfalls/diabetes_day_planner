
import sys
sys.path.append('/home/marcus/personal_projects/diabetes_day_planner/')

from insulin_dose_calculator.utils.trend_calculator import TrendCalculator
from insulin_dose_calculator.utils.optimal_dose_calculator import OptimalDoseCalculator
import matplotlib.pyplot as plt

dose = 9
correction = 1.5
carbs = 40
ratio = 5
delay = 20
glycemic_index = 6
starting_bg = 8

optimal_dose_calculator = OptimalDoseCalculator(
                                                correction=correction,
                                                carbs=carbs,
                                                ratio=ratio,
                                                glycemic_index=glycemic_index,
                                                starting_bg=starting_bg
                                                )
#
all_trends = optimal_dose_calculator.calculate_trends()
#
print(all_trends)

filtered_trends = optimal_dose_calculator.find_optimal(all_trends)

for column_name in filtered_trends.columns:
    column = filtered_trends[column_name]
    plt.plot(filtered_trends.index.tolist(), trend_bg)

plt.axhspan(min(min(trend_bg), 3), 4, facecolor='red', alpha=0.3)
plt.axhspan(4, 8, facecolor='green', alpha=0.3)
plt.axhspan(8, 10, facecolor='greenyellow', alpha=0.3)
plt.axhspan(10, 14, facecolor='yellow', alpha=0.3)
if max(trend_bg) >= 13:
    plt.axhspan(14, max(trend_bg) + 1, facecolor='orange', alpha=0.3)

plt.show()

# trend_calculator = TrendCalculator(dose, correction, carbs, ratio, delay, glucemic_index, starting_bg)
#
# trend_time, trend_bg = trend_calculator.total_effect()
#
# plt.plot(trend_time, trend_bg)
#
# plt.axhspan(min(min(trend_bg), 3), 4, facecolor='red', alpha=0.3)
# plt.axhspan(4, 8, facecolor='green', alpha=0.3)
# plt.axhspan(8, 10, facecolor='greenyellow', alpha=0.3)
# plt.axhspan(10, 14, facecolor='yellow', alpha=0.3)
# if max(trend_bg) >= 13:
#     plt.axhspan(14, max(trend_bg) + 1, facecolor='orange', alpha=0.3)
#
# plt.show()


