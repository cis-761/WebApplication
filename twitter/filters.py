
import django_filters
from .models import User
from .models import Tweets

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['name', 'screen_name', 'geo_enabled', 'verified', ]

class TweetFilter(django_filters.FilterSet):
    class Meta:
        model = Tweets
        fields = ['text', 'location', 'favorite', 'date', 'rt', ]

        