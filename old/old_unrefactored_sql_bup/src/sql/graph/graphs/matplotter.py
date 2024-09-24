import sys
import sqlite3
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def bar_chart(x, y, all_y = False):
    green_color = "#00FF00"

    fig = plt.figure(figsize=(10,6))

    ax = plt.gca()
    ax.set_facecolor('black')
    plt.gcf().set_facecolor('black')
  
    plt.bar(x, y, color="red")

    plt.xlabel('x', color=green_color)
    plt.ylabel('y', color=green_color, rotation=45)
    plt.title('example matplotlib', color=green_color)
    plt.xticks(rotation=45, color=green_color)
    plt.yticks(color=green_color)

    if all_y:
        ax.yaxis.set_major_locator(MultipleLocator(1))
        
    plt.grid(True, color=green_color, linestyle="--", linewidth=0.5)

    plt.show()



def main() -> int:
    x = [1,2,3,4,5,6,7,8,9,10]
    y = [31,24,16,13,16,8,12, 15, 14, 31]
 
    bar_chart(x, y)

    return 0

if __name__ == "__main__":
    sys.exit(main())
