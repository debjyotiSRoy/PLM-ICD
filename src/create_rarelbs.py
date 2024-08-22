import argparse
import csv
import pandas as pd
from collections import Counter
from pathlib import Path

def compute_label_frequencies(train_file, dev_file, test_file, output_file, k=50, sort_by=None, label_delim=None):
    # Read CSV file into DataFrame
    df_train = pd.read_csv(train_file)
    df_dev = pd.read_csv(dev_file)
    df_test = pd.read_csv(test_file)
    if sort_by:
        for df in [df_train, df_dev, df_test]:
            df.sort_values(by=sort_by, inplace=True)#.reset_index(drop=True)

    # Compute label frequencies in train and dev set
    lbl_freqs = Counter()
    df = pd.concat((df_train, df_dev))
    for _,row in df.iterrows():
        if pd.notna(row.LABELS):
            lbl_freqs.update(row.LABELS.split(label_delim if label_delim is not None else ',' ))
    
    # Sort label frequencies in descending order
    lbls_sorted = sorted(lbl_freqs.items(), key=lambda item: item[1], reverse=True)

    # Save rarest `k` labels to CSV file
    rarest_labels = lbls_sorted[-k:]
    rarest_labels_list = [lbl for lbl,_ in rarest_labels]
    # import ipdb; ipdb.set_trace()
    code_file = Path(output_file).parent/(Path(output_file).name.split('.')[0] + '.txt')
    with open(output_file, "w", newline="") as csvfile, open(code_file, "w") as codefile:
        writer = csv.writer(csvfile)
        writer.writerow(["label", "frequency"])
        for label, frequency in rarest_labels:
            writer.writerow([label, frequency])
            codefile.write(f"{label}\n")  # Example code line with label

    print(f"Rarest {k} labels along with their frequncies are saved to CSV file '{output_file}'. Also, the list of labels are saved in {code_file}.")

    # Select all datapoints from train/dev/test that heave at least one of these rarest labels to create a rare dataset
    splits = ('train', 'dev', 'test')
    files = (train_file, dev_file, test_file)
    dfs = (df_train, df_dev, df_test)
    for split,input_file,df in zip(splits, files, dfs):
        df_rare = df[ 
            df.LABELS.str.split(label_delim if label_delim is not None else ',' ).apply(
                lambda o: isinstance(o, list) and (True if set(o).intersection(lbl for lbl, _ in rarest_labels) else False)
            ) 
        ]
        # Filtering only rarest labels in df_rare
        df_rare.loc[:, 'LABELS'] = df_rare.LABELS.str.split(label_delim if label_delim is not None else ',' ).apply(
            lambda labels: label_delim.join([label for label in labels if label in rarest_labels_list])
        )

        input_path = Path(input_file)
        rare_fname = input_path.name.split('.')[0] + f'_rare{k}.' + input_path.name.split('.')[1]
        rare_fname = input_path.parent/rare_fname
        df_rare.to_csv(rare_fname)
        print(f"Rare dataset for {split} of size {len(df_rare)} based off of {k} rareset labels saved to CSV file '{rare_fname}'.")

def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Compute label frequencies on the training set and save rarest 50 labels to a CSV file.")
    # Add arguments
    parser.add_argument("--train_file", help="Path to the input train CSV file.")
    parser.add_argument("--dev_file", help="Path to the input dev CSV file.")
    parser.add_argument("--test_file", help="Path to the input test CSV file.")
    parser.add_argument("--k", help="rarest k labels.")
    parser.add_argument("--output_file", help="Path to the output CSV file containing the rarest `k` labels and their frequencies."),
    parser.add_argument("--sort_by", help="Sort by field in the input CSV file."),
    parser.add_argument("--label_delim", help="label delimiter in the input file.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Compute label frequencies and save rarest labels to CSV file and create a rare dataset based off of rarest labels
    compute_label_frequencies(args.train_file, args.dev_file, args.test_file, args.output_file, int(args.k), args.sort_by, args.label_delim)


if __name__ == "__main__":
    main()