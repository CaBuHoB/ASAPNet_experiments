#!/bin/bash
python train.py --name cityscapes_512 --dataroot ../TheCityscapesDataset --dataset_mode cityscapes --batchSize 2 --gpu_ids 0 --print_freq 500