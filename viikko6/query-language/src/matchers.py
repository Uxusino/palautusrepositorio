class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def get_matchers(self):
        return self._matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
            
        return False

class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)
    
class All:
    def __init__(self):
        pass

    def test(self, player):
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
    
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class QueryBuilder:
    def __init__(self, *matchers):
        self._matchers = matchers or (All(),)

    def build(self):
        return And(*self._matchers)
    
    def get_matchers(self):
        return self._matchers
    
    def one_of(self, *matchers):
        self._matchers = (Or(*matchers),)
        
        return self
    
    def plays_in(self, team: str) -> "QueryBuilder":

        return QueryBuilder(*self._matchers, PlaysIn(team))
    
    def has_at_least(self, value, attr) -> "QueryBuilder":

        return QueryBuilder(*self._matchers, HasAtLeast(value, attr))
    
    def has_fewer_than(self, value, attr) -> "QueryBuilder":

        return QueryBuilder(*self._matchers, HasFewerThan(value, attr))