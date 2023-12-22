from pathlib import Path

import geopandas as gpd
import papermill as pm
from tqdm import tqdm

df_val = gpd.read_file('https://raw.githubusercontent.com/OPERA-Cal-Val/DSWx-Requirement-Verification/dev/dswx_verification/data/validation_table.geojson')
hls_ids = df_val.hls_id

TEMPLATE_NB = '0-Run-DSWX-HLS.ipynb'
NB_OUT_DIR = Path('out_notebooks')
NB_OUT_DIR.mkdir(exist_ok=True, parents=True)

for aerosol_param in [True, False]:
    for hls_id in tqdm(hls_ids):
        print(hls_id)
        aero_token = 'on' if aerosol_param else 'off'
        pm.execute_notebook(TEMPLATE_NB,
                            NB_OUT_DIR / f'{hls_id}-aerosol_{aero_token}.ipynb',
                            parameters=dict(HLS_ID_OR_HLS_DIR_PATH=hls_id,
                                            OUT_DIR=f'out-aerosol_{aero_token}',
                                            DOWNLOAD_HLS=True,
                                            AEROSOL_PARAM=aerosol_param))
