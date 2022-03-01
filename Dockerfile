

# build with
# docker build -t neutronics .
# run with
# docker run -p 8888:8888 neutronics


FROM ghcr.io/fusion-energy/neutronics-workshop:dependencies

COPY monoblock_salu.ipynb .


CMD ["jupyter", "lab", "--notebook-dir=/", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
