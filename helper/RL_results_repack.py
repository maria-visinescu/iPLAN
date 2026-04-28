import pandas as pd
log_dir = "/home/maria-visinescu/iPLAN/results/sacred/5"
log_file = "cout.txt"
ds_file = "results.csv"
with open(log_dir + "/" + log_file, encoding="utf8") as f:
    lines = f.readlines()
raw_lines = lines[2:]
raw_lines
def logout_helper(single_line):
    episode = int(single_line[0].split("#")[1])
    time_step = int(single_line[1].split(":")[1])
    win_num = float(single_line[2].split(":")[1])
    reward = float(single_line[3].split(":")[1])
    epi_len = float(single_line[4].split(":")[1])
    return episode, time_step, win_num, reward, epi_len
def result_repack(lines):
    episode_list, time_step_list, win_num_list, reward_list, epi_len_list = [], [], [], [], []
    for i in range(len(lines)):
        line = lines[i]
        # Only keep the summary lines not the additional metric lines
        if "Current time step" not in line:
            continue
        single_line = lines[i].split("|")
        if len(single_line) > 3:
            episode, time_step, win_num, reward, epi_len = logout_helper(single_line)
            episode_list.append(episode)
            time_step_list.append(time_step)
            win_num_list.append(win_num)
            reward_list.append(reward)
            epi_len_list.append(epi_len)
    return episode_list, time_step_list, win_num_list, reward_list, epi_len_list
episode_list, time_step_list, win_num_list, reward_list, epi_len_list = result_repack(raw_lines)
data = {"Episode" : episode_list, 
        "Time_step": time_step_list, 
        "Average Win Num": win_num_list, 
        "Average reward": reward_list, 
        "Average Episode Length": epi_len_list}
df = pd.DataFrame(data=data)
df
df.to_csv(log_dir + "/" + ds_file)
