#!/bin/bash
export MIMIC_3_DIR=../data/mimic3
python create_mimic_few.py \
    --train_file $MIMIC_3_DIR/train_full.csv \
    --dev_file $MIMIC_3_DIR/dev_full.csv \
    --test_file $MIMIC_3_DIR/test_full.csv \
    --output_file $MIMIC_3_DIR/rarelbs.csv \
    --sort_by SUBJECT_ID \
    --label_delim \;