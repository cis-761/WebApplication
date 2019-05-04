from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tweets
from .models import User
from .models import Flu
from .models import Symptoms
from .models import Trends
from .models import fluSymptoms
from .models import tweetFlu
from .models import userTweets
from .models import tweetFlu
from .models import userTweets
from .models import tweetTrends

admin.site.register(Tweets)
admin.site.register(User)
admin.site.register(Flu)
admin.site.register(Symptoms)
admin.site.register(Trends)
admin.site.register(fluSymptoms)
admin.site.register(tweetFlu)
admin.site.register(userTweets)
admin.site.register(tweetFlu)
admin.site.register(userTweets)
admin.site.register(tweetTrends)
