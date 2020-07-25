import random
from pade.acl.messages import ACLMessage
from pade.behaviours.protocols import FipaRequestProtocol
from pade.misc.utility import display_message, start_loop
from pade.behaviours.protocols import TimedBehaviour


# n = random.randint(0,22)

class PassingBehaviour(FipaRequestProtocol):
    def __init__(self, agent):
        super(PassingBehaviour, self).__init__(agent=agent,
                                               message=None,
                                               is_initiator=False)
        print('Passing behaviour')

    def handle_request(self, message):
        super(PassingBehaviour, self).handle_request(message)
        msg = message.create_reply()
        msg.set_performative(ACLMessage.INFORM)
        msg.set_content('Ball Passed!!')
        self.agent.send(msg)


class AttackingBehaviour(FipaRequestProtocol):
    def __init__(self, agent):
        super(AttackingBehaviour, self).__init__(agent=agent, message=None, is_initiator=False)
        print('Attacking behaviour')


class BallReceivingBehaviour(FipaRequestProtocol):
    def __init__(self, agent):
        super(BallReceivingBehaviour, self).__init__(agent=agent, message=None, is_initiator=True)
        print('Ball Receiving behaviour')

    def handle_inform(self, message):
        display_message(self.agent.aid.localname, message.content)


class TemporalBehaviour(TimedBehaviour):
    def __init__(self, agent, time, message):
        super(TemporalBehaviour, self).__init__(agent, time)
        self.message = message
        print('Timed Behaviour')

    def on_time(self):
        super(TemporalBehaviour, self).on_time()
        self.agent.send(self.message)


class ComportTemporal(TimedBehaviour):
    """Timed Behaviour of the Clock agent"""

    def __init__(self, agent, time, message):
        super(ComportTemporal, self).__init__(agent, time)
        self.message = message

    def on_time(self):
        super(ComportTemporal, self).on_time()
        self.agent.send(self.message)


class Time(TimedBehaviour):

    def __init__(self, agent, notify):
        super(Time, self).__init__(agent, 1)
        self.notify = notify
        self.inc = 0

    def on_time(self):
        super(Time, self).on_time()
        message = ACLMessage(ACLMessage.INFORM)
        message.set_protocol(ACLMessage.FIPA_SUBSCRIBE_PROTOCOL)
        message.set_content(str(random.random()))
        self.notify(message)
        self.inc += 0.1
