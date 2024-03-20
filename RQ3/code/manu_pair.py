import pandas as pd


def getTrainpair(path, write_path):
    df = pd.DataFrame(pd.read_excel(path))
    feature = []
    review = []
    label = []
    for row, index in df.iterrows():
        feature.append(index['feature'])
        review.append(index['review'])
        label.append(index['label'])

    for index in range(len(label)):
        if label[index] == 1:
            label[index] = '相关'
        if label[index] == 0:
            label[index] = '无关'

    with open(write_path, 'w', encoding='utf-8') as f:
        for index in range(len(label)):
            if label[index] == '相关':
                f.write(feature[index])
                f.write('\t')
                f.write(review[index])
                f.write('\t')
                f.write(label[index])
                f.write('\n')
    print('done')


if __name__ == '__main__':
    path = 'RQ2/tencent_pair_manu.xlsx'
    write_path = '../data/tencent_pair_manu.txt'

    # path = 'RQ2/douyin_pair_manu.xlsx'
    # write_path = '../data/douyin_pair_manu.txt'

    # path = 'RQ2/dingding_pair_manu.xlsx'
    # write_path = '../data/dingding_pair_manu.txt'

    # path = 'RQ2/keep_pair_manu.xlsx'
    # write_path = '../data/keep_pair_manu.txt'

    # path = 'RQ2/zoom_pair_manu.xlsx'
    # write_path = '../data/zoom_pair_manu.txt'
    getTrainpair(path, write_path)
