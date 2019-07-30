from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_expriments'
    players_per_group = 3
    num_rounds = 1

    endowment = c(100)
    multiplication_factor = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            # self.payoff = Constants.endowment
            role = "A"
            return role
        if self.id_in_group == 2:
            # self.payoff = c(50)
            role = "B1"
            return role
        if self.id_in_group == 3:
            # self.payoff = c(50)
            role = "B2"
            return role

