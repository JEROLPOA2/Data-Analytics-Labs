
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("news.csv", index_col=0)
plt.figure()

colors = {
    "Television" : "dimgray",
    "Newspaper" : "gray",
    "Internet" : "tab:blue", 
    "Radio" : "lightgray"
    }

zorder = {
    "Television" : 1,
    "Newspaper" : 1,
    "Internet" : 2, 
    "Radio" : 1
}

linewidths = {
    "Television" : 2,
    "Newspaper" : 2,
    "Internet" : 4, 
    "Radio" : 2
}
for col in df.columns:

    plt.plot(
        df[col], 
        label=col,
        color=colors[col],
        zorder=zorder[col],
        linewidth=linewidths[col]
        )

plt.title("How People Get Their News", fontsize=16)

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["left"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)

for col in df.columns:

    firstyear = df.index[0]
    
    plt.scatter(
        x=firstyear,
        y=df[col][firstyear],
        color=colors[col],
        zorder=zorder[col]
    )

    lastyear = df.index[-1]
    
    plt.scatter(
        x=lastyear,
        y=df[col][lastyear],
        color=colors[col],
        zorder=zorder[col]
    )

    plt.text(
        firstyear - 0.2,
        df[col][firstyear],
        col + " " + str(df[col][firstyear]) + "%",
        ha="right",
        va="center",
        color=colors[col]
    )

    plt.text(
        lastyear + 0.2,
        df[col][lastyear],
        str(df[col][lastyear]) + "%",
        ha="left",
        va="center",
        color=colors[col]
    )

plt.tight_layout()
plt.savefig("news.png")  
plt.show()

