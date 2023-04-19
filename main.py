import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

# initialize aries
minutes = [7, 15, 23, 31, 38, 45, 53, 60, 6, 13, 19, 24, 30, 35, 39, 43]
seconds = [51, 40, 25, 4, 34, 56, 5, 0, 40, 3, 7, 51, 13, 12, 46, 55]
degree = 0
theta = []
vara_decimals = []
sci_decimals = []

def decimal_calc(minute: float, second: float):
    decimal = minute/60 + second/60**2
    return decimal

# fill empty lists with corresponding values
for i in range(0, 16):
    # aries calculations
    degree += 3.75
    theta.append(degree)
    vara_decimals.append(decimal_calc(minutes[i], seconds[i]))
    sci_decimals.append(math.sin(math.radians(theta[i])))

data = {'Theta': theta,
        'Vara Decimals': vara_decimals,
        'Calculator Decimals': sci_decimals}

data_frame = pd.DataFrame(data)
graph = sns.pointplot(x='Theta', y='value', hue='variable', data=pd.melt(data_frame, ['Theta']))
graph.set(ylabel="Numeric Value", title='Sine vs. sin')
plt.xticks(rotation = 45)
plt.show()

