import subprocess
import time

while True:
    process = subprocess.Popen(["python", "MudaeAutoBot.py"])
    process.wait()

    print("MudaeAutoBot has disconnected. Restarting in 3 seconds...")
    time.sleep(3)

    print("Restarting MudaeAutoBot...")