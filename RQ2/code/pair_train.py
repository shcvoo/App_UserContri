import pandas as pd
import random


def divide_t_v(anno_path, train_path, val_path):
    df = pd.read_excel(anno_path)
    re_pair = [f"{row['feature'][11:]}\t{row['review'][11:]}\t相关\n" for index, row in df.iterrows() if
               row['label'] == 1]
    ir_pair = [f"{row['feature'][11:]}\t{row['review'][11:]}\t无关\n" for index, row in df.iterrows() if
               row['label'] == 0]
    pair = re_pair + ir_pair
    random.shuffle(pair)

    print("get pair done")

    sample_indices = random.sample(range(len(pair)), int(len(pair) * 0.7))

    sample_lines = [pair[i] for i in sample_indices]
    remaining_indices = set(range(len(pair))) - set(sample_indices)
    remaining_lines = [pair[i] for i in remaining_indices]

    with open(train_path, 'w', encoding='utf-8') as file:
        file.writelines(sample_lines)
    with open(val_path, 'w', encoding='utf-8') as file:
        file.writelines(remaining_lines)

    print('done')


if __name__ == '__main__':
    anno_path = '../data/tencent_pair_manu.xlsx'
    train_path = '../data/tencent_train.txt'
    val_path = '../data/tencent_val.txt'
    
    # anno_path = '../data/douyin_pair_manu.xlsx'
    # train_path = '../data/douyin_train.txt'
    # val_path = '../data/douyin_val.txt'
    
    # anno_path = '../data/dingding_pair_manu.xlsx'
    # train_path = '../data/dingding_train.txt'
    # val_path = '../data/dingding_val.txt'
    
    # anno_path = '../data/keep_pair_manu.xlsx'
    # train_path = '../data/keep_train.txt'
    # val_path = '../data/keep_val.txt'
    
    # anno_path = '../data/zoom_pair_manu.xlsx'
    # train_path = '../data/zoom_train.txt'
    # val_path = '../data/zoom_val.txt'
    
    divide_t_v(anno_path, train_path, val_path)