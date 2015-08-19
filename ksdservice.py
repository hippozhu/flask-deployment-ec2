# -*- coding: utf-8 -*-
import json
from keywordStuffingClassifier import *
from flask import Flask, request
import pickle

import time
print 'before nltk'
import nltk
print 'after nltk'
application = Flask('__name__')

#kw = topKeywords(10000)

print 'starting application'
print 'loading pickles'

classifier = pickle.load(open('model.pickle', 'rb'))
bigrams_FreqDist = pickle.load(open('/dict_bigram_FreqLog.pickle', 'rb'))
trigrams_FreqDist = pickle.load(open('/dict_trigram_FreqLog.pickle', 'rb'))
print 'pickles loaded'
print 'startup complete.'

@application.route('/', methods=['GET', 'POST'])
def detect_spam():
    if request.method == 'POST':
        title = request.form.get('title', '')
        desc = request.form.get('desc', '')
        reqs = request.form.get('reqs', '')
    else:
        title = request.args.get('title', '')
        desc = request.args.get('desc', '')
        reqs = request.args.get('reqs', '')

    print "title = " + title
    print "desc = " + desc
    print "reqs = " + reqs

    if title == '' and desc == '' and reqs == '':
        return "Error: at least one of (title, desc, reqs) must be provided."
    answer = classify(kw, trigrams_FreqDist, bigrams_FreqDist, classifier, title, desc, reqs)
    #answer = 'hello world!'
    output = '{"data":{"contains_spam":"' + str(answer) + '"}}'

    return output
