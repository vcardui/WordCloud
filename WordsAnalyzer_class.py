# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2025, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: November 4th, 2025
# | Last update..: November 5th, 2025
# | WhatIs.......: Words Analyzer - Class
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# [1] Resource punkt_tab not found — for NLTK (NLP)
# https://gudguy1a.medium.com/resource-punkt-tab-not-found-for-nltk-nlp-d9e313aff438

# [2] Automatically detecting character encodings
# https://www.kaggle.com/code/rtatman/automatically-detecting-character-encodings

# ------------------------- Libraries -------------------------
import os  # os.path.exists(path)
import chardet # chardet.detect(rawdata.read())

import ssl # ssl._create_default_https_context

import matplotlib.pyplot as plt

import nltk
from nltk import word_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from wordcloud import WordCloud

# ------------------------- Class -------------------------
class WordsAnalyzer:
    def __init__(self):
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        nltk.download('punkt_tab') # [1]
        nltk.download('stopwords')

    def makeCloud(self, fileroute):
        if os.path.exists(fileroute):
            with open(fileroute, 'rb') as rawdata:
                result = chardet.detect(rawdata.read()) # [2]
                print(fileroute, result['encoding'])

            with open(fileroute, 'r', encoding=result['encoding']) as file:
                text = file.read()
                tokens = word_tokenize(text, language='spanish')
                # print("Tokens: ", tokens)

                stop_words = set(stopwords.words('spanish'))
                tokens_filtrados = [palabra for palabra in tokens if palabra.lower() not in stop_words]
                print("Tokens sin stopwords:", tokens_filtrados)
                texto_tokens_filtrados = ' '.join(tokens_filtrados)

                wordcloud = WordCloud(background_color="white").generate(texto_tokens_filtrados)
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis("off")
                plt.show()
        else:
            print(f"File not found on route: {fileroute}")