import subprocess
import threading

def dummy():
    subprocess.run(["bash","test.sh"])

print("Start")

threading.Thread(target=dummy)

print("Finished")
