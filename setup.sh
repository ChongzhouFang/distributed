[ -f Anaconda3-2023.07-2-Linux-x86_64.sh ] || wget -b https://repo.continuum.io/archive/Anaconda3-2023.07-2-Linux-x86_64.sh
bash Anaconda3-2023.07-2-Linux-x86_64.sh -b -p ~/anaconda3
echo 'eval "(~/anaconda3/bin/conda shell.bash hook)"' >> ~/.bashrc
source ~/.bashrc
conda --version