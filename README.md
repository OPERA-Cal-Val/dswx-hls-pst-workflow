# Workflow to obtain DSWx-HLS

See: https://github.com/nasa/PROTEUS

Basically, use the notebook to take an HLS_ID and output a DSWx Product.


## Installation and Setup.

Clone this repository and navigate to it. Create an `.env` file in this directory with your earthdata username and password as:

```
ED_USERNAME=<USERNAME>
ED_PASSWORD=<PASSWORD>
```

1. `mamba env update -f environment.yml`
2. `conda activate dswx_hls_generation`
3. `python -m ipykernel install --user --name dswx_hls_generation`
4. `jupyter-lab` and open the workflow notebook

This only works specifying a single HLS IDs. All the necessary datasets are localized.