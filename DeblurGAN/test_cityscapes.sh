#!/bin/bash
python test.py \
    --name cityscapes_512 --dataroot ../TheCityscapesDataset \
    --dataset_mode orig2blur --resize_or_crop scale_width \
    --learn_residual --fineSize 1024 --gan_type gan \
    --which_direction BtoA --display_id 0 \
    --serial_batches --no_flip --nThreads 1  --model test \
    --batchSize 1 --gpu_ids 0