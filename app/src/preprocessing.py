# Import libraries
import pandas as pd
import numpy as np

# Define column types
target_col = 'binary_target'
drop_col = ["зона_1", "зона_2", "mrg_", "client_id"]

def import_data(path_to_file):

    # Get input dataframe
    input_df = pd.read_csv(path_to_file).drop(columns=drop_col , axis=1)

    return input_df

def transform_skew(data, method='log1p'):
    if method == 'log1p':
        return np.log1p(data)
    elif method == 'sqrt':
        return np.sqrt(data)

# Main preprocessing function
def run_preproc(input_df):


    input_df['регион'].fillna('Missing', inplace=True)
    input_df['pack'].fillna('Missing', inplace=True)
    input_df['сумма'].fillna(0, inplace=True)
    input_df['частота_пополнения'].fillna(0, inplace=True)
    input_df['доход'].fillna(0, inplace=True)
    input_df['сегмент_arpu'].fillna(0, inplace=True)
    input_df['частота'].fillna(0, inplace=True)
    input_df['объем_данных'].fillna(0, inplace=True)
    input_df['on_net'].fillna(0, inplace=True)
    input_df['продукт_1'].fillna(0, inplace=True)
    input_df['продукт_2'].fillna(0, inplace=True)
    input_df['pack_freq'].fillna(0, inplace=True)
    input_df['регион'].fillna('Missing', inplace=True)
    input_df['pack'].fillna('Missing', inplace=True)

    skewed_cols = ['частота_пополнения', 'сегмент_arpu', 'объем_данных', 'on_net', 'продукт_1', 'продукт_2', 'секретный_скор', 'pack_freq']
    skewed_cols_log = ['частота_пополнения_log', 'сегмент_arpu_log', 'объем_данных_log', 'on_net_log', 'продукт_1_log', 'продукт_2_log', 'секретный_скор_log', 'pack_freq_log']
    skewed_cols_sqrt = ['частота_пополнения_sqrt', 'сегмент_arpu_sqrt', 'объем_данных_sqrt', 'on_net_sqrt', 'продукт_1_sqrt', 'продукт_2_sqrt', 'секретный_скор_sqrt', 'pack_freq_sqrt']
    input_df[skewed_cols_log] = input_df[skewed_cols].apply(lambda x: transform_skew(x))
    input_df[skewed_cols_sqrt] = input_df[skewed_cols].apply(lambda x: transform_skew(x, method='sqrt'))


    if target_col in input_df:
        features = input_df.drop('binary_target', axis=1)
    else:
        features = input_df

    categorical_features = features.select_dtypes(include=['object']).columns

    for col in categorical_features:
        value_counts = features[col].value_counts()
        total_count = len(features)
        freq_map = (value_counts + 1) / (total_count + len(value_counts))
        features[col] = features[col].map(freq_map)

    # Return resulting dataset
    return features 