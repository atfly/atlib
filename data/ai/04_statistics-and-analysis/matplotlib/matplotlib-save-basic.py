import pandas as pd
import os
import matplotlib.pyplot as plt

plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "fundamentals"


def save_fig(fig_id):
    path = os.path.join(PROJECT_ROOT_DIR, fig_id + ".png")
    print("Saving figure", fig_id)
    plt.savefig(path, format='png', dpi=300)


data = pd.DataFrame({'k': [1, 2, 3, 4, 5]})
data.plot(kind='scatter', x="k", y="k", figsize=(5, 3))
plt.show()
save_fig('test')
