from openpyxl import load_workbook
from matplotlib import pyplot
import os


def get_value(v):
    return v.value


file = os.path.dirname(os.path.realpath(__file__)) + "/data/data_analysis_lab.xlsx"
wb = load_workbook(file)
sheet = wb["Data"]
year = list(map(get_value, sheet['A'][1:]))
temp = list(map(get_value, sheet['C'][1:]))
sun = list(map(get_value, sheet['D'][1:]))

pyplot.plot(year, temp, label="Температура")
pyplot.plot(year, sun, label="Активность солнца")
pyplot.xlabel("Год")
pyplot.ylabel("Температура / Активность")
pyplot.title("Корреляция между активностью Солнца и\nизменениями климата на Земле")
pyplot.show()
