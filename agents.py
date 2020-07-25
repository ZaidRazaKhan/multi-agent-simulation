from pade.core.agent import Agent


class GoalKeeper(Agent):
    def __init__(self, aid):
        super(GoalKeeper, self).__init__(aid=aid, debug=False)
        print('Goal Keeper')


class Defender(Agent):
    def __init__(self, aid):
        super(Defender, self).__init__(aid=aid, debug=False)
        print('Defender')


class Striker(Agent):
    def __init__(self, aid):
        super(Striker, self).__init__(aid=aid, debug=False)
        print('Striker')


class Winger(Agent):
    def __init__(self, aid):
        super(Winger, self).__init__(aid=aid, debug=False)
        print('Winger')


class Scorer(Agent):
    def __init__(self, aid):
        super(Scorer, self).__init__(aid=aid, debug=False)
        print('Scorer')



# class AgenteHelloWorld(Agent):
#     def __init__(self, aid):
#         super(AgenteHelloWorld, self).__init__(aid=aid, debug=False)

#         comp_temp = ComportTemporal(self, 1.0)

#         self.behaviours.append(comp_temp)