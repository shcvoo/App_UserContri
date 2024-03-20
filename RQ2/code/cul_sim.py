import random
import jieba
from simtext import similarity
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string



def cul_sim(review_path, feature_path, write_path):
    df = pd.read_excel(review_path)
    review = [str(row['date'])[:10] + '-' + str(row['content']) for index, row in df.iterrows() if
              row['label'] == 1]
    print("get review done")

    with open(feature_path, 'r', encoding='utf-8') as f:
        feature_list = [line.strip() for line in f]
    feature = random.sample(feature_list, int(len(feature_list) * 0.3))
    print("get feature done")

    sim = similarity()
    pair = []
    print("start Calculate")
    stopwords_path = './hit_stopwords.txt'
    with open(stopwords_path, 'r', encoding='utf-8') as f:
        stopwords = [line.strip() for line in f.readlines()]

    for fea in feature:
        for rev in review:
            clean_review = ''.join([word for word in jieba.cut(rev[11:]) if word not in stopwords])
            clean_feature = ''.join([word for word in jieba.cut(fea[11:]) if word not in stopwords])

            result = sim.compute(clean_feature, clean_review)
            if result['Sim_Cosine'] >= 0.3:
                pair.append(fea + '\t' + rev + '\t' + '1')

    split_data = [item.split('\t') for item in pair]
    df = pd.DataFrame(split_data, columns=['feature', 'review', 'label'])
    df.to_excel(write_path, index=False)

    print('done')


def cul_sim_eng(review_path, feature_path, write_path):
    df = pd.read_excel(review_path)
    review = [str(row['date'])[:10] + '-' + str(row['content']) for index, row in df.iterrows() if
              row['label'] == 1]
    print("get review done")

    with open(feature_path, 'r', encoding='utf-8') as f:
        feature_list = [line.strip() for line in f]
    feature = random.sample(feature_list, int(len(feature_list) * 0.3))
    print("get feature done")

    pair = []
    print("start Calculate")

    for fea in feature:
        for rev in review:
            texts = [fea[11:], rev[11:]]

            translator = str.maketrans("", "", string.punctuation)
            texts = [text.translate(translator).lower() for text in texts]

            stop_words = set(stopwords.words('english'))
            texts = [' '.join([word for word in word_tokenize(text) if word not in stop_words]) for text in texts]

            tfidf_vectorizer = TfidfVectorizer()
            tfidf_matrix = tfidf_vectorizer.fit_transform(texts)

            cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

            if cosine_sim[0][0] >= 0.3:
                pair.append(fea + '\t' + rev + '\t' + '1')

    split_data = [item.split('\t') for item in pair]
    df = pd.DataFrame(split_data, columns=['feature', 'review', 'label'])
    df.to_excel(write_path, index=False)

    print('done')


if __name__ == '__main__':
    
    review_path = 'RQ1/tencent_manu.xlsx'
    feature_path = 'feature/tencent.txt'
    write_path = '../data/tencent_pair_manu.xlsx'
    
    # review_path = 'RQ1/douyin_manu.xlsx'
    # feature_path = 'feature/douyin.txt'
    # write_path = '../data/douyin_pair_manu.xlsx'
    
    # review_path = 'RQ1/dingding_manu.xlsx'
    # feature_path = 'feature/dingding.txt'
    # write_path = '../data/dingding_pair_manu.xlsx'
    
    # review_path = 'RQ1/keep_manu.xlsx'
    # feature_path = 'feature/keep.txt'
    # write_path = '../data/keep_pair_manu.xlsx'


    # review_path = 'RQ1/zoom_manu.xlsx'
    # feature_path = 'feature/zoom.txt'
    # write_path = '../data/zoom_pair_manu.xlsx'

    cul_sim(review_path, feature_path, write_path)
    # cul_sim_eng(review_path, feature_path, write_path)
