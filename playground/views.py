import datetime

from django.views import View
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import GameLog, Game, MoveType, Move
from .models import Rock, Paper, Scissor
from accounts.models import User


class PlayGroundView(View):
    template_name = "playground/home.html"

    def get(self, request, *args, **kwargs):
        playdroid = User.objects.get(username='PlayDroid')
        player = request.user
        context = {
            'playdroid': playdroid,
            'player': player
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        player = request.user
        bot = User.objects.get(username='PlayDroid')
        player_move_type = request.POST.get('player_move_type')
        bot_move_type = request.POST.get('bot_move_type')
        result = self._get_move_result(player_move_type, bot_move_type)  # result for player
        bot_result = 'draw'
        if result == 'win':
            bot_result = 'loss'
        if result == 'loss':
            bot_result = 'win'
        game_log = self._log(player, bot, player_move_type, bot_move_type, result)
        game = self._add_game(player, bot, game_log)
        p_move_type = MoveType.objects.get(name=player_move_type)
        b_move_type = MoveType.objects.get(name=bot_move_type)
        player_move = self._add_move(player, bot, p_move_type, game, result)
        bot_move = self._add_move(bot, player, b_move_type, game, bot_result)
        player_game_details = {
            'win_count': player.get_win_count(bot),
            'loss_count': player.get_loss_count(bot),
            'draw_count': player.get_draw_count(bot),
        }
        bot_game_details = {
            'win_count': bot.get_win_count(player),
            'loss_count': bot.get_loss_count(player),
            'draw_count': bot.get_draw_count(player),
        }

        context = {
            'success': True,
            'player_move_type': player_move_type,
            'bot_move_type': bot_move_type,
            'player_result': player_move.result,
            'bot_result': bot_move.result,
            'player_game_details': player_game_details,
            'bot_game_details': bot_game_details
        }
        return JsonResponse(context)

    def _log(self, player, bot, player_move_type, bot_move_type, result):
        now = str(datetime.datetime.now())
        player_name = player.get_full_name()
        bot_name = bot.get_full_name()
        log_text = f"{player_name} - {bot_name} : {player_move_type} - {bot_move_type} at {now} result {result}"
        game_log = GameLog(log_text=log_text)
        game_log.save()
        return game_log

    def _add_game(self, player_one, bot, game_log):
        now = str(datetime.datetime.now())
        title = f"{player_one} vs {bot} at {now} "
        game = Game(title=title)
        game.game_log = game_log
        game.save()
        return game

    def _add_move(self, player, against, move_type, game, result):
        move = Move(player=player, against=against, move_type=move_type, game=game)
        move.result = result
        move.save()
        return move

    def _get_move_result(self, player_move_type, bot_move_type):
        player_move = self._get_move_type_object(player_move_type)
        bot_move = self._get_move_type_object(bot_move_type)
        result = 'draw'
        if player_move > bot_move:
            result = 'win'
        if bot_move > player_move:
            result = 'loss'
        return result


    def _get_move_type_object(self, move_type):

        if move_type == 'rock':
            return Rock()
        if move_type == 'paper':
            return Paper()
        if move_type == 'scissor':
            return Scissor()




