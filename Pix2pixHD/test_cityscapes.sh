#!/bin/bash
python test.py --name cityscapes_512 --dataroot ../TheCityscapesDataset --batchSize 1 --gpu_ids 0 --phase test --netG local --ngf 32