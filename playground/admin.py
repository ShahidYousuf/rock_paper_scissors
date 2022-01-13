from django.contrib import admin
from .models import GameLog, MoveType, Game, Move


class GameLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'log_text', 'created_on')


class MoveTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_on')


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rounds', 'created_on')


class MoveAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'against', 'move_type', 'game', 'result', 'created_on')


admin.site.register(GameLog, GameLogAdmin)
admin.site.register(MoveType, MoveTypeAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Move, MoveAdmin)