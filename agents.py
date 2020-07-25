from pade.core.agent import Agent
from pade.misc.utility import display_message, start_loop, call_later
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID


class GoalKeeper(Agent):
    def __init__(self, aid):
        super(GoalKeeper, self).__init__(aid=aid, debug=False)
        self.message = None
        print('Goal Keeper')

    def on_start(self):
        super(GoalKeeper, self).on_start()
        display_message(self.aid.localname, 'Passing the ball to winger!!')
        call_later(8.0, self.sending_message)

    def sending_message(self):
        self.send(self.message)

    def react(self, message):
        super(GoalKeeper, self).react(message)
        display_message(self.aid.localname, 'Ball is succesfully passed to {}'.format(message))

    def set_message(self, message_content):
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID(BallReceivingWinger))
        message.set_content(message_content)
        self.message = message.as_xml()


class BallReceivingWinger(Agent):
    def __init__(self, aid):
        super(BallReceivingWinger, self).__init__(aid=aid, debug=False)
        print('Winger')

    def react(self, message):
        super(BallReceivingWinger, self).react(message)
        display_message(self.aid.localname, 'Ball received from {}'.format(message.sender.name))


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