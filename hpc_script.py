from datetime import datetime
import subprocess
import shutil
import threading
import time
import os


batchScript_PH= 0
simulation_PH = 0
dir_PH = "placeholder_files"
time_now = datetime.now()
bashScript_filename = "ISCA_Submission.sh"

def non_negative_int_userInput(prompt, not_negative=True):
    while True:
        try:
            value = int(input(f"{prompt}\n--> "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if value <= 0 and not_negative:
            print("Sorry, this cannot be a negative number")
            continue
        else:
            break
    return value

def y_n_userInput(prompt):
    while True:
        try:
            y_n = str(input(f"{prompt}\n--> "))
        except ValueError:
            print("Sorry, I didn't understand this.")
            continue
        if y_n == "y":
            output = True
            break
        elif y_n == "n":
            output = False
            break
        else:
            print("Sorry this input was invalid. Please enter either 'y' or 'n'")
    return output

def replace_inplace(filename, find, replace):
    with open(filename, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(find, replace)

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def dedalusPipeline(simulation_DIR):  
    with cd (simulation_DIR):  
        result = subprocess.run(["sbatch", f"ISCA_Submission.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

run = 1
anotherRun = True
while anotherRun:
    run_name = time_now.strftime(f"%d-%m-%y_%H-%M-%S_run_{run}")
    simulation_DIR = f"./Simulations/{run_name}"
    
    # Input options go here
    sbatch_options = {
        "1": "How many cores to run the simulation on?",
    }

    simulation_options = {
        "2": "What square resolution would you like to set?",
        "3": "What maximum time would you like to be reached in the simulation?"
    }

    plotting_options = {
        
    }

    # cores
    # resolution
    # max_sim_time
    
    # Lambda 
    # Dust to gas ratio bd0
    # eta

    default_settings = {
        "1": "4",
        "2": "256",
        "3": "30"
    }

    settings = {
    }
    # for key, value in options.items():
    #     setting = str(non_negative_int_userInput(f"({key}): {value}"))
    #     settings[key: setting]

    cores = str(non_negative_int_userInput(f"cores"))

    shutil.copytree(dir_PH, simulation_DIR)
    replace_inplace(f"{simulation_DIR}/{bashScript_filename}", "$1", cores)
    # replace_inplace(f"{run_name}/{bashScript_filename}", "$2", f"./{run_name}")
    time.sleep(2)

    # threading.Thread(target=dedalusPipeline, args=(run_name,))
    dedalusPipeline(simulation_DIR)
    anotherRun = y_n_userInput("Would you like to add another run?")
    run += 1