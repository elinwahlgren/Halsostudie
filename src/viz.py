import matplotlib.pyplot as plt

def histogram (ax, x, title, xlabel, ylabel:str = "Antal", grid: bool= True):
    ax.hist(x, bins = 8, edgecolor = "black")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.tight_layout()
    return ax

def boxplot (ax, values, tick_label, title, xlabel, ylabel):
    ax.boxplot(values, tick_labels = tick_label)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.tight_layout()
    plt.suptitle("")
    return ax

def bar (ax, x,y, title, xlabel, ylabel):
    ax.bar(x,y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.tight_layout()
    plt.suptitle("")
    return ax

def plot (ax, x, y, axhline_label="Mål: 80% power", xlabel = "Ökning av gruppstorlekar (groupsize * n)", ylabel = "Skattad power (simulerad)", title= "Simulerad power"  ):    
    ax.plot(x, y, marker="o")
    ax.axhline(0.8, color="gray", linestyle="--", label=axhline_label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend()
    return ax