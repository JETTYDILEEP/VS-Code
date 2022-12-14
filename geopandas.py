import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import pandas as pd
import geopandas as gpd
# function to update the data
def my_function(i):
    # get data
    try:
        df = pd.read_excel('w.xlsx', engine='openpyxl')
    except:
        print('error reading file')
   # merge with world map
    world_values = world.merge(df, how='right', 
                               on='name', copy=True)
    # clear axis
    ax.cla()
    ax1.cla()
    # plot map
    world_values.plot(column='Val', ax=ax1, 
                      cmap='coolwarm_r', edgecolors='black',
                      linewidths=0.5, alpha=0.8)
    # remove spines and ticks
    ax1.spines['left'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.set_yticks([])
    ax1.set_xticks([])
    # get records with a value higher than 0.97
    alert = world_values[world_values['Val'] > 0.97]
    alert = alert.sort_values('Val', ascending=False)
    # plot bars
    ax.bar(alert.name, alert.Val, color='#E9493C', alpha=0.8)
    # limits, labels, and spines
    ax.set_ylim(0.9, 1)
    ax.set_xticklabels(alert.name, fontsize=11)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
# world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# define and adjust figure
fig, (ax, ax1) = plt.subplots(2, 1, figsize=(16,12), facecolor='#707576', gridspec_kw={'height_ratios': [1, 3]})
ax.set_facecolor('#707576')
ax1.set_facecolor('#707576')
# animate
ani = FuncAnimation(fig, my_function, interval=500)
fig.tight_layout()
plt.show()
