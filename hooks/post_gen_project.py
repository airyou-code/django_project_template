# This script is executed after the project generation process is complete.
# It will make the 'start.sh' script executable and then run it.

import os
import subprocess

# Notify the user that the start.sh script will be run.
print("Running the start.sh script...")

# Make sure that the start.sh script is executable
# os.path.curdir refers to the current directory
start_script_path = os.path.join(os.path.curdir, 'start.sh')
# Add execute permission to the start.sh script
os.chmod(start_script_path, os.stat(start_script_path).st_mode | 0o111)

# Run the start.sh script using subprocess to call the shell command
result = subprocess.run(['./start.sh'], check=True)

# Check the result of the script execution
if result.returncode == 0:
    print("Script executed successfully.")
else:
    print("Script failed to execute.")
