from django.contrib import admin
from .models import Note
from django.contrib.sessions.models import Session

admin.site.register(Note)

admin.site.register(Session)