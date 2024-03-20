import pandas as pd
import re
import emojiswitch


def pre_review(read_path, write_path):
    
    print('get review')

    df = pd.DataFrame(pd.read_excel(read_path))

    
    df = df.applymap(lambda x: x.replace('（该条评论已经被删除）', '') if type(x) is str else x)
    df = df.applymap(lambda x: x.replace('\n', '') if type(x) is str else x)
    df = df.applymap(lambda x: x.replace((re.findall('(?<=---).*$', x))[0], '') if type(
        x) is str and '---' in x else x)
    df = df.applymap(lambda x: x.replace('---', '') if type(x) is str else x)

    df = df.applymap(lambda x: x.replace('*', '') if type(x) is str else x)
    df = df.applymap(lambda x: x.replace('~', '') if type(x) is str else x)
    df = df.applymap(lambda x: x.replace('$', '') if type(x) is str else x)
    df = df.applymap(lambda x: x.replace('#', '') if type(x) is str else x)
    df = df.applymap(lambda x: x.replace('^', '') if type(x) is str else x)
    df = df.applymap(lambda x: x.replace('_', '') if type(x) is str else x)

    # zh
    df = df.applymap(lambda x: emojiswitch.demojize(x, delimiters=("'", "'"), lang='zh') if type(x) is str else x)
    # en
    # df = df.applymap(lambda x: emojiswitch.demojize(x, delimiters=("'", "'"), lang='en') if type(x) is str else x)
   
    df_filtered = df[df['content'].notna()]
 
    df_filtered.to_excel(write_path)

    print("done")

if __name__ == '__main__':

    read_path = "../data/tencent.xlsx"
    write_path = "../data/tencent_manu.xlsx"
    
    # read_path = "../data/douyin.xlsx"
    # write_path = "../data/douyin_manu.xlsx"
    
    # read_path = "../data/dingding.xlsx"
    # write_path = "../data/dingding_manu.xlsx"
    
    # read_path = "../data/keep.xlsx"
    # write_path = "../data/keep_manu.xlsx"
    
    # read_path = "../data/zoom.xlsx"
    # write_path = "../data/zoom_manu.xlsx"
    
    pre_review(read_path, write_path)
