from django.urls import path
from .views import leaderboard, events_list, player_search, player_registration

urlpatterns = [
    path('player-register', player_registration, name='player-register'),
    path('leaderboard', leaderboard, name='leaderboard'),
    path('events', events_list, name='events'),
    path('player-search', player_search, name='player_search'),
    # path('<str:event_name>/leaderboard',
    #      event_leaderboard, name='event_leaderboard')
]
