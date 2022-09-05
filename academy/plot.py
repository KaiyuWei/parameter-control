import pandas as pd
import os
import matplotlib.pyplot as plt

func_name = "C25"
os.chdir("C:/courses/graduation thesis/code/collect data/{}".format(func_name))
# dictionary containing 11 dfs from tuning_method
data = {}
data['DPTP'] = pd.read_excel("training_result_{}.xlsx".format(func_name),
                             sheet_name="tuning method", header=0, index_col=0)
for i in range(10):
    name = str(i)
    data[name] = pd.read_excel("training_result_{}.xlsx".format(func_name),
                               sheet_name="preset {}".format(i), header=0, index_col=0)

# draw the figures
axes = data['DPTP'].plot(x="time", y="fitness",
                         label="DPTP(r = 30)", linestyle='dashed')
for i in range(10):
    name = str(i)
    data[name].plot(ax=axes, x="time", y="fitness",
                    label="Preset {}".format(name))
# data['7'].plot(ax=axes, x="time", y="fitness", label="Preset 7")
# data['8'].plot(ax=axes, x="time", y="fitness", label="Preset 8")
# data['9'].plot(ax=axes, x="time", y="fitness", label="Preset 9")
plt.grid()
plt.xlabel('time(seconds)')
plt.ylabel('fitness')
plt.show()
