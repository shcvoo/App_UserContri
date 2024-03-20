import pandas as pd


def predict_pair(review_path, feature_path, with_date_path, for_predict_path):
    df = pd.read_excel(review_path)
    review = [str(row['date'])[:10] + '-' + str(row['content']) for index, row in df.iterrows() if
              row['label'] == 1]

    with open(feature_path, 'r', encoding='utf-8') as f:
        feature = [line.strip() for line in f]

    with open(with_date_path, 'w', encoding='utf-8') as f:
        for fea_index in range(len(feature)):
            for rev_index in range(len(review)):
                f.write(feature[fea_index])
                f.write('\t')
                f.write(review[rev_index])
                f.write('\n')
    f.close()
    print("file with date write done")

    with open(for_predict_path, 'w', encoding='utf-8') as f:
        for fea_index in range(len(feature)):
            for rev_index in range(len(review)):
                f.write(feature[fea_index][11:])
                f.write('\t')
                f.write(review[rev_index][11:])
                f.write('\n')
    f.close()
    print("file for predict write done")


if __name__ == '__main__':
    review_path = 'else_review/tencent_else_review.xlsx'
    feature_path = 'feature/tencent.txt'
    with_date_path = '../data/tencent_remain_date.txt'
    for_predict_path = '../data/tencent_for_predict.txt'

    # review_path = 'else_review/douyin_else_review_part1.xlsx'
    # feature_path = 'feature/douyin.txt'
    # with_date_path = '../data/douyin_remain_date1.txt'
    # for_predict_path = '../data/douyin_for_predict1.txt'

    # review_path = 'else_review/douyin_else_review_part2.xlsx'
    # feature_path = 'feature/douyin.txt'
    # with_date_path = '../data/douyin_remain_date2.txt'
    # for_predict_path = '../data/douyin_for_predict2.txt'

    # review_path = 'else_review/douyin_else_review_part3.xlsx'
    # feature_path = 'feature/douyin.txt'
    # with_date_path = '../data/douyin_remain_date3.txt'
    # for_predict_path = '../data/douyin_for_predict3.txt'

    # review_path = 'else_review/douyin_else_review_part4.xlsx'
    # feature_path = 'feature/douyin.txt'
    # with_date_path = '../data/douyin_remain_date4.txt'
    # for_predict_path = '../data/douyin_for_predict4.txt'

    # review_path = 'else_review/douyin_else_review_part5.xlsx'
    # feature_path = 'feature/douyin.txt'
    # with_date_path = '../data/douyin_remain_date5.txt'
    # for_predict_path = '../data/douyin_for_predict5.txt'

    # review_path = 'else_review/dingding_else_review.xlsx'
    # feature_path = 'feature/dingding1.txt'
    # with_date_path = '../data/dingding_remain_date1.txt'
    # for_predict_path = '../data/dingding_for_predict1.txt'

    # review_path = 'else_review/dingding_else_review.xlsx'
    # feature_path = 'feature/dingding2.txt'
    # with_date_path = '../data/dingding_remain_date2.txt'
    # for_predict_path = '../data/dingding_for_predict2.txt'

    # review_path = 'else_review/dingding_else_review.xlsx'
    # feature_path = 'feature/dingding3.txt'
    # with_date_path = '../data/dingding_remain_date3.txt'
    # for_predict_path = '../data/dingding_for_predict3.txt'

    # review_path = 'else_review/dingding_else_review.xlsx'
    # feature_path = 'feature/dingding4.txt'
    # with_date_path = '../data/dingding_remain_date4.txt'
    # for_predict_path = '../data/dingding_for_predict4.txt'

    # review_path = 'else_review/dingding_else_review.xlsx'
    # feature_path = 'feature/dingding5.txt'
    # with_date_path = '../data/dingding_remain_date5.txt'
    # for_predict_path = '../data/dingding_for_predict5.txt'

    # review_path = 'else_review/dingding_else_review.xlsx'
    # feature_path = 'feature/dingding3.txt'
    # with_date_path = '../data/dingding_remain_date6.txt'
    # for_predict_path = '../data/dingding_for_predict6.txt'

    # review_path = 'else_review/dingding_else_review.xlsx'
    # feature_path = 'feature/dingding4.txt'
    # with_date_path = '../data/dingding_remain_date7.txt'
    # for_predict_path = '../data/dingding_for_predict7.txt'

    # review_path = 'else_review/dingding_else_review.xlsx'
    # feature_path = 'feature/dingding5.txt'
    # with_date_path = '../data/dingding_remain_date8.txt'
    # for_predict_path = '../data/dingding_for_predict8.txt'

    # review_path = 'else_review/zoom_else_review.xlsx'
    # feature_path = 'feature/zoom.txt'
    # with_date_path = '../data/zoom_remain_date.txt'
    # for_predict_path = '../data/zoom_for_predict.txt'

    predict_pair(review_path, feature_path, with_date_path, for_predict_path)
