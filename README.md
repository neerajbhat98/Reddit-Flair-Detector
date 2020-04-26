# Reddit-Flair-Detector
Build a web application which can be used to predict Flare of a r/india post. Application has an input field which expects a link to a reddit post from r/india. On submission predicts the flair of the post.

## Structure
* [Requirements ](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/requirements.txt) contains all the packages along with their versions needed to run this application.
* [Reddit Data Scrapper](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/Reddit%20Data%20Scrapper.ipynb) contains the code which was used to scrape data from Reddit using ['PushShift'](https://pushshift.io/api-parameters/) and saving into .json files. 
* [Redddit Flair Detector'](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/Reddit%20Flair%20Detector.ipynb) containe the code for data cleaning, model building and training. 
* [app.py](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/app.py) contains the routing information and template rendering for the app.
* [Link to App](http://midas-reddit-flair-detector.herokuapp.com/)

## App SnapShots
![alt text](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/home_page.png)
![alt ttext](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/result_page.png)


## Approach
* Around 10k reddit posts were scraped using Pushshift API from January 1,2019 to April 25,2020. However due to non-uniform distribution of posts for different flairs, some additional data was scraped from January 1, 2017 to January 1, 2019 for flairs like Food, Sports etc.
* All the preprocessing and cleaning was done by this Python [Package](https://pypi.org/project/clean-text/).
* A deep learning model(i.e. LSTM) was trained for 10 epochs on a train-test-split ratio of 90:10.
* Input features to the model was post.title+ " " + post.body.
* Pre-trained Glove Embeddings were used during training, but due to the absence of a large of tokens from reddit posts in the Glove Embeddings, the weights of the Embedding layers were set to trainable=True.
* A 100-D vector was used to represent tokens. Using 200-D and 300-D lead to overfitting.
* Trained Model can be dowloaded from [model](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/model.h5). In case, you're having problems with loading this model in Keras(very likely), I would recommmend to download [weights](https://www.kaggle.com/nbhativp/kernel19d73c0342/output?scriptVersionId=32660830) from my Kaggle repository where you'll also the find the model architecture and then you can easily load this model.
* [Word_Index](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/word_index.json) contains all the tokens from the scraped corpus and their respective indices used during training.

![alt text](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/architecture.png)
![alt ttext](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/Training.png)
![alt ttext](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/Accuracy.png)



