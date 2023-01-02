import uuid
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    whitePlayers = models.ManyToManyField(to=User, blank=True, related_name="white_players")
    blackPlayers = models.ManyToManyField(to=User, blank=True, related_name="black_players")
    started = models.BooleanField(default=False)
    ended = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now())
    fen = models.CharField(max_length=100, default="")
    currMove1 = models.CharField(max_length=100, default="")
    currMove2 = models.CharField(max_length=100, default="")
    whiteTurn = models.BooleanField(default=True)

    def getWhiteCount(self):
        return self.whitePlayers.count()

    def getBlackCount(self):
        return self.blackPlayers.count()

    def join(self, user):
        if self.inProgress():
            return False
        if self.getWhiteCount() < 2:
            self.whitePlayers.add(user)
        elif self.getBlackCount() < 2:
            self.blackPlayers.add(user)

        if self.getWhiteCount() == 2 and self.getBlackCount() == 2:
            self.started = True
        self.save()
        return True

    def inProgress(self):
        return self.started

    def removePlayer(self, user):
        self.whitePlayers.remove(user)
        self.blackPlayers.remove(user)

    def isMyTurn(self, user):
        for player in self.whitePlayers.all():
            if player.id == user.id:
                return self.whiteTurn

        for player in self.blackPlayers.all():
            if player.id == user.id:
                return not self.whiteTurn 
        
        return False

    def makeMove(self, user, move):
        # check for move validity later 

        if not self.isMyTurn(user):
            return 

        

        

