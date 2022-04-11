from django.db import models

# Create your models here.


class Player(models.Model):
    username = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True, default="")
    points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)
    registration_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.username


class Event(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class EventPlayer(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    event_points = models.PositiveIntegerField(default=0)
    registration_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.event) + " - " + str(self.player.username)
