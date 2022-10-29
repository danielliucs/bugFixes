import pandas as pd

def consolidate_n_files(folder, file, save_file, seeds, num_tasks):

    #initial read path
    csv_read_path = f'{folder}{seeds[0]}/{file}.csv'
    print(csv_read_path)
    csv_save_path = f'{save_file}_ALL.csv'
    col_names = []

    for i in range(num_tasks):
        col_names.append(i)

    rewards_csv_all = pd.read_csv(csv_read_path, names=col_names)
    print(rewards_csv_all)

    for i in range(1, len(seeds)):
        csv_read_path = f'{folder}{seeds[i]}/{file}.csv'
        
        print(csv_read_path)

        new_rewards = pd.read_csv(csv_read_path, names=col_names)

        tasks_counter = 0
        
        while tasks_counter < num_tasks:
        
           # print(i*num_tasks+tasks_counter)
            rewards_csv_all[i*num_tasks+tasks_counter] = new_rewards.iloc[:,tasks_counter]
            tasks_counter += 1

    rewards_csv_all.to_csv(csv_save_path, index=False, header=None)


if __name__ == '__main__':
    """Make sure the folder name at index i matches with the file name at index i"""
    results_folders = ["6out6/results_critic_grad_lamda2_aggregate_seed_","6out6/results_a2cadp_aggregate_seed_", "6out6/results_fedavg_aggregate_seed_", 
    "12out12/results_critic_grad_lamda2_aggregate_seed_","12out12/results_a2cadp_aggregate_seed_", "12out12/results_fedavg_aggregate_seed_", 
    "18out18/results_critic_grad_lamda2_aggregate_seed_","18out18/results_a2cadp_aggregate_seed_", "18out18/results_fedavg_aggregate_seed_",
    "6out6/a2c_abr_sim_seed_", "12out12/a2c_abr_sim_seed_", "18out18/a2c_abr_sim_seed_"]
    #"A2C_RL_SERVER_FED_ADP", "A2C_RL_SERVER_FED_AVG","A2C_RL_SERVER_FED_AVG", "evaluations"
    file_names = ["A2C_RL_SERVER_PERCENTILE_AGGREGATE", "A2C_RL_SERVER_FED_ADP", "A2C_RL_SERVER_FED_AVG",
        "A2C_RL_SERVER_PERCENTILE_AGGREGATE", "A2C_RL_SERVER_FED_ADP", "A2C_RL_SERVER_FED_AVG",
        "A2C_RL_SERVER_PERCENTILE_AGGREGATE", "A2C_RL_SERVER_FED_ADP", "A2C_RL_SERVER_FED_AVG",
        "evaluations", "evaluations", "evaluations"] 
    #"A2C_RL_SERVER_CRITIC", "A2C_RL_SERVER_ADP", "A2C_RL_SERVER_FEDAVG", "A2C_RL_SERVER_MAS", "A2C_ABR_SIM"
    save_files = ["6out6_critic_grad", "6out6_fedadp", "6out6_fedavg", "12out12_critic_grad", "12out12_fedadp", "12out12_fedavg",
    "18out18_critic_grad", "18out18_fedadp", "18out18_fedavg", "6out6_abr_sim", "12out12_abr_sim", "18out18_abr_sim"]
    seeds = [5, 10, 15]

    NUM_TASKS = 6
    
    for i in range(len(file_names)):
        print(len(results_folders), len(file_names), len(save_files))
        consolidate_n_files(results_folders[i], file_names[i], save_files[i], seeds, NUM_TASKS)
