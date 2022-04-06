from django.http import JsonResponse
from .models import Player, Event, EventPlayer


def leaderboard(request):
    players = Player.objects.all().order_by('-points')
    ctx = {"players": []}
    for player in players:
        ctx["players"].append({
            "username": player.username,
            "points": player.points
        })
    return JsonResponse(ctx)


def events_list(request):
    events = Event.objects.all()
    ctx = {"events": []}
    for event in events:
        ctx["events"].append({
            "name": event.name,
        })
    return JsonResponse(ctx)


def event_leaderboard(request, event_name):
    ctx = {
        "players": []
    }
    players = EventPlayer.objects.filter(
        event__name=event_name).order_by('-event_points')
    for player in players:
        ctx["players"].append({
            "username": player.player.username,
            "points": player.event_points
        })
    return JsonResponse(ctx)
