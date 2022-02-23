

# build with
# docker build -t neutronics .
# run with
# docker run -v $PWD:/shared_folder -it neutronics


FROM continuumio/miniconda3:4.10.3

# ghcr.io/openmc-data-storage/miniconda3_4.9.2_endfb-7.1_nndc_tendl_2019

RUN apt-get --allow-releaseinfo-change update
RUN apt-get install -y libgl1-mesa-glx libgl1-mesa-dev libglu1-mesa-dev freeglut3-dev libosmesa6 libosmesa6-dev libgles2-mesa-dev

RUN conda install -c conda-forge mamba

RUN mamba install -c fusion-energy -c cadquery -c conda-forge paramak_develop

# this needs dagmc as well, which we are working on
RUN mamba install -c conda-forge openmc

