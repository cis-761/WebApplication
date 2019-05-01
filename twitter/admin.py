from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tweets
from .models import User
from .models import Flu
from .models import Symptoms

admin.site.register(Tweets)
admin.site.register(User)
admin.site.register(Flu)
admin.site.register(Symptoms)