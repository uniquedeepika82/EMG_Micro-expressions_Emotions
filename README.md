
# EMG-Based Novel Micro-Expression Validation

This repository contains the full implementation of the experimental pipeline to validate **novel micro-expressions** using **EMG (Electromyography)** signals.

It includes:
- Arduino code for data acquisition
- Python scripts for signal filtering (bandpass, notch), rectification, and preprocessing
- Structured data storage ready for machine learning pipelines

## Repository Structure

emg_microexpression_project/
├── data/
│   └── emg_dataset.csv               # Raw EMG data
│
├── metadata/
│   └── channel_mapping.csv           # EMG channel to muscle mapping
│
├── arduino/
│   └── emg_acquisition.ino           # Arduino sketch for serial EMG data
│
├── src/
│   ├── data_collection.py            # Python script to collect and store EMG data
│   ├── filters.py                    # Bandpass, notch, and rectification filters
│   └── preprocessing_pipeline.py     # Preprocess raw EMG signals
│
├── notebooks/
│   └── signal_processing_demo.ipynb  # Visualization of filtering steps
│
├── README.md                         # Project overview and instructions
└── requirements.txt                  # Python dependencies

## Hardware Setup

- **Microcontroller**: Arduino 
- **EMG Sensor**: 
- **Channels**: 8
- **Subjects**: 15 participants
- **Emotions**: Happy, Sad, Angry, Fear, Surprise, Disgust

---

## Data Acquisition

1. emg_acquisition.ino
2. EMG sensors connection to analog pins (e.g., A0, A1).
3. data_collection.py to capture data via serial.
4. Recording of each subject's signal data for all 6 emotion stimuli.

---

## Preprocessing Pipeline

preprocessing_pipeline.py

This will apply:
- Bandpass Filter
- Notch Filter 
- Full-Wave Rectification for EMG envelope
- Outputs structured CSV for ML training

## Machine Learning Ready

The final dataset is structured for ML with columns like:

- `Timestamp`, `Subject_ID`, `Emotion`, `Channel`, `Raw_Signal`, `Filtered_Signal`

Feature Extraction:
- Mean
- Standard Deviation
