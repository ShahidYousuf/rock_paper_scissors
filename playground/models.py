from django.db import models
from accounts.models import User


class GameLog(models.Model):
    log_text = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.log_text}"

    def get_all_games(self):
        return self.games.all()


class MoveType(models.Model):
    MOVES = (
        ('rock', 'rock'),
        ('paper', 'paper'),
        ('scissor', 'scissor'),
    )
    name = models.CharField(max_length=30, choices=MOVES, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    def get_all_moves(self):
        return self.moves.all()

    def __str__(self):
        if self.name == 'rock':
            return f"{Rock()}"
        if self.name == 'paper':
            return f"{Paper()}"
        if self.name == 'scissor':
            return f"{Scissor()}"


class Game(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    game_log = models.ForeignKey(GameLog, related_name='games', on_delete=models.CASCADE)
    rounds = models.PositiveIntegerField(default=3)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    def get_all_game_moves(self):
        return self.moves.all()


class Move(models.Model):
    player = models.ForeignKey(User, related_name='moves', on_delete=models.CASCADE)
    move_type = models.ForeignKey(MoveType, related_name='moves', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name='moves', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)


class Shape:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __eq__(self, other):
        return self._name == other.name

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"


class Rock(Shape):
    def __init__(self):
        super(Rock, self).__init__('rock')

    def __gt__(self, other):
        if other.name == 'scissor':
            return True
        else:
            return False

    def __lt__(self, other):
        if other.name == 'paper':
            return True
        else:
            return False

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    def __str__(self):
        return self.name


class Paper(Shape):
    def __init__(self):
        super(Paper, self).__init__('paper')

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    def __gt__(self, other):
        if other.name == 'rock':
            return True
        else:
            return False

    def __lt__(self, other):
        if other.name == 'scissor':
            return True
        else:
            return False

    def __str__(self):
        return self.name


class Scissor(Shape):
    def __init__(self):
        super(Scissor, self).__init__('scissor')

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    def __gt__(self, other):
        if other.name == 'paper':
            return True
        else:
            return False

    def __lt__(self, other):
        if other.name == 'rock':
            return True
        else:
            return False

    def __str__(self):
        return self.name
