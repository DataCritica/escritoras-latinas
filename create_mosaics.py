import os
import subprocess
import escritoras_latinas.data.load as load

# Load data
targets_processed = load.targets_processed
imgs_processed = load.imgs_processed

# Generate file names in a directory tree
path, dirs, files = next(os.walk(f'{targets_processed}'))
# Iterate through files
for file in files:
    # Execute command to create a mosaic for each file
    subprocess.run(['python3', 'photomosaics/photomosaics/run.py', f'{targets_processed}/{file}', f'{imgs_processed}'])