# Reddit-Flair-Detector
Build a web application which can be used to predict Flare of a r/india post. Application has an input field which expects a link to a reddit post from r/india. On submission predicts the flair of the post.

## Structure
* [Requirements ](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/requirements.txt) contains all the packages along ith their versions needed to run this application.
* [Reddit Data Scrapper](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/Reddit%20Data%20Scrapper.ipynb) contains the code which was used to scrape data from Reddit using ['PushShift'](https://pushshift.io/api-parameters/) and saving into .json files. The data was collected from January 1,2019 to April 25,2020. Due to non-uniform distribution of number of posts for different flairs, some additional data was scraped from January 1, 2017 to January 1, 2019 for some flairs like Food, Sport etc. 
* [Redddit Flair Detector'](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/Reddit%20Flair%20Detector.ipynb) containe the code for data cleaning, model building and training. 
* [app.py](https://github.com/neerajbhat98/Reddit-Flair-Detector/blob/master/app.py) contains the routing information and template rendering for the app.
* [Link to App](http://midas-reddit-flair-detector.herokuapp.com/)
