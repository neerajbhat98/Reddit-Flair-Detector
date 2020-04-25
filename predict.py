import json
import keras
import numpy as np
import os
import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Flatten, LSTM, Conv1D, MaxPooling1D, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.utils import to_categorical
from keras.layers import Dense, Input, GlobalMaxPooling1D
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model
from keras.initializers import Constant
import tensorflow as tf
from cleantext import clean
from sklearn.model_selection import train_test_split
from keras.models import Sequential, load_model

def mapping(index):
    labels_to_index = {0:'AskIndia', 1:'Non-Political', 2:'Science/Technology',3:'Coronavirus', 4:'Politics', 5:'Business/Finance/Policy/Economy', 6:'Sports', 7:'Food'}
    return labels_to_index[index]

def preprocess_text(text):
        text = clean(text,fix_unicode=True,               # fix various unicode errors
            to_ascii=True,                  # transliterate to closest ASCII representation
            lower=True,                     # lowercase text
            no_line_breaks=False,           # fully strip line breaks as opposed to only normalizing them
            no_urls=True,                  # replace all URLs with a special token
            no_emails=True,                # replace all email addresses with a special token
            no_phone_numbers=True,         # replace all phone numbers with a special token
            no_numbers=True,               # replace all numbers with a special token
            no_digits=True,                # replace all digits with a special token
            no_currency_symbols=True,      # replace all currency symbols with a special token
            no_punct=True,                 # fully remove punctuation
            replace_with_url="",
            replace_with_email="",
            replace_with_phone_number="",
            replace_with_number="",
            replace_with_digit="",
            replace_with_currency_symbol="",
            lang="en"                       # set to 'de' for German special handling
        )
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        text = ''.join(filter(whitelist.__contains__, text))    
        
        return text


def predict_flair(post):
    MAX_NUM_WORDS= 100000
    EMBEDDING_DIM = 100
    MAX_SEQUENCE_LENGTH = 2000
    file = open('word_index.json',) 
    word_index = json.load(file)  
    num_words = min(MAX_NUM_WORDS, len(word_index) + 1)
    model = load_model('model.h5')
    text = post['title'] + post['content']
                    
    flair_wise_dict = {"AskIndia":[], "Non-Political":[], "Science/Technology":[], "Coronavirus":[],"Politics":[],"Business/Finance":[], "Policy/Economy":[],"Sports":[], "Food":[]}
    text = preprocess_text(text)
    test = []
    tokenised_text = []
    for tokens in text.split():
        if tokens in word_index.keys():
            tokenised_text.append(word_index[tokens])
    test.append(tokenised_text)
    test = pad_sequences(test, maxlen=MAX_SEQUENCE_LENGTH)
    flair =  mapping(np.argmax(model.predict(test)))
    keras.backend.clear_session()
    
    if post['flair'] not in flair_wise_dict.keys():
        return post['flair']
    elif post['flair'] != flair:
        return post['flair']    
    return flair

def predict_flair_post_request(post):
    MAX_NUM_WORDS= 100000
    EMBEDDING_DIM = 100
    MAX_SEQUENCE_LENGTH = 2000
    file = open('word_index.json',) 
    word_index = json.load(file)  
    num_words = min(MAX_NUM_WORDS, len(word_index) + 1)
    model = load_model('model.h5')
    text = post['title'] + post['content']
                    
    flair_wise_dict = {"AskIndia":[], "Non-Political":[], "Science/Technology":[], "Coronavirus":[],"Politics":[],"Business/Finance":[], "Policy/Economy":[],"Sports":[], "Food":[]}
    text = preprocess_text(text)
    test = []
    tokenised_text = []
    for tokens in text.split():
        if tokens in word_index.keys():
            tokenised_text.append(word_index[tokens])
    test.append(tokenised_text)
    test = pad_sequences(test, maxlen=MAX_SEQUENCE_LENGTH)
    flair =  mapping(np.argmax(model.predict(test)))
    keras.backend.clear_session()
    
    if post['flair'] not in flair_wise_dict.keys():
        return "Photography"
    elif post['flair'] != flair:
        return post['flair']    
    return flair

