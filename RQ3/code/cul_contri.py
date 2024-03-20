from ordered_set import OrderedSet


def change_pair_format(read_path):
    unique_feature = OrderedSet()
    feature_review_dict = {}

    with open(read_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            strip_line = line.strip().split('\t')
            unique_feature.add(strip_line[0])
    feature_list = list(unique_feature)

    for feature in feature_list:
        feature_review_dict[feature] = []

    with open(read_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            strip_line = line.strip().split('\t')

            for key in feature_review_dict:
                if key == strip_line[0]:
                    if strip_line[1] != 'empty':
                        if strip_line[2] == '相关':
                            feature_review_dict[key].append(strip_line[1])

    return feature_review_dict


def cul_contri(feature_review_dict):
    zero_zero = {}
    zero_one = {}
    one_zero = {}
    one_one = {}

    for feature in feature_review_dict:
        if len(feature_review_dict[feature]) == 0:
            zero_zero[feature] = []

    for feature in feature_review_dict:
        feature_date = feature[:10]
        flag_inf = 0
        flag_end = 0
        for review in feature_review_dict[feature]:
            review_date = review[:10]
            if review_date > feature_date:
                flag_end = 1
            if review_date <= feature_date:
                flag_inf = 1
        if flag_inf == 1 and flag_end == 1:
            one_one[feature] = feature_review_dict[feature]
        if flag_inf == 0 and flag_end == 1:
            zero_one[feature] = feature_review_dict[feature]
        if flag_inf == 1 and flag_end == 0:
            one_zero[feature] = feature_review_dict[feature]
    print('0-0:', len(zero_zero))
    print('0-1:', len(zero_one))
    print('1-0:', len(one_zero))
    print('1-1:', len(one_one))

    user = len(one_zero) + len(one_zero)
    total = len(zero_zero) + len(zero_one) + len(one_zero) + len(one_zero)
    user_contri = user / total
    print(user_contri)


if __name__ == '__main__':
    read_path = '../data/tencent_alPair.txt'

    # read_path = '../data/douyin_alPair.txt'

    # read_path = '../data/dingding_Pair1.txt' 
    # read_path = '../data/dingding_Pair2.txt'
    # read_path = '../data/dingding_Pair3.txt'
    # read_path = '../data/dingding_Pair4.txt'
    # read_path = '../data/dingding_Pair5.txt'
    # read_path = '../data/dingding_Pair6.txt'
    # read_path = '../data/dingding_Pair7.txt'
    # read_path = '../data/dingding_Pair8.txt'

    # read_path = '../data/keep_alPair.txt'

    # read_path = '../data/zoom_alPair.txt'

    feature_review_dict = change_pair_format(read_path)
    cul_contri(feature_review_dict)
