from core.models import Player
player_set = list(Player.objects.order_by("-points", "registration_date"))
for i in range(len(player_set)):
    player = player_set[i]
    player.rank = i + 1
    player.save()