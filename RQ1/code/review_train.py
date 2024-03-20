import pandas as pd
import random


def read_file(path, train_path, val_path):
    df = pd.DataFrame(pd.read_excel(path))
    contents = [f"{row['content']}" for index, row in df.iterrows()]
    label = []
    for value in df['label']:
        if value == 1:
            label.append('相关')
        elif value == 0:
            label.append('无关')

    re_review = []
    ir_review = []
    re_num = 0
    for index in range(len(contents)):
        if label[index] == '相关':
            re_review.append(label[index] + '\t' + contents[index])
            re_num += 1
        if label[index] == '无关':
            ir_review.append(label[index] + '\t' + contents[index])

    random.shuffle(ir_review)

    review = []
    for i in range(len(re_review)):
        review.append(re_review[i] + '\n')
        review.append(ir_review[i] + '\n')

    random.shuffle(review)

    sample_size = int(len(review) * 0.7)

    sample_indices = random.sample(range(len(review)), sample_size)

    sample_lines = [review[i] for i in sample_indices]
    remaining_indices = set(range(len(review))) - set(sample_indices)
    remaining_lines = [review[i] for i in remaining_indices]

    with open(train_path, 'w', encoding='utf-8') as file:
        file.writelines(sample_lines)
    with open(val_path, 'w', encoding='utf-8') as file:
        file.writelines(remaining_lines)

    print('done')


if __name__ == '__main__':
    path = '../data/tencent_manu.xlsx'
    train_path = '../data/tencent_train.txt'
    val_path = '../data/tencent_val.txt'

    # path = '../data/douyin_manu.xlsx'  
    # train_path = '../data/douyin_train.txt'  
    # val_path = '../data/douyin_val.txt'

    # path = '../data/dingding_manu.xlsx'
    # train_path = '../data/dingding_train.txt'  
    # val_path = '../data/dingding_val.txt'

    # path = '../data/dingding_manu.xlsx'
    # train_path = '../data/dingding_train.txt'  
    # val_path = '../data/dingding_val.txt'

    # path = '../data/keep_manu.xlsx'
    # train_path = '../data/keep_train.txt'  
    # val_path = '../data/keep_val.txt'

    # path = '../data/zoom_manu.xlsx'
    # train_path = '../data/zoom_train.txt'  
    # val_path = '../data/zoom_val.txt'  

    read_file(path, train_path, val_path)
