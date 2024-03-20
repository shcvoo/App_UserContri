def write_label(label_path, date_path):
    label = []
    with open(label_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            strip_line = line.strip().split('\t')
            label.append(strip_line[0])
    f.close()

    with open(date_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    f.close()

    for i in range(len(lines)):
        lines[i] = lines[i].strip().split('\t')[0] + '\t' + lines[i].strip().split('\t')[1] + '\t' + label[i] + '\n'

    with open(date_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    f.close()


if __name__ == '__main__':
    label_path = '../data/tencent_for_predict.txt'
    date_path = '../data/tencent_remain_date.txt'

    # label_path = '../data/douyin_for_predict1.txt'
    # date_path = '../data/douyin_remain_date1.txt'

    # label_path = '../data/douyin_for_predict2.txt'
    # date_path = '../data/douyin_remain_date2.txt'

    # label_path = '../data/douyin_for_predict3.txt'
    # date_path = '../data/douyin_remain_date3.txt'

    # label_path = '../data/douyin_for_predict4.txt'
    # date_path = '../data/douyin_remain_date4.txt'

    # label_path = '../data/douyin_for_predict5.txt'
    # date_path = '../data/douyin_remain_date5.txt'

    # label_path = '../data/dingding_for_predict1.txt'
    # date_path = '../data/dingding_remain_date1.txt'

    # label_path = '../data/dingding_for_predict2.txt'
    # date_path = '../data/dingding_remain_date2.txt'

    # label_path = '../data/dingding_for_predict3.txt'
    # date_path = '../data/dingding_remain_date3.txt'

    # label_path = '../data/dingding_for_predict4.txt'
    # date_path = '../data/dingding_remain_date4.txt'

    # label_path = '../data/dingding_for_predict5.txt'
    # date_path = '../data/dingding_remain_date5.txt'

    # label_path = '../data/dingding_for_predict6.txt'
    # date_path = '../data/dingding_remain_date6.txt'

    # label_path = '../data/dingding_for_predict7.txt'
    # date_path = '../data/dingding_remain_date7.txt'

    # label_path = '../data/dingding_for_predict8.txt'
    # date_path = '../data/dingding_remain_date8.txt'

    # label_path = '../data/zoom_for_predict.txt'
    # date_path = '../data/zoom_remain_date.txt'

    write_label(label_path, date_path)
