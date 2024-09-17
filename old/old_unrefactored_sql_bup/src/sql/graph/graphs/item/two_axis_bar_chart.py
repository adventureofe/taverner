import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def two_axis_bar_chart(x_axis, y_axis, title, x_label, y_label, mult_one = False):
    green_color = "#00FF00"
    fig, ax = plt.subplots(figsize=(2, 2), facecolor='black',
                       layout='constrained')

    ax.bar(x_axis, y_axis, color="red")
    
    fig.suptitle('Figure')
    ax.set_title(title, color=green_color, loc='left', fontstyle='oblique', fontsize='xx-large')
    ax.set_xlabel(x_label, color=green_color)
    ax.set_ylabel(y_label, color=green_color)
    ax.tick_params(axis='x', colors=green_color, rotation=45)  
    ax.tick_params(axis='y', colors=green_color)

    if mult_one:
        ax.yaxis.set_major_locator(MultipleLocator(1))
    
    ax.grid(True, color=green_color, linestyle="--", linewidth=0.5, which='both', axis='y')

    # Set background colors (optional)
    ax.set_facecolor('black')                     # Axes background
    fig.patch.set_facecolor('black')              # Figure background

    ax.spines['left'].set_color(green_color)
    ax.spines['bottom'].set_color(green_color)

    plt.show()
