from django.contrib import admin
from .models import Player, Event, EventPlayer
# from django_admin_listfilter_dropdown.filters import DropdownFilter


def add_10_points(modeladmin, request, queryset):
    for obj in queryset:
        player = obj.player
        player.points += 10
        player.save()
        obj.event_points += 10
        obj.save()

def add_20_points(modeladmin, request, queryset):
    for obj in queryset:
        player = obj.player
        obj.player.points += 20
        player.save()
        obj.event_points += 20
        obj.save()

class EventAdmin(admin.ModelAdmin):
    search_fields = ('name', )

class PlayerAdmin(admin.ModelAdmin):
    search_fields = ['username', 'phone']
    list_display = ['username', 'phone', 'points']
    readonly_fields = ('points',)

class EventPlayerAdmin(admin.ModelAdmin):
    list_display = ['player','event','event_points']
    search_fields = ('event__name', 'player__username')
    autocomplete_fields = ('event', 'player' )
    readonly_fields = ('event_points',)
    list_filter = ('event__name',)
    actions = [add_10_points, add_20_points] 

admin.site.site_header = 'Inertia Admin'
admin.site.register(Player, PlayerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventPlayer, EventPlayerAdmin)