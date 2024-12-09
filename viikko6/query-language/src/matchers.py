class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
    

class All:
    def test(self, player):
        if player:
            return True



class Not:
    def __init__(self, ehto):
        self.ehto = ehto

    def test(self, player): # eli siis käänteinen tapaus HasAtLeast luokalle
        return not self.ehto.test(player)
    


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        return getattr(player, self._attr, 0) < self._value
    

class Or:
    def __init__(self, *ehdot):
        self.ehdot = ehdot

    def test(self, player):
        for ehto in self.ehdot:
            if ehto.test(player):
                return True
        return False

