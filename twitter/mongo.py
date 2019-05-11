from pymongo import MongoClient
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from django.conf import settings as djangoSettings
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import time

def aggregation():
    s = time.time()
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client['Twitter-Text-Mining']
    collection = db.data
    # lets first get the data that we are going to graph
    count_flu = 0
    count_flushot = 0
    count_sick = 0
    count_ill = 0
    count_cold = 0
    count_influenza = 0
    count_flu = collection.count_documents({ 'text': { '$regex':'/.*flu*/'  } })
    count_flushot = collection.count_documents({ 'text': { '$regex':'/.*flushot*/'  } })
    count_sick = collection.count_documents({ 'text': { '$regex':'/.*sick*/'  } })
    count_ill = collection.count_documents({ 'text': { '$regex':'/.*ill*/'  } })
    count_cold = collection.count_documents({ 'text': { '$regex':'/.*cold*/'  } })
    count_influenza = collection.count_documents({ 'text': { '$regex':'/.*influenza*/'  } })
    print("Total count of occurences of keyword flu: " + str(count_flu))
    print("Total count of occurences of keyword flushot: " + str(count_flushot))
    print("Total count of occurences of keyword sick: " + str(count_sick))
    print("Total count of occurences of keyword ill: " + str(count_ill))
    print("Total count of occurences of keyword cold: " + str(count_cold))
    print("Total count of occurences of keyword influenza: " + str(count_influenza))
    master_list = [count_flu, count_flushot, count_sick, count_ill, count_cold, count_influenza]
    fig=Figure()
    ax=fig.add_subplot(111)
    x = ['flu', 'flushot', 'sick', 'ill', 'cold', 'influenza']
    y = master_list
    ax.bar(x,y)
    ax.set_title("Count of Tweets per Keyword")
    ax.set_xlabel("Keywords")
    ax.set_ylabel("Number of tweets")
    canvas=FigureCanvas(fig)    
    fig.savefig('./mongo_graph.png')
    e = time.time()
    print(e-s)

aggregation()

