#!/bin/bash
python3 run_icd.py \
    --train_file ../data/mimic3/train_few.csv \
    --dev_file ../data/mimic3/dev_few.csv \
    --validation_file ../data/mimic3/test_few.csv \
    --max_length 3072 \
    --chunk_size 128 \
    --model_name_or_path ../models/RoBERTa-base-PM-M3-Voc-distill-align-hf \
    --per_device_eval_batch_size 1 \
    --num_train_epochs 0 \
    --output_dir ../models/roberta-mimic3-fewshot \
    --model_type roberta \
    --model_mode laat \
    --code_file ../data/mimic3/rarelbs.txt \
    --logfile log
