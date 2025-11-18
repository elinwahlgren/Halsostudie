import numpy as np 
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

def spec_bar(df):
    plt.figure()
    df.plot(kind="bar")
    plt.ylabel("Andel")
    plt.title("Verklig vs simulerad andel")
    plt.xticks([0,1], ["Verklig", "Simulerad"], rotation= 0)
    plt.gca().set_yticks(np.arange(0, 0.07, 0.005))
    plt.gca().yaxis.set_major_formatter(lambda x, pos: f"{x:.1%}")
    plt.legend("")
    plt.show()

def errorbar(ax, mean_stick, lo, hi, mean_bp):
    ax.errorbar([0], [mean_stick], yerr=[[mean_stick - lo], [hi - mean_stick]], fmt="o", capsize=6)
    ax.axhline(mean_bp, color="tab:green", linestyle="--", label="Sant medel (från orginaldata)")
    ax.set_xticks([])
    ax.set_ylabel("Blodtryck")
    ax.grid(True, axis="y")
    ax.legend()
    ax.set_title("95%-CI för medel (normal-approximation)")
    plt.show()

def ax_boot(ax, boot_info, stick):
    ax.hist(boot_info, bins = 30, edgecolor = "black")
    ax.axvline(np.mean(stick), color="tab:green", linestyle="--", label="Stickprovsmedel")
    ax.axvline(np.percentile(boot_info, 2.5), color="tab:red", linestyle="--", label="2.5%")
    ax.axvline(np.percentile(boot_info, 97.5), color="tab:red", linestyle="--", label="97.5%")
    ax.set_title("Bootstrap-förderlning av medel + 95% - intervall")
    ax.set_xlabel("Resamplat medel")
    ax.set_ylabel("Antal")
    ax.grid(True, axis="y")
    plt.legend()
    plt.show()