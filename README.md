# Smart Grievances Redressal Dashboard

## Introduction
`Smart_Grievances_Redressal` is a dashboard made by `Team Scooptroop` for monitoring people complaints against posted in various social media handles, like twitter as well as the grievances portal. . 


## Built With
* [Dash](https://dash.plot.ly/) - Main server and interactive components 
* [Plotly Python](https://plot.ly/python/) - Used to create the interactive plots
* [Google Translate](https://translate.google.co.in/) - Translate marathi/hindi or code mixed language into english
* [Amazon transcribe](https://aws.amazon.com/transcribe/) - To convert speech to text, yet to be integrated with frontend
* We have also facilitated the use of amazon cloud 9 along with EC2 instance and lambda function generator to facilitate this feature as an independent API, which is able to handle large and live inputs and produce the output

## Unique Features 
* Classifies complaints without human intervention according to the department
* [Text classification](https://github.com/purplepotion/Smart_Grievances_Redressal/tree/master/multi-class-text-classification-cnn) using deep learning approaches such as [CNN and LSTM](https://www.researchgate.net/profile/Basit_Raza2/publication/333706654_A_Hybrid_CNN-LSTM_Model_for_Improving_Accuracy_of_Movie_Reviews_Sentiment_Analysis/links/5d00b1eb299bf13a384ea950/A-Hybrid-CNN-LSTM-Model-for-Improving-Accuracy-of-Movie-Reviews-Sentiment-Analysis.pdf)
* Modular use of [Twitter API](https://colab.research.google.com/drive/1J1Cb-61b6Vw22Moz0yQktA-RZvwe_9wy?usp=sharing) to get the most relevant data
* Code-mixed laguage could also be used - [Translator](https://github.com/purplepotion/Smart_Grievances_Redressal/blob/master/web_app/apps/helpers/language_translation.py)
* [Extensive database](https://github.com/purplepotion/Smart_Grievances_Redressal/blob/master/web_app/apps/helpers/complaint_data.db)
* [Word embeddings](https://github.com/purplepotion/Smart_Grievances_Redressal/blob/master/multi-class-text-classification-cnn/data_helper.py) to deal with extra noisy data
## Requirements
We suggest you to create a separate virtual environment running Python 3 for this app, and install all of the required dependencies there. Run in Terminal/Command Prompt:

```
git clone https://github.com/purplepotion/Smart_Grievances_Redressal
python3 -m virtualenv venv
To run only the model: 
* cd multi-class-text-classification-cnn/
* python data_helpers.py
* python text_CNN.py
* python train.py
* python predict.py

To run the dashboard: Python index.py
```
In UNIX system: 

```
source venv/bin/activate
```
In Windows: 

```
venv\Scripts\activate
```

To install all of the required packages to this environment, simply run:

```
pip install -r requirements.txt
```

and all of the required `pip` packages, will be installed, and the app will be able to run.


## How to use this app

Run this app locally by:
```
python index.py
```
Open http://0.0.0.0:8050/ in your browser, you will see a live-updating dashboard.


## What does this app shows
Key words are displayed according to the department and the frequency graph of the complaints are dispalyed in the analytics dashboard
## Resources and references
* [Smart complaints dispatching](https://arxiv.org/pdf/1912.10546v1.pdf)
