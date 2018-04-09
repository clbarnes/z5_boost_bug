#!/usr/bin/env

import os
import logging
from datetime import datetime
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.info('importing z5py')

import z5py
logger.info('imported z5py')

file_path = datetime.now().isoformat() + '.n5'

logger.info('creating File')
f = z5py.File(file_path, use_zarr_format=False)
logger.info('created File')
assert os.path.isdir(file_path), "z5py did not create dir at " + file_path

logger.info('creating Dataset')
ds = f.create_dataset('ds', shape=(10, 10, 10), dtype='uint8', chunks=(1, 10, 10))
logger.info('created Dataset')
ds_path = os.path.join(file_path, 'ds')
assert os.path.isdir(ds_path), "z5py did not create dir at " + ds_path

