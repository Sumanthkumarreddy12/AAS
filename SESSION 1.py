# Install required libraries
!pip install pandas numpy

import os
import pandas as pd
import numpy as np
import urllib.request
import zipfile

# Step 1: Download UCI HAR Dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI%20HAR%20Dataset.zip"
zip_path = "har.zip"

urllib.request.urlretrieve(url, zip_path)

# Step 2: Extract Dataset
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall()

# Step 3: Load Motion Features (Accelerometer Data)
data_path = "UCI HAR Dataset/train/Inertial Signals/body_acc_z_train.txt"
motion_data = pd.read_csv(data_path, delim_whitespace=True, header=None)

# Step 4: Extract Velocity Proxy
velocity = motion_data.mean(axis=1)

# Step 5: Extract Altitude Proxy (simulated using variance)
altitude = motion_data.var(axis=1)

# Step 6: Rule-Based Classifier
def classify_robot(alt):
    if alt > 0:
        return "Aerial Autonomous Robot"
    else:
        return "Ground Robot"

robot_type = classify_robot(altitude.mean())

# Step 7: Output
print("Robot Type:", robot_type)
print("Industry: NVIDIA Jetson Drone Systems")
OUTPUT:
Requirement already satisfied: pandas in /usr/local/lib/python3.12/dist-packages (2.2.2)
Requirement already satisfied: numpy in /usr/local/lib/python3.12/dist-packages (2.0.2)
Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.3)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)
/tmp/ipython-input-357/4033047065.py:22: FutureWarning: The 'delim_whitespace' keyword in pd.read_csv is deprecated and will be removed in a future version. Use ``sep='\s+'`` instead
  motion_data = pd.read_csv(data_path, delim_whitespace=True, header=None)
Robot Type: Aerial Autonomous Robot
Industry: NVIDIA Jetson Drone Systems
