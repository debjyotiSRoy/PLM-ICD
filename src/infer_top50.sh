#!/bin/bash
python3 run_icd.py \
    --train_file ../data/mimic3/train_50.csv \
    --validation_file ../data/mimic3/test_50.csv \
    --max_length 3072 \
    --chunk_size 128 \
    --model_name_or_path ../models/RoBERTa-base-PM-M3-Voc-distill-align-hf \
    --per_device_eval_batch_size 8 \
    --num_train_epochs 0 \
    --output_dir ../models/roberta-mimic3-top50 \
    --model_type roberta \
    --model_mode laat \
    --code_50 \
    --code_file ../data/mimic3/ALL_CODES_50.txt \
    --logfile log
