from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect 
from django.conf import settings as djangoSettings
import pandas as pd
from .models import Tweets
from .models import User
from .models import Flu
from .models import Symptoms
from .models import Trends
from .models import fluSymptoms
from .models import tweetFlu
from .models import userTweets
from .models import tweetTrends
import re
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .filters import UserFilter
from .filters import TweetFilter
import time
from .mongo import aggregation


# Create your views here.

def tweets_list(request):
    if request.method == 'POST':
        s = time.time()
        all_entries = Tweets.objects.all()
        flu_related = []
        flushot_related = []
        sick_related = []
        ill_related = []
        cold_related = []
        infleunza_related = []
        for i in all_entries:
            if word_in_text('flu', i.text):
                flu_related.append(i)
            if word_in_text('flushot', i.text):
                flushot_related.append(i)
            if word_in_text('sick', i.text):
                sick_related.append(i)
            if word_in_text('ill', i.text):
                ill_related.append(i)
            if word_in_text('cold', i.text):
                cold_related.append(i)
            if word_in_text('influenza', i.text):
                infleunza_related.append(i)
        count_flu = len(flu_related)
        count_flushot = len(flushot_related)
        count_sick = len(sick_related)
        count_ill = len(ill_related)
        count_cold = len(cold_related)
        count_influenza = len(infleunza_related)
        print("Total count of occurences of keyword flu: " + str(count_flu))
        print("Total count of occurences of keyword flushot: " + str(count_flushot))
        print("Total count of occurences of keyword sick: " + str(count_sick))
        print("Total count of occurences of keyword ill: " + str(count_ill))
        print("Total count of occurences of keyword cold: " + str(count_cold))
        print("Total count of occurences of keyword influenza: " + str(count_influenza))
        master_list = [count_flu, count_flushot, count_sick, count_ill, count_cold, count_influenza]
        fig=Figure()
        ax=fig.add_subplot(111)
        x= ['flu', 'flushot', 'sick', 'ill', 'cold', 'influenza']
        y = master_list
        ax.bar(x,y)
        ax.set_title("Count of Tweets per Keyword")
        ax.set_xlabel("Keywords")
        ax.set_ylabel("Number of tweets")
        canvas=FigureCanvas(fig)    
        path = djangoSettings.STATIC_ROOT 
        fig.savefig(path + '/admin/img/graph.png')
        e = time.time()
        print(e-s)
        return redirect('results')
    else:
        return render(request, 'twitter/index.html', {})

def simple_upload(request):
    if request.method == 'POST':
        new_types = request.FILES['myfile']
        csv = pd.read_csv(request.FILES['myfile'])
        col_names = list(csv.columns.values)
        pokemon_model_att = ''
        model_att = ''
        check_names_list = [] # empty list to begin 
        col_dataframes = []
        for i in range(len(col_names)):
            check_names_list.append(col_names[i])
        check_names = tuple(check_names_list)
        print(check_names)
        if check_names == ('text', 'favorite', 'date', 'rt', 'location'): # we have tweets.csv
             for value in range(csv.shape[0]):
                 col1_val = str(csv.at[value, col_names[0]])
                 col2_val = str(csv.at[value, col_names[1]])
                 col3_val = str(csv.at[value, col_names[2]])
                 col4_val = str(csv.at[value, col_names[3]])
                 col5_val = str(csv.at[value, col_names[4]])
                 Tweets.objects.create(text=col1_val, favorite=col2_val, date=col3_val, rt=col4_val, location=col5_val)
                 print('tweet added ' + str(col1_val) + ' ' + str(col2_val)) 
        elif check_names == ('name', 'screen_name', 'geo_enabled', 'verified'): # we have user.csv
            for value in range(csv.shape[0]):
                col1_val = str(csv.at[value, col_names[0]])
                col2_val = str(csv.at[value, col_names[1]])
                col3_val = str(csv.at[value, col_names[2]])
                col4_val = str(csv.at[value, col_names[3]])
                User.objects.create(name=col1_val, screen_name=col2_val, geo_enabled=col3_val, verified=col4_val)
                print('user added ' + str(col1_val) + ' ' + str(col2_val))
        elif check_names == ('name', 'description'): # we have symptoms.csv 
            for value in range(csv.shape[0]):
                col1_val = str(csv.at[value, col_names[0]])
                col2_val = str(csv.at[value, col_names[1]])
                Symptoms.objects.create(name= col1_val, description=col2_val)
                print('symptom added ' + str(col1_val))
        elif check_names == ('Unnamed: 0','user_id', 'tweet_id'): #we have userTweets.csv
            for value in range(1,csv.shape[0]+1):
                col1_val = User.objects.get(id=value)
                col2_val = Tweets.objects.get(id=value)
                userTweets.objects.create(user_id= col1_val, tweet_id=col2_val)
                print('userTweets added ' + str(col1_val))
        else: # we have flu.csv
            for value in range(csv.shape[0]):
                col1_val = str(csv.at[value, col_names[0]])
                Flu.objects.create(flu_type= col1_val)
                print('flu type added ' + str(col1_val))
            
            
    return render(request, 'twitter/simple_upload.html', {})

def results(request):
    return render(request, 'twitter/results.html', {})

# checks if word is in text
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def login(request):
    if request.POST:
        if 'login' in request.POST:
            return HttpResponseRedirect('/youloggedin/')
        else:
            return HttpResponseRedirect('/youregistered')
    else:
        return render(request, '/twitter/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, '/twitter/register.html', {'form': form})

def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'twitter/user_list.html', {'filter': user_filter})

def tweet_search(request):
    tweet_list = Tweets.objects.all()
    tweet_filter = TweetFilter(request.GET, queryset=tweet_list)
    return render(request, 'twitter/tweet_list.html', {'filter': tweet_filter})

def mongo(request):
    if request.method == 'POST':
        aggregation()
        return redirect('mongo_results')
    else:
        return render(request, 'twitter/mongo.html')

def mongo_results(request):
    return render(request, 'twitter/mongo_results.html', {})

def t_cluster(request):
    return render(request, 'twitter/t-sne-cluster.html' )

def idm(request):
    return render(request, 'twitter/intertopic-distance-map.html')

def graphs(request):
    return render(request, 'twitter/graphs.html')

def postgresql(request):
    if request.method == 'POST':
        s = time.time()
        all_entries = Tweets.objects.all()
        flu_related = []
        flushot_related = []
        sick_related = []
        ill_related = []
        cold_related = []
        infleunza_related = []
        for i in all_entries:
            if word_in_text('flu', i.text):
                flu_related.append(i)
            if word_in_text('flushot', i.text):
                flushot_related.append(i)
            if word_in_text('sick', i.text):
                sick_related.append(i)
            if word_in_text('ill', i.text):
                ill_related.append(i)
            if word_in_text('cold', i.text):
                cold_related.append(i)
            if word_in_text('influenza', i.text):
                infleunza_related.append(i)
        count_flu = len(flu_related)
        count_flushot = len(flushot_related)
        count_sick = len(sick_related)
        count_ill = len(ill_related)
        count_cold = len(cold_related)
        count_influenza = len(infleunza_related)
        print("Total count of occurences of keyword flu: " + str(count_flu))
        print("Total count of occurences of keyword flushot: " + str(count_flushot))
        print("Total count of occurences of keyword sick: " + str(count_sick))
        print("Total count of occurences of keyword ill: " + str(count_ill))
        print("Total count of occurences of keyword cold: " + str(count_cold))
        print("Total count of occurences of keyword influenza: " + str(count_influenza))
        master_list = [count_flu, count_flushot, count_sick, count_ill, count_cold, count_influenza]
        fig=Figure()
        ax=fig.add_subplot(111)
        x= ['flu', 'flushot', 'sick', 'ill', 'cold', 'influenza']
        y = master_list
        ax.bar(x,y)
        ax.set_title("Count of Tweets per Keyword")
        ax.set_xlabel("Keywords")
        ax.set_ylabel("Number of tweets")
        canvas=FigureCanvas(fig)    
        path = djangoSettings.STATIC_ROOT 
        fig.savefig(path + '/admin/img/graph.png')
        e = time.time()
        print(e-s)
        return redirect('results')
    else:
        return render(request, 'twitter/postgresql.html', {})