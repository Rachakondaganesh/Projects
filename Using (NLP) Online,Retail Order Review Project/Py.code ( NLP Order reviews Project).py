# ONLINE / RETAIL ORDER REVIEWS PROJECT
# TO MAKE THIS PROJECT TRICKY WE USE "portuguese" REVIEWS
# Our objective is to calculate unigram, bigram, trigram
# IT IS HUGE DATA UPTO 1 LAKH ROWS

link="C:/Users/user/Downloads/order_reviews.csv"

import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer,WordNetLemmatizer

# NOW WE READ THE FILE
data=pd.read_csv(link)
print(data) # the data is upto 1lakh rows
print(list(data.columns))
# let's convert review_creation_date as date. else pandas read as text only
data["review_creation_date"]=pd.to_datetime(data["review_creation_date"])
data["review_creation_date"]=pd.to_datetime(data["review_creation_date"])

# Plotting bar graph to demo multiple score values
# lets create the colors using color code from colors in chrome
color_1 = "#fa2a05"
color_2 = "#f6fa05"
color_3 = "#051cfa"
color_4 = "#05f6fa"
color_5 = "#09fa05"
review_palette=sns.color_palette((color_1,color_2,color_3,color_4,color_5))

#pie-chart to see the % of each reviews
rev1=len(data[data["review_score"]==1])/ len(data)*100
rev2=len(data[data["review_score"]==2])/len(data)*100
rev3=len(data[data["review_score"]==3])/len(data)*100
rev4=len(data[data["review_score"]==4])/len(data)*100
rev5=len(data[data["review_score"]==5])/len(data)*100
data1=(rev1,rev2,rev3,rev4,rev5)
title=["review 1","review2","review3","review4","review5"]
plt.pie(data1,labels=title,colors=review_palette)
#plt.show()

# NOW LETS PLOT THE BAR GRAPH ON GREY BACKGROUND
# LETS PICK THE COLOR CODE FROM HTML COLOR PALETTE

sns.set_style("darkgrid",{"axes.facecolor": "#F0D8D3"}) # this code is our color

# FIGURE SIZE

resize_plot=lambda : plt.gcf().set_size_inches(12,5)

sns.catplot(x="review_score",kind="count",data=data,palette=review_palette).set(xlabel="review score",
                                                                                 ylabel="number of reviews")
plt.title("review_score distrubution")
plt.show()

# AS WE KNOW THIS IS PORTUGUESE DATA LETS PERFORM ON THE TEXT DATA
# FUNCTION TO REMOVE ACCENT

import unicodedata
def remove_accent(text):
    return unicodedata.normalize("NFKD",text).encode("ascii",errors="ignore").decode("utf-8")

#NFKD = Normalization Form Compatibility Decomposition
#ascii=American Standard Code for Information Interchange


  # now we perform basic NLP operations

def nlp_analysis(text):
    # making all lower
    text = text.lower()
    # tokenization
    text = word_tokenize(text)
    # performing stop words
    nltk_stop_words = set(stopwords.words("portuguese"))
    nltk_stop_words.update({"nao"})
    for i in text:
        if i in nltk_stop_words:
            count_i = text.count(i)
            for j in range(count_i):
                text.remove(i)

    # joining the text so that we are removing the brackets for all sentences

    text1 = " ".join(text)
  # this should return the value
    text=remove_accent(text1)
    return text1


commented_reviews=data[data["review_comment_message"].notnull()].copy()
commented_reviews["review_words"]=commented_reviews["review_comment_message"].apply(nlp_analysis)

review5s=commented_reviews[commented_reviews["review_score"]==5]
review1s=commented_reviews[commented_reviews["review_score"]==1]

# write a function to create UNIGRAM, BIGRAM and TRIGRAM
'''
i like product very much
unigram= [i,like,product, very, much]
bigram=[i like, like product, product very, very much]
trigram= [i like product, like product very, product very much]
'''
def word_to_ngrams(text):
    uni,bi,tri=[],[],[]
    words=text.split()
    for w in words:
        uni.extend(w)
        bi.extend(" ".join(b) for b in nltk.bigrams(w))
        tri.extend(" ".join(t) for t in nltk.trigrams(w))
    return uni,bi,tri

from nltk.util import ngrams
uni_5=ngrams(review5s["review_words"],1)
bi_5=ngrams(review5s["review_words"],2)
tri_5=ngrams(review5s["review_words"],3)
uni_1=ngrams(review1s["review_words"],1)
bi_1=ngrams(review1s["review_words"],2)
tri_1=ngrams(review1s["review_words"],3)

# function to plot the distribution graph
def freq_dist(tokens,color):
    resize_plot()
    # plotting FreqDist for top 25 ngrams
    nltk.FreqDist(tokens).plot(25,cumulative=False,color=color)
    plt.show()
# plot the ngrams for reviews with 5 score
freq_dist(uni_5, color_5)
freq_dist(bi_5, color_5)
freq_dist(tri_5, color_5)


# plot the ngrams for reviews with 1 score
freq_dist(uni_1, color_1)
freq_dist(bi_1, color_1)
freq_dist(tri_1, color_1)

#### OUR NLP ORDER REVIEWS PROJECT IS DONE ✅###







