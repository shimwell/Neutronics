

# build with
# docker build -t neutronics .
# run with
# docker run -v $PWD:/shared_folder -it neutronics


FROM continuumio/miniconda3:4.10.3

# ghcr.io/openmc-data-storage/miniconda3_4.9.2_endfb-7.1_nndc_tendl_2019

RUN apt-get --allow-releaseinfo-change update
RUN apt-get install -y libgl1-mesa-glx libgl1-mesa-dev libglu1-mesa-dev freeglut3-dev libosmesa6 libosmesa6-dev libgles2-mesa-dev

RUN conda install -c conda-forge mamba
RUN mamba install -c cadquery -c conda-forge cadquery==master
# RUN mamba install -c fusion-energy -c cadquery -c conda-forge paramak
RUN mamba install -c fusion-energy -c cadquery -c conda-forge brep_to_h5m brep_part_finder
RUN mamba install -c fusion-energy -c cadquery -c conda-forge paramak
# needs dagmc as well
RUN mamba install -c conda-forge openmc


COPY monoblock_salu_2.py .
