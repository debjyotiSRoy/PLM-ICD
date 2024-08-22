#!/bin/bash
python3 run_icd.py \
    --train_file ../data/mimic3/train_few.csv \
    --validation_file ../data/mimic3/dev_few.csv \
    --max_length 3072 \
    --chunk_size 128 \
    --model_name_or_path ../models/RoBERTa-base-PM-M3-Voc-distill-align-hf \
    --per_device_train_batch_size 2 \
    --gradient_accumulation_steps 8 \
    --per_device_eval_batch_size 1 \
    --num_train_epochs 20 \
    --num_warmup_steps 2000 \
    --output_dir ../models/roberta-mimic3-fewshot \
    --model_type roberta \
    --model_mode laat \
    --code_file ../data/mimic3/rarelbs.txt
