from django.contrib import admin
from django.urls import path
from .views import leaderboard, events_list, event_leaderboard

urlpatterns = [
    path('leaderboard', leaderboard, name='leaderboard'),
    path('events', events_list, name='events'),
    path('<str:event_name>/leaderboard',
         event_leaderboard, name='event_leaderboard'),
    # path('admin/', admin.site.urls),
]
