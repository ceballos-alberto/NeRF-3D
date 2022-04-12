# Installation Instructions

This project uses multiple external libraries and packages, please follow the installation instructions precisely to avoid future problems:

1. Create empty conda environment with Python 3.9 >>

    `source ~/.bashrc`

    `conda create --name NeRF-3D python=3.9`

    `conda activate NeRF-3D`

2. Install Pytorch + CUDA + Pytorch-lightning >>

    `conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch`

    `pip install pytorch-lightning`

3. Clone the project repository and switch to dev branch >>

    `git clone git@github.com:ceballos-alberto/NeRF-3D.git`

    `cd NeRF-3D`

    `git checkout dev`

4. Install other project dependencies >>

    `pip install -r requirements.txt`

5. For convenience you can execute all the steps described above using the installation script that has been provided

    `chmod +x install.sh`

    `./install.sh`
