# EMG-Based Novel Micro-Expression Validation

This repository contains the full implementation of the experimental pipeline to validate novel micro-expressions using EMG (Electromyography) signals. It includes Arduino code for data acquisition, Python scripts for filtering and preprocessing, and structured data storage ready for machine learning tasks.

---

## 📁 Repository Structure

emg_microexpression_project/
│
├── data/
│ └── emg_dataset.csv # Raw EMG data
│
├── metadata/
│ └── channel_mapping.csv # EMG channel to muscle mapping
│
├── arduino/
│ └── emg_acquisition.ino # Arduino sketch for serial EMG data
│
├── src/
│ ├── data_collection.py # Python script to collect and store EMG data
│ ├── filters.py # Bandpass, notch, and rectification filters
│ └── preprocessing_pipeline.py # Filter and preprocess raw EMG signals
│
├── notebooks/
│ └── signal_processing_demo.ipynb # Visualization of filtering steps
│
├── README.md # Repository overview and usage
└── requirements.txt # Python dependencies