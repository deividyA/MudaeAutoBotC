import subprocess
import time

while True:
    process = subprocess.Popen(["python", "MudaeAutoBot.py"])
    process.wait()

    print("MudaeAutoBot has disconnected. Restarting in 5 seconds...")
    time.sleep(5)

    print("Restarting MudaeAutoBot...")