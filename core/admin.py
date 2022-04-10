from django.contrib import admin
from .models import Player, Event, EventPlayer


def add_10_points(modeladmin, request, queryset):
    for obj in queryset:
        player = obj.player
        player.points += 10
        from_rank = player.rank
        if Player.objects.filter(points__gte=player.points).exists():
            last_player = Player.objects.filter(points__gte=player.points).exclude(username=player.username).last()
            r = last_player.rank
            player.rank = r + 1
        else:
            player.rank = 1

        to_rank = player.rank
        print("For", player, ":")
        print(f"{player} went from {from_rank} to {to_rank}")
        
        if from_rank != to_rank:
            for p in Player.objects.filter(rank__gte=to_rank, rank__lt=from_rank):
                print(f"{p} reduced rank from {p.rank}")
                p.rank += 1
                p.save()
                print(f"{p} reduced rank to {p.rank}")

        player.save()

        obj.event_points += 10
        obj.save()
        print("----")



def add_20_points(modeladmin, request, queryset):
    for obj in queryset:
        player = obj.player
        player.points += 20
        from_rank = player.rank
        if Player.objects.filter(points__gte=player.points).exists():
            last_player = Player.objects.filter(points__gte=player.points).exclude(username=player.username).last()
            r = last_player.rank
            player.rank = r + 1
        else:
            player.rank = 1

        to_rank = player.rank
        print("For", player, ":")
        print(f"{player} went from {from_rank} to {to_rank}")
        print("Shifting down:", Player.objects.filter(rank__gte=to_rank, rank__lt=from_rank))
        if from_rank != to_rank:
            for p in Player.objects.filter(rank__gte=to_rank, rank__lt=from_rank):
                print(f"{p} reduced rank from {p.rank}")
                p.rank += 1
                p.save()
                print(f"{p} reduced rank to {p.rank}")
        player.save()
        obj.event_points += 20
        obj.save()
        print("----")


class EventAdmin(admin.ModelAdmin):
    search_fields = ('name', )


class PlayerAdmin(admin.ModelAdmin):
    search_fields = ['username', 'phone']
    list_display = ['username', 'phone', 'email', 'points', 'rank']
    # readonly_fields = ('points',)


class EventPlayerAdmin(admin.ModelAdmin):
    list_display = ['player', 'event', 'event_points']
    search_fields = ('event__name', 'player__username')
    autocomplete_fields = ('event', 'player')
    # readonly_fields = ('event_points',)
    list_filter = ('event__name',)
    actions = [add_10_points, add_20_points]


admin.site.site_header = 'Inertia Admin'
admin.site.register(Player, PlayerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventPlayer, EventPlayerAdmin)
