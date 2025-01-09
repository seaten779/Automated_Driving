# Automated_Driving
This project uses [NVIDIA's](https://arxiv.org/pdf/1604.07316) End-to-End Learning for Self-Driving Cars model, enhanced with dropout layers to optimize performance on smaller datasets. The framework offers accurate steering angle prediction and combines a YOLO-based segmentation model for accurate road object identification.

# Dataset used for training YOLO model 
https://universe.roboflow.com/sue-ergdx/l-s-kvbur-z1sqm/dataset/1

# Dataset used 
https://github.com/SullyChen/driving-datasets

# How to use 
1. Download the dataset

2.Create a virtual enviroment 
-- Using venv:
  `
  python -m venv env
  source env/bin/activate  #Linux/Mac
  .\env\Scripts\activate   #Windows
  `
-- Using conda: 
  `
  conda create --name auto_driving_env python=3.8
  conda activate auto_driving_env
  `
  
3.Install Dependencies
  `
  python setup.py install
  `
  
4.Run the Applicatio
  `
  python run_auto_driving.py
  `
