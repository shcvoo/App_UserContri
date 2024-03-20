## Code

- *cul_sim.py*

  ​	Calculate word similarity between user reviews and update logs for manual annotation.

- *pair_train.py*

  ​	Create a dataset for fine-tuning matching.

### train

- *log_review_match.py*

  ​	Fine-tuning matching tasks. (To run the model, create a *pair* folder in the current directory and place the corresponding training set inside and modify the code from lines 187 to 223 to make it applicable to different datasets. Using command below)

  ​	Download pre-trained BERT model [BERT-Base, Chinese](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip), [BERT-Base](https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-12_H-768_A-12.zip).
  
  ```
  for tencent, douyin, dingding, keep datasets
  python log_review_match.py: --task_name=pair --do_train=true --do_eval=true --do_predict=false --data_dir=pair --vocab_file=./pretrained_model/chinese_L-12_H-768_A-12/vocab.txt --bert_config_file=./pretrained_model/chinese_L-12_H-768_A-12/bert_config.json --init_checkpoint=./pretrained_model/chinese_L-12_H-768_A-12/bert_model.ckpt --train_batch_size=32 --max_seq_length=128 --output_dir=result
  
  for zoom datasets
  python log_review_match.py: --task_name=pair --do_train=true --do_eval=true --do_predict=false --data_dir=pair --vocab_file=./pretrained_model/uncased_L-12_H-768_A-12/vocab.txt --bert_config_file=./pretrained_model/uncased_L-12_H-768_A-12/bert_config.json --init_checkpoint=./pretrained_model/uncased_L-12_H-768_A-12/bert_model.ckpt --train_batch_size=32 --max_seq_length=128 --output_dir=result
  ```

## Data

We are temporarily not releasing the original files of the update log data because we will conduct further research on this dataset.

### manually annotated data

- *tencent_pair_manu.xlsx*
- *douyin_pair_manu.xlsx*
- *dingding_pair_manu.xlsx* 
- *keep_pair_manu.xlsx*
- *zooom_pair_manu.xlsx*

### training data

- *tencent_train.txt*
- *tencent_val.txt*
- *douyin_train.txt*
- *douyin_val.txt*
- *dingding_train.txt*
- *dingding_val.txt* 
- *keep_train.txt*
- *keep_val.txt*
- *zoom_train.txt*
- *zoom_val.txt*

## Requirements

```
python==3.6
jieba==0.42.1
simtext==1.1
pandas==1.1.5
scikit-learn==0.22
nltk==3.6.7
tensorflow-gpu==1.15.0
```

