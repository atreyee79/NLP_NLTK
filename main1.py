from flask import Flask,render_template,request
import nltk
nltk.download('punkt')
import string
punct=string.punctuation
# data='The United Kingdom of Great Britain and Northern Ireland, commonly known as the United Kingdom (UK) or Britain,is a sovereign country in north-western Europe, off the north-western coast of the European mainland.[20] The United Kingdom includes the island of Great Britain, the north-eastern part of the island of Ireland, and many smaller islands within the British Isles.Northern Ireland shares a land border with the Republic of Ireland. Otherwise, the United Kingdom is surrounded by the Atlantic Ocean, with the North Sea to the east, the English Channel to the south and the Celtic Sea to the south-west, giving it the 12th-longest coastline in the world. The Irish Sea separates Great Britain and Ireland. The total area of the United Kingdom is 93,628 square miles (242,500 km2).'
from nltk import FreqDist


app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/predict', methods = ['get'])
def predict():
    sent_name=request.form.get('Enter a sentence')
    
    data=input('enter a sentence:')
    len_sent=len(nltk.sent_tokenize(data))
    len_word=len(nltk.word_tokenize(data))
    
    freq=FreqDist(nltk.word_tokenize(data))
    clean_data=[]
    
    for word in nltk.word_tokenize(data):
        if word not in punct:
            
            clean_data.append(word)
            
    return render_template ('home.html',predict={ 'len_sent':len_sent,'len_word':len_word,'freq':freq})     
            
    
    information=getsentence()
    print(information)


if __name__=='__main__':
    app.run(debug=True)     
