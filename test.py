#!/usr/bin/env

import z5py
from datetime import datetime
fpath = datetime.now().isoformat() + '.n5'

f = z5py.File(fpath, use_zarr_format=False)

