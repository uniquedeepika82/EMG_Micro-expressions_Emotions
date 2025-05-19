# preprocessing_pipeline.py
# Applies filters and stores processed EMG data

import pandas as pd
import numpy as np
from filters import bandpass_filter, notch_filter, full_wave_rectify
import os

data_dir = "d:/emg_micro/data/gen/"
processed_dir = "d:/emg_micro/data/processed/"
os.makedirs(processed_dir, exist_ok=True)

for file in os.listdir(data_dir):
    if file.endswith(".csv") and not file.startswith("processed"):
        df = pd.read_csv(os.path.join(data_dir, file))

        # Extract fixed metadata columns
        timestamps = df["timestamp"]
        emotion = df["emotion_label"]
        muscle = df["muscle_name"]

        # Only EMG signal channels 
        sensor_columns = [col for col in df.columns if col.startswith("s")]
        signals = df[sensor_columns].values.astype(float)

        # filtering and rectification
        processed = []
        for i in range(signals.shape[1]):
            signal = signals[:, i]
            filtered = bandpass_filter(signal)
            filtered = notch_filter(filtered)
            rectified = full_wave_rectify(filtered)
            processed.append(rectified)

        # new DataFrame with processed signals
        processed_df = pd.DataFrame(
            np.array(processed).T,
            columns=sensor_columns
        )

        # Re-insert metadata columns
        processed_df.insert(0, "muscle_name", muscle)
        processed_df.insert(0, "emotion_label", emotion)
        processed_df.insert(0, "timestamp", timestamps)

        # Save processed file
        processed_df.to_csv(os.path.join(processed_dir, f"p_{file}"), index=False)
        print(f"Processed {file}")
