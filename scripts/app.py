
import subprocess
import time
import os

def run_programs():
    python_executable = os.path.join("..", "py", "python")
    subprocess.Popen([python_executable, "../backend.py"])
    time.sleep(2)  # Wait for 2 seconds
    gui_process = subprocess.Popen([python_executable, "gui.py"])
    gui_process.wait()  # Wait for the GUI process to finish

if __name__ == "__main__":
    run_programs()
