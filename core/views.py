import json
from django.http import HttpResponse, JsonResponse
from .models import Player, Event, EventPlayer
from django.views.decorators.csrf import csrf_exempt


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


def player_search(request):
    event = request.GET.get('event')
    name = request.GET.get('name')

    if event != "All":
        event_players = EventPlayer.objects.filter(
            event__name=event, player__username__icontains=name)
        ctx = {"players": []}

        for player in event_players:
            ctx["players"].append({
                "username": player.player.username,
                "points": player.event_points
            })
        return JsonResponse(ctx)
    else:
        players = Player.objects.filter(username__icontains=name)
        ctx = {"players": []}
        for player in players:
            ctx["players"].append({
                "username": player.username,
                "points": player.points
            })
        return JsonResponse(ctx)


@csrf_exempt
def player_registration(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        phone = data.get("phone")
        email = data.get("email")

        if Player.objects.filter(username=username).exists():
            return JsonResponse({
                "message": "Player with name already exists",
                "status": "FAILED"
            })

        if Player.objects.filter(phone=phone).exists():
            return JsonResponse({
                "message": "Player with this phone number already exists",
                "status": "FAILED"
            })

        if Player.objects.filter(email=email).exists():
            return JsonResponse({
                "message": "Player with this email already exists",
                "status": "FAILED"
            })

        player = Player(username=username, phone=phone, email=email)
        player.save()

        return JsonResponse({
            "message": "Player created successfully",
            "status": "OK"
        })
