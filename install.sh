#!/bin/sh

# Run this script from Home #

# 1. make the script executable >> chmod +x install.sh #
# 2. Run the script >> ./install.sh #

# This project uses multiple external libraries and packages, please follow the installation instructions precisely to avoid future problems: #

source ~/.bashrc
conda create --name NeRF-3D python=3.9
conda activate NeRF-3D
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
pip install pytorch-lightning
git clone git@github.com:ceballos-alberto/NeRF-3D.git
cd NeRF-3D
git checkout dev
pip install -r requirements.txt

# Everything has been installed #
