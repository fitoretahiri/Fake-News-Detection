import string
import os
import pickle
from nltk.corpus import stopwords
from dotenv import load_dotenv

def punctuation_removal(text):
    all_list = [char for char in text if char not in string.punctuation]
    clean_str = ''.join(all_list)
    return clean_str

def remove_stopwords(text):
    stop = stopwords.words('english')
    return ' '.join([word for word in text.split() if word not in stop])


def load_model():
    load_dotenv()
    path = os.path.abspath(os.getenv('PATH_TO_MODEL'))
    return pickle.load(open(path, 'rb'))

def load_vector():
    load_dotenv()
    path = os.path.abspath(os.getenv('PATH_TO_VECTOR'))
    return pickle.load(open(path, 'rb'))

def make_prediction(model, vector, input_data):
    input_data = punctuation_removal(input_data)
    input_data = input_data.lower()
    input_data = remove_stopwords(input_data)
    test = vector.transform([input_data])
    prediction = model.predict(test)
    return prediction