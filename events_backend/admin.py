# admin.py
# Arnav Ghosh, Jessica Zhao, Jill Wu, Adit Gupta
# 17th Sept. 2018

from django.contrib import admin
from events_backend.models import Attendance, Event, Location, Media, Tag, App_User, Org

admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Media)
admin.site.register(Tag)
admin.site.register(Attendance)
admin.site.register(App_User)
admin.site.register(Org)