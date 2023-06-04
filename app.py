import pickle
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import nltk
from flask import Flask, request, render_template

nltk.download('stopwords')
nltk.download('wordnet')

# cleaning the text i.e removing all unncessary characters


def text_cleaning(text):
  text = re.sub("'\''", "", text)  # Remove backslashes followed by single quotes
  text = re.sub("[^a-zA-Z]", " ", text)  # Replace non-alphabetic characters with spaces
  text = ' '.join(text.split())  # Remove extra whitespace
  text = text.lower()  # Convert text to lowercase

  return text



# removing the stopwords
stop_words = set(stopwords.words('english'))
# defining the stopwords removal function
def remove_stopwords(text):
  removed_words = [word for word in text.split() if word not in stop_words]
  return ' '.join(removed_words)


# lemmatizing the text
def lemmatizing(sentence):
  word_lemma = WordNetLemmatizer()
  stemSentence = ""
  for word in sentence.split():
    stemmed = word_lemma.lemmatize(word)
    stemSentence += stemmed
    stemSentence += " "
  stemSentence = stemSentence.strip()
  return stemSentence

# stemming the text,i.e reducing the word size

def stemming(text):

    stemmer = PorterStemmer()
    stemmed_sentence = ""
    for word in text.split():
        stem = stemmer.stem(word)
        stemmed_sentence += stem
        stemmed_sentence += " "

    stemmed_sentence = stemmed_sentence.strip()
    return stemmed_sentence



def test(text, model, tfid_vector):
  text = text_cleaning(text)
  text = remove_stopwords(text)
  text = lemmatizing(text)
  text = stemming(text)

  vectorized_text = tfid_vector.transform([text])
  predicted = model.predict(vectorized_text)

  newmapper = {0: 'Fantasy', 1: 'Science Fiction', 2: 'Crime Fiction',
                 3: 'Historical novel', 4: 'Horror', 5: 'Thriller'}
  
  return newmapper[predicted[0]]


# loading the model
amz_mb_file = open('amz_classification_model.pkl', 'rb')
model = pickle.load(amz_mb_file)
amz_mb_file.close()

amz_tfid_file = open('amz_tfid_model.pkl', 'rb')
tfidf_vectorizer = pickle.load(amz_tfid_file)
amz_tfid_file.close()


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':

        mydict = request.form
        text = mydict["summary"]
        prediction = test(text, model, tfidf_vectorizer)

        return render_template('index.html', genre=prediction, text=str(text)[:100], showresult=True)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
