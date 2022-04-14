# Installation Instructions

## Calypso server - 172.31.1.154

This project uses multiple external libraries and packages, please follow the installation instructions precisely to avoid future problems (Note that Anaconda is required to install the project dependencies):

1. Create empty conda environment with Python 3.8 >>

    `source ~/.bashrc`

    `conda create --name NeRF-3D python=3.8`

    `conda activate NeRF-3D`

2. Install Pytorch + CUDA + Pytorch-lightning >>

    `conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch`

    `pip install pytorch-lightning`

3. Clone the project repository and switch to dev branch >>

    `git clone git@github.com:ceballos-alberto/NeRF-3D.git` or `git clone https://github.com/ceballos-alberto/NeRF-3D.git`

    `cd NeRF-3D`

    `git checkout dev`

4. Install other project dependencies >>

    `pip install -r requirements.txt`

## Gaston server - 172.31.1.150

This project uses multiple external libraries and packages, please follow the installation instructions precisely to avoid future problems (Note that Anaconda is required to install the project dependencies):

1. Create empty conda environment with Python 3.8 >>

    `conda create --name NeRF-3D python=3.8`

    `conda activate NeRF-3D`

2. Install Pytorch + CUDA + Pytorch-lightning >>

    `conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch`

    `pip install pytorch-lightning`

3. Clone the project repository and switch to dev branch >>

    `git clone git@github.com:ceballos-alberto/NeRF-3D.git` or `git clone https://github.com/ceballos-alberto/NeRF-3D.git`

    `cd NeRF-3D`

    `git checkout dev`

4. Install other project dependencies >>

    `pip install -r requirements.txt`

# Uninstallation Instructions

All the libraries and packages that we have previously installed are inside a conda environment, please follow the uninstallation instructions precisely to avoid future problems:

1. Deactivate current conda environment (skip this step if the current environment is base) >>

    `conda deactivate`

2. Remove the environment >>

    `conda env remove -n NeRF-3D`

3. Remove repository files >>

    `cd ..`

    `rm -r NeRF-3D`
