import matplotlib.pyplot as plt

def histogram (ax, x, title, xlabel, ylabel:str = "antal", grid: bool= True):
    ax.hist(x, bins = 8, edgecolor = "black")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis= "y")
    plt.tight_layout()
    return ax

def boxplot (ax, values, tick_label, title, xlabel, ylabel):
    ax.boxplot(values, tick_labels = tick_label)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    plt.tight_layout()
    plt.suptitle("")
    return ax

def bar (ax, x,y, title, xlabel, ylabel):
    ax.bar(x,y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, axis = "y")
    plt.tight_layout()
    plt.suptitle("")
    return ax