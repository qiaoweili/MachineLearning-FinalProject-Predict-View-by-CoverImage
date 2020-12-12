# Forecast Views Through Video Cover Images
## —A Classification Problem Using VGG and ResNet from Machine Learning

The goal of this project is to have and video cover image as an input, and output the predicted range of number of views the video might have.

It helps the video producer to test whether his/her video cover is attractive enough and might help us study human visual aesthetic.

### All these data are collected from videos with a 'vlog' tag on www.bilibili.com using Beautifulsoup4.

The attributes we collected are the link of the cover images and the corresponding number of views of the videos.

-**data collecting/bililarge_download.py, bili_download.py**: python files for web scraping and downloading: 

-**data collecting/bililarge_vlog.html**: example html file for web scraping

-**data collecting/checkimg.py**: python file for checking if all images are downloaded properly and delete invalid ones

-**data collecting/numhit_distribution.csv**: first csv file to see the distribution of number of views and decide the range of each class

-**data collecting/bili_trainset.xlsx**: xlsx file of collected cover image link, number of views and corresponding downloaded name

-**split dataset into train validation test set.ipynb**:jupyter notebook for spliting data into train/validation/test sets

The collection of huge amount of html files are done by both Wenyu and Qiaowei; web scraping by Qiaowei; distribution Histogram by Wenyu

### The dataset we have can be found in Google Drive:  https://drive.google.com/drive/u/1/folders/1bLj34DvK0SZyDXt-dFfC40RLADSKE2Qo

**IMAGES_NEW**: first time collected imbalanced dataset

**coverimage**: balanced dataset after another round of webscraping and undersampling

**dataset_whole_split**: all data we have


### The machine learning model we use is Convolutional neural Network(CNN) and Transfer Learning.

We choose VGG16 and Resnet50 as two pretrained models to initialize our task and use logistic regression as the last layer to achieve our classification purpose.

**Transer Learning(VGG16)+logisticregression.ipynb**(pytorch): The transfer learning model using VGG16 as initial model. The dataset used in this uploaded file is the balanced dataset. Can change dataset by adjusting the dataset file name.

**TransferLearning(Resnet50).ipynb** (tensorflow): The transfer learning model based on Resnet50 as initial model. The dataet used in this uploaded file is the balanced dataset. Can change dataset by adjusting the dataset file name.

**resnet-balanced-prediction**: The model to predict the potential range of views of a cover image. Input into a random subfolder in folder test_img(whichever subfolder you like), and get the prediction. The model used here is based on Resnet using the balanced dataset(coverimage).

**dataset_summary.pdf**: summary of both the distribution information of each dataset, and the test accuracy we get by running the two transfer learning models on each dataset. 6 outcomes in total.

This part is done by both Wenyu and Qiaowei.

**Reference:**

https://www.youtube.com/watch?v=1Gbcp66yYX4&feature=youtu.be

http://enric.hosting.nyu.edu/notebooks/CNN-VGG-Transfer

