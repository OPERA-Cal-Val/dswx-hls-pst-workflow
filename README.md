# Workflow to obtain DSWx-HLS

See: https://github.com/nasa/PROTEUS

Basically, use the notebook to take an HLS_ID and output a DSWx Product.


## Installation

1. Clone this repository and navigate to it.
2. `mamba env update -f environment.yml`
3. `conda activate dswx_hls`
4. `python -m ipykernel install --user --name dswx_hls`
5. `jupyter-lab` and open the Workflow

This only works specifying a single HLS IDs. All the necessary datasets are localized.