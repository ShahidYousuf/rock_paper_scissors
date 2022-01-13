from django import template
from accounts.models import User
register = template.Library()


@register.simple_tag
def get_player_win_count(player, against):
    return player.get_win_count(against)

@register.simple_tag
def get_player_loss_count(player, against):
    return player.get_loss_count(against)

@register.simple_tag
def get_player_draw_count(player, against):
    return player.get_draw_count(against)

@register.simple_tag
def get_bot_win_count(bot, against):
    return bot.get_win_count(against)

@register.simple_tag
def get_bot_loss_count(bot, against):
    return bot.get_loss_count(against)

@register.simple_tag
def get_bot_draw_count(bot, against):
    return bot.get_draw_count(against)
