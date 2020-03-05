from django.contrib import admin

# Register your models here.
from .models import Room, Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user','uuid','currentRoom')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'n_to','s_to','e_to','w_to')

admin.site.register(Player, PlayerAdmin)
admin.site.register(Room, RoomAdmin)