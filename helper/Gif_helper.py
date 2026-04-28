import glob
from PIL import Image

def make_gif(algo_name, env_name, frame_folder, info):
    frames = [Image.open(frame_folder + "/" + str(i) + ".jpg") for i in range(89)]
    
    frame_one = frames[0]
    info_str = "_" + str(info["win"]) + "_" + str(info["avg_len"]) + "_" + str(info["avg_speed"])
    frame_one.save(algo_name + "_" + env_name + info_str + ".gif", format="GIF", append_images=frames, save_all=True)

# Algo and env names
algo_name = "MAPPO"
env_name = "Hetero_E"
# Navigation matrics
info = {"win": 2, "avg_len": 49.6, "avg_speed":28.44}
# Change the path for screenshot storage
frame_folder = "animation/2"

make_gif(algo_name, env_name, frame_folder, info)