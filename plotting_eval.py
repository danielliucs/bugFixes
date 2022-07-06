import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fisher_file = "AVG_OF_FISHER_EXPERIMENTS.csv"
fedavg_file = "AVG_OF_FEDAVG_EXPERIMENTS.csv"

TSBOARD_SMOOTHING = 0.0
NUM_TRAINING_ROUNDS = 30

algorithm_names = ["Federated Averaging", "Shoal"]

fisher_csv = pd.read_csv(fisher_file, names=["trace1","trace2","trace3"])
fedavg_csv = pd.read_csv(fedavg_file)

#print(fisher_csv)
sns.set(font_scale=1.4)
sns.set_style("whitegrid")
f, ax1 = plt.subplots(figsize=(8.5,5))

fisher_csv = fisher_csv.ewm(alpha=(1 - TSBOARD_SMOOTHING)).mean()
ax1 = sns.lineplot(data=fisher_csv, palette='mako', linewidth=2.5)

#print(len(fisher_csv)-1), this is 30

ax1.set_xlabel("Training Round", fontstyle='normal')
ax1.set_ylabel("Average Reward")
ax1.tick_params(axis='y')

plt.xlim(0, len(fisher_csv)-1)
f.savefig("fisher_avg_plot.pdf", bbox_inches='tight')
plt.show()
