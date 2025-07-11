import os
import time
import numpy as np
from sense_hat import SenseHat

print("Choose a gesture:")
print("1. none")
print("2. circle")
print("3. shake")
print("4. twist")

a = input("Enter the number for each gesture: ")

if a == "1":
    LABEL = "move_none"
elif a == "2":
    LABEL = "move_circle"
elif a == "3":
    LABEL = "move_shake"
elif a == "4":
    LABEL = "move_twist"
else:
    print("Invalid input. Defaulting to 'move_none'")
    LABEL = "move_none"

sense = SenseHat()
SAMPLES = 50  # number of samples per file (for 1 second)
FREQ_HZ = 50
DELAY = 1.0 / FREQ_HZ

save_dir = f"./motion_data/{LABEL}"
os.makedirs(save_dir, exist_ok=True)

print(f"\nRecording 55 data files for label: {LABEL}")
try:
    for i in range(55):
        input(f"\n[{i+1}/55] Press Enter to record 1 second of data...")
        data = []
        for _ in range(SAMPLES):
            acc = sense.get_accelerometer_raw()
            gyro = sense.get_gyroscope_raw()
            sample = [
                acc['x'], acc['y'], acc['z'],
                gyro['x'], gyro['y'], gyro['z']
            ]
            data.append(sample)
            time.sleep(DELAY)
        timestamp = int(time.time())
        filename = f"{LABEL}_{timestamp}.npy"
        np.save(os.path.join(save_dir, filename), np.array(data))
        print(f"Saved {filename}")
    print("\n✅ Finished recording 55 samples.")
except KeyboardInterrupt:
    print("\nRecording interrupted by user.")
