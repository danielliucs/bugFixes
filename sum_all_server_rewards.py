import pandas as pd

seeds = [5,10,15]

fedavg_eval = "A2C_RL_SERVER_FED_AVG"
fisher_eval = "A2C_RL_SERVER_PERCENTILE_AGGREGATE"

fedavg_eval_all_file = f'{fedavg_eval}_ALL'
fisher_eval_all_file = f'{fisher_eval}_ALL'

sum_fedavg_all = f'SUM_{fedavg_eval_all_file}.csv'
sum_fisher_all = f'SUM_{fisher_eval_all_file}.csv'

fisher_rewards = pd.read_csv(f'{fisher_eval_all_file}.csv', names=[0,1,2,3,4,5,6,7,8])
fedavg_rewards = pd.read_csv(f'{fedavg_eval_all_file}.csv', names=[0,1,2,3,4,5,6,7,8])

print(f'{fisher_eval_all_file}.csv')
print(f'{fedavg_eval_all_file}.csv')

fed = open(sum_fedavg_all, "w")
fed.close()

fish = open(sum_fisher_all, "w")
fish.close()

for i in range(len(seeds)):
    #sum along the columns
    sumlist = [i, i+3, i+6]
    fisher_rewards[i] = fisher_rewards[sumlist].sum(axis=1)
    fedavg_rewards[i] = fedavg_rewards[sumlist].sum(axis=1)

#Only want the first 3 columns
fisher_rewards.iloc[:, 0:len(seeds)].to_csv(sum_fisher_all, index=False, header=None)
fedavg_rewards.iloc[:, 0:len(seeds)].to_csv(sum_fedavg_all, index=False, header=None)
