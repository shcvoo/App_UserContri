## Code

- *predict_pair.py*

  ​	Creating a dataset for predicting the matching between user reviews and update logs.

- *manu_pair.py*

  ​	Get user reviews and update logs annotated as matches in RQ2.
  
- *write_result.py*

  ​	Write the prediction results to a file with timestamps.
  
- *cul_contri.py*

  ​	Calculate the user contribution for each app.

### predict 

#### filter_review

- *filter_review.py:*

  ​	Predicting remaining reviews. (To run the model, create a *review* folder in the current directory and place the corresponding remaining set inside and modify the code from lines 198 to 221 and from  754 to 764 to make it applicable to different datasets. Using command below)

  ​	Download pre-trained BERT model [BERT-Base, Chinese](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip), [BERT-Base](https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-12_H-768_A-12.zip).
  
  ```
  for tencent, douyin, dingding, keep datasets
  python filter_review.py --task_name=rev --do_train=false --do_eval=false --do_predict=true --data_dir=review --vocab_file=./pretrained_model/chinese_L-12_H-768_A-12/vocab.txt --bert_config_file=./pretrained_model/chinese_L-12_H-768_A-12/bert_config.json --init_checkpoint=./pretrained_model/chinese_L-12_H-768_A-12/bert_model.ckpt --train_batch_size=32 --max_seq_length=128 --output_dir=result
  
  for zoom datasets
  python filter_review.py --task_name=rev --do_train=false --do_eval=false --do_predict=true --data_dir=review --vocab_file=./pretrained_model/uncased_L-12_H-768_A-12/vocab.txt --bert_config_file=./pretrained_model/uncased_L-12_H-768_A-12/bert_config.json --init_checkpoint=./pretrained_model/uncased_L-12_H-768_A-12/bert_model.ckpt --train_batch_size=32 --max_seq_length=128 --output_dir=result
  ```

#### log_review_match

- *log_review_match.py*

  Predicting remaining user reviews and update logs. (To run the model, create a *pair* folder in the current directory and place the corresponding remaining set inside and modify the code from lines 203 to 229 amd from 767 to 779 to make it applicable to different datasets. Using command below)

  ```
  for tencent, douyin, dingding, keep datasets
  python log_review_match.py --task_name=pair --do_train=false --do_eval=false --do_predict=true --data_dir=pair --vocab_file=./pretrained_model/chinese_L-12_H-768_A-12/vocab.txt --bert_config_file=./pretrained_model/chinese_L-12_H-768_A-12/bert_config.json --init_checkpoint=./pretrained_model/chinese_L-12_H-768_A-12/bert_model.ckpt --train_batch_size=32 --max_seq_length=128 --output_dir=result
  		
  for zoom datasets
  python log_review_match.py --task_name=pair --do_train=false --do_eval=false --do_predict=true --data_dir=pair --vocab_file=./pretrained_model/uncased_L-12_H-768_A-12/vocab.txt --bert_config_file=./pretrained_model/uncased_L-12_H-768_A-12/bert_config.json --init_checkpoint=./pretrained_model/uncased_L-12_H-768_A-12/bert_model.ckpt --train_batch_size=32 --max_seq_length=128 --output_dir=result
  ```

## Data

### else review

We are temporarily not releasing the original files of the remaining review data because we will conduct further research on this dataset.

### predicted_review_log

Because of file size issues, we manually merged all matching user reviews with the update logs except for the dataset of *DingTalk*, and the data stored [here](https://pan.baidu.com/s/1a43VX8eca2xbzvZYKLxskA?pwd=fbwr).

### questionnaire survey result

- questionnaire survey result.xlsx

## Requirements

```
python==3.6
pandas==1.1.5
ordered_set==4.0.2
tensorflow-gpu==1.15.0
```

