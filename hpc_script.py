from datetime import datetime
import subprocess
import shutil
import threading

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

def dedalusPipeline(run_name):
    subprocess.run(["sbatch", f"{run_name}/ISCA_Submission.sh"])

run = 1
anotherRun = True
while anotherRun:
    run_name = time_now.strftime(f"%d-%m-%y_%H-%M-%S_run_{run}")
    # Input options go here
    cores = str(non_negative_int_userInput("How many cores to run the simulation on?"))
    # Lambda 
    # Dust to gas ratio bd0
    # eta

    # simulation time
    # iteration number 
    # wall time

    shutil.copytree(dir_PH, run_name)
    replace_inplace(f"{run_name}/{bashScript_filename}", "$1", cores)
    replace_inplace(f"{run_name}/{bashScript_filename}", "$2", f"./{run_name}")
    

    threading.Thread(target=dedalusPipeline, args=(run_name,))

    anotherRun = y_n_userInput("Would you like to add another run?")
    run += 1