#!/bin/bash
python3 run_icd.py \
    --train_file ../data/mimic3/train_full.csv \
    --validation_file ../data/mimic3/test_full.csv \
    --max_length 3072 \
    --chunk_size 128 \
    --model_name_or_path ../models/roberta-mimic3-full \
    --per_device_eval_batch_size 8 \
    --num_train_epochs 0 \
    --output_dir ../models/roberta-mimic3-full \
    --model_type roberta \
    --model_mode laat \
    --logfile log
