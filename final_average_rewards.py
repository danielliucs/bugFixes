import pandas as pd

fedavg_eval = "SUM_A2C_RL_SERVER_FED_AVG_ALL.csv"
fisher_eval = "SUM_A2C_RL_SERVER_PERCENTILE_AGGREGATE_ALL.csv"

fedavg_avg = "AVG_OF_FEDAVG_EXPERIMENTS.csv"
fisher_avg = "AVG_OF_FISHER_EXPERIMENTS.csv"

seeds = [1,2,3]

fisher_rewards = pd.read_csv(fisher_eval, names=[0,1,2])
fedavg_rewards = pd.read_csv(fedavg_eval, names=[0,1,2])

avg_fisher_rewards = []
avg_fedavg_rewards = []
#Let df represent dataframe
#We always append to a list and convert to dataframe at the end to save memory and speed
df_avg_fisher_rewards = [] 
df_avg_fedavg_rewards = []

counter = 0

while counter < len(seeds):
    avg_fisher_rewards = []
    avg_fedavg_rewards = []
    for index, row in fisher_rewards.iterrows():
        avg_fisher_rewards.append(row[counter]/len(seeds))
    for index, row in fedavg_rewards.iterrows():
        avg_fedavg_rewards.append(row[counter]/len(seeds))

    df_avg_fisher_rewards.append(avg_fisher_rewards)
    df_avg_fedavg_rewards.append(avg_fedavg_rewards)
    print("The column's rows that you are now iterating through are: ", counter)
    counter += 1

#We transpose at the end since appending a list causes the dataframe to have the rows and cols swap
#Therefore we want the opposite so we transpose

pd.DataFrame(df_avg_fisher_rewards).transpose().to_csv(fisher_avg, index=False, header=None)
pd.DataFrame(df_avg_fedavg_rewards).transpose().to_csv(fedavg_avg, index=False, header=None)
    
