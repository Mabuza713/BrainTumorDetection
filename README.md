
# Brain Tumor Detection

This project implements a deep learning model for detecting brain tumors in MRI images using TensorFlow and Keras.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [Model Training](#model-training)
- [Prediction](#prediction)
- [Contributing](#contributing)

## Overview

This project consists of two main components:

1. A training script (`BrainTumorTrain.py`) that prepares the dataset, builds and trains the neural network models.
2. A detection script (`BrainTumorDetection.py`) that uses the trained models to predict the presence of brain tumors in new images.

The system can be trained to perform both binary classification (tumor present or not) and categorical classification.

## Requirements

To run this project, you'll need:

- Python 3.x
- TensorFlow
- Keras
- OpenCV (cv2)
- NumPy
- Pillow (PIL)
- scikit-learn

You can install the required packages using pip:

```bash
pip install tensorflow keras opencv-python numpy pillow scikit-learn
```

## Usage

1. Prepare your dataset by placing MRI images in the appropriate directories:
   - Images without tumors in `BrainTumorDetection/no/`
   - Images with tumors in `BrainTumorDetection/yes/`

2. Train the models using `BrainTumorTrain.py`
3. Use the trained models to make predictions with `BrainTumorDetection.py`

## Model Training

To train the models, run:

```bash
python BrainTumorTrain.py
```

This script will:
1. Load and preprocess the images
2. Split the data into training and testing sets
3. Build and train both binary and categorical classification models
4. Save the trained models as `.h5` files in the `BrainTumorDetection/` directory

You can adjust the `size` and `epochsAmount` parameters in the script to modify the input image size and the number of training epochs.

## Prediction

To use the trained models for prediction, use the `BrainTumorDetection` class in `BrainTumorDetection.py`:

```python
from BrainTumorDetection import BrainTumorDetection

# Initialize the detector
detector = BrainTumorDetection(size=64)

# Make a prediction
detector.PrepareImage("BrainTumorDetection/pred/image_to_predict.jpg")
```

The `PrepareImage` method will print the prediction result:
- A value close to 0 indicates no tumor
- A value close to 1 indicates the presence of a tumor

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.
