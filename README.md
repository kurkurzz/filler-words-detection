# Fille Words Detection in Speech

Model to detect "um", "ah", "hm", "uh" etc in speech.

### **Dataset**: 
https://paperswithcode.com/dataset/sep-28k
https://www.kaggle.com/bschuss02/stuttering-events-in-podcasts-dataset-sep28k

Each audio clips are 3 seconds.

**Note**: After the first training, the result was very bad. Then I decided to take a look at the dataset and I found that the label is not so accurate. So I decided to manually labelled the FluencyBank dataset which consist of 4k rows.

### **Method**:

Extract 13 components of MFCC from the audios then applied to a CNN model. Run threshold tuning to get the best threshold value.

### ORIGINAL vs AUGMENTED

**Original dataset consist of:**

| um_label | n_rows |
|----------|--------|
| 0.0      | 3219   |
| 1.0      | 925    |

Imbalanced dataset since 1.0 is only 22.3% from the total rows.

Ran the data on the CNN model. The result was not very good. 
Best f1_Score on **validation set is only 66%. (Accuracy is 83%** but in imbalanced dataset, accuracy is not the best metric to use.)

**Augmented dataset consist of:**

| um_label | n_rows |
|----------|--------|
| 0.0      | 3219   |
| 1.0      | 3700   |

Data augmentation is only done on the 1.0 labelled rows to upsample. (Risky bcuz open to high possibility of bias)

Set aside 600 rows (300 of 0.0 and 300 of 1.0) to be used as testing set. These 600 rows is taken only from the original data to measure the real performance of the model.

Balanced the remaining dataset to be almot 50% each and then feed into the CNN model.

The result from the validation set is good. **89% accuracy and 88% f1 score**. But it is possibly because of the bias regarding the augmentation

Test on the testing set that I set aside earlier. The result is quiet good, a lot of improvement from non augmented data. **~~82% accuracy and 81% f1_score~~**. 

I realised there is some kind of data leakage when I use the augmented audios from the audio files that used for testing set. So I filter out the specific augmented audio files and retrain the model. The result is **76% accuracy and 72% f1 score** which is acceptable and still better than no augmentation at all.

### Next Step

1. Label more data. Since the augmentation could improve the model performance, I expect more labelled data could too.


### Potential Bias

1. Data augmentation only be done on the  audio containing filler words which can trick the model into predicting augmented audio instead of audio containing filler words.
2. The dataset is taken from people that have very bad problems with stutter. Stuttering will cause repetition in the audio waveform. The model might have less accuracy in predicting non-stutter people.
3. The dataset is taken from non-malaysian people. It may or may not have drops of accuracy on malaysian speech. Potential reason it might not is because the filler words accent is not so different actually. But maybe the overall accent can affect the performance.


### **Lessons learned**:

1. Unlike Neural Network (NN) where the weights are independent, CNN’s weights are attached to the neighboring pixels to extract features in every part of the image.
2. Threshold value does not necessary be 0.5. In some cases especially in an inbalanced dataset, the threshold value need to be adjust.
3. If you augment the minority class of the data, make sure to run test on the original and unseen data to measure its true performance.
4. Need to alert on data leakage and bias.