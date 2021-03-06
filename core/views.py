import json
from django.http import HttpResponse, JsonResponse
from .models import Player, Event, EventPlayer
from django.views.decorators.csrf import csrf_exempt


def leaderboard(request):
    players = Player.objects.all().order_by('rank', 'registration_date')[:20]
    ctx = {"players": []}
    for player in players:
        ctx["players"].append({
            "username": player.username,
            "points": player.points,
            "rank": player.rank
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


def player_search(request):
    name = request.GET.get('name')
    players = Player.objects.filter(username__icontains=name)[:20]
    ctx = {"players": []}
    for player in players:
        ctx["players"].append({
            "username": player.username,
            "points": player.points,
            "rank": player.rank
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

        last_player_rank = Player.objects.last().rank
        player = Player(username=username, phone=phone, email=email, rank=last_player_rank+1)
        player.save()

        return JsonResponse({
            "message": "Player created successfully",
            "status": "OK"
        })
