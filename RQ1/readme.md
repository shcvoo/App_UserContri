## Code

- *remove_symbol.py*

  ​	Remove special symbols from the original reviews.

- *review_train.py*

  ​	Create a dataset for fine-tuning review filtering.

### train

- *filter_review.py*

  ​	Fine-tuning review filtering tasks. (To run the model, create a *review* folder in the current directory and place the corresponding training set inside and modify the code from lines 183 to 217 to make it applicable to different datasets. Using command below). 

  ​	Download pre-trained BERT model [BERT-Base, Chinese](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip), [BERT-Base](https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-12_H-768_A-12.zip).
  
  ```
  for tencent, douyin, dingding, keep datasets
  python filter_review.py --task_name=rev --do_train=true --do_eval=true --do_predict=false --data_dir=review --vocab_file=./pretrained_model/chinese_L-12_H-768_A-12/vocab.txt --bert_config_file=./pretrained_model/chinese_L-12_H-768_A-12/bert_config.json --init_checkpoint=./pretrained_model/chinese_L-12_H-768_A-12/bert_model.ckpt --train_batch_size=32 --max_seq_length=128 --output_dir=result
  
  for zoom datasets
  python filter_review.py --task_name=rev --do_train=true --do_eval=true --do_predict=false --data_dir=review --vocab_file=./pretrained_model/uncased_L-12_H-768_A-12/vocab.txt --bert_config_file=./pretrained_model/uncased_L-12_H-768_A-12/bert_config.json --init_checkpoint=./pretrained_model/uncased_L-12_H-768_A-12/bert_model.ckpt --train_batch_size=32 --max_seq_length=128 --output_dir=result	
  ```

## Data

### manually annotated data

- *tencent_manu.xlsx*
- *douyin_manu.xlsx*
- *dingding_manu.xlsx* 
- *keep_manu.xlsx*
- *zooom_manu.xlsx*

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
pandas==1.1.5
emojiswitch==0.0.3
tensorflow-gpu==1.15.0
```

