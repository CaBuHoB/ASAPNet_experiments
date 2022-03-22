#!/bin/bash
python train.py \
    --name cityscapes_512 --dataroot ../TheCityscapesDataset \
    --dataset_mode orig2blur --resize_or_crop scale_width \
    --learn_residual --fineSize 1024 --gan_type gan \
    --which_direction BtoA --display_id 0 \
    --save_latest_freq 1000 --save_epoch_freq 50 \
    --batchSize 2 --gpu_ids 0