from pade.core.agent import Agent
from pade.misc.utility import display_message, start_loop, call_later
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from protocols import *
from behavious import *


class GoalKeeper(Agent):
    def __init__(self, aid):
        super(GoalKeeper, self).__init__(aid=aid, debug=False)
        self.message = 'HOLA!!'
        print('Goal Keeper')

    def on_start(self):
        super(GoalKeeper, self).on_start()
        display_message(self.aid.localname, 'Passing the ball to winger!!')
        call_later(8.0, self.sending_message)

    def sending_message(self):
        self.send(self.message)

    def react(self, message):
        super(GoalKeeper, self).react(message)
        display_message(self.aid.localname, 'Ball is succesfully passed from {}'.format(message.receivers[0].name))

    def set_message(self, message_content):
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID(BallReceivingWinger))
        message.set_content(message_content)
        self.message = message.as_xml()


class BallReceivingWinger(Agent):
    def __init__(self, aid):
        super(BallReceivingWinger, self).__init__(aid=aid, debug=False)
        print('Winger')
        message = ACLMessage(ACLMessage.SUBSCRIBE)
        message.set_protocol(ACLMessage.FIPA_SUBSCRIBE_PROTOCOL)
        message.set_content("Ball!!")
        self.call_later(8.0, self.launch_subscriber_protocol, message)

    def launch_subscriber_protocol(self, message):
        self.protocol = SubscriberProtocol(self, message)
        self.behaviours.append(self.protocol)
        self.protocol.on_start()

    def react(self, message):
        super(BallReceivingWinger, self).react(message)
        display_message(self.aid.localname, 'Ball received from {}'.format(message.sender.name))



class Crowd(Agent):
    
    def __init__(self, aid, message):
        super(Crowd, self).__init__(aid)
        print('Crowd')
        self.call_later(8.0, self.launch_subscriber_protocol, message)

    def launch_subscriber_protocol(self, message):
        self.protocol = SubscriberProtocol(self, message)
        self.behaviours.append(self.protocol)
        self.protocol.on_start()


class AgentPublisher(Agent):

    def __init__(self, aid):
        super(AgentPublisher, self).__init__(aid)

        self.protocol = PublisherProtocol(self)
        self.timed = Time(self, self.protocol.notify)

        self.behaviours.append(self.protocol)
        self.behaviours.append(self.timed)


class Defender(Agent):
    def __init__(self, aid):
        super(Defender, self).__init__(aid=aid, debug=False)
        print('Defender')


class Striker(Agent):
    def __init__(self, aid):
        super(Striker, self).__init__(aid)
        print('Striker')
        self.protocol = PublisherProtocol(self)
        self.timed = Time(self, self.protocol.notify)

        self.behaviours.append(self.protocol)
        self.behaviours.append(self.timed)


class Winger(Agent):
    def __init__(self, aid):
        super(Winger, self).__init__(aid=aid, debug=False)
        print('Winger')


class Scorer(Agent):
    def __init__(self, aid):
        super(Scorer, self).__init__(aid=aid, debug=False)
        print('Scorer')


class PassingWinger(Agent):
    
    def __init__(self, aid, participants):
        super(PassingWinger, self).__init__(aid=aid, debug=False)

        message = ACLMessage(ACLMessage.CFP)
        message.set_protocol(ACLMessage.FIPA_CONTRACT_NET_PROTOCOL)
        message.set_content('60.0')

        for participant in participants:
            message.add_receiver(AID(name=participant))

        self.call_later(8.0, self.launch_contract_net_protocol, message)

    def launch_contract_net_protocol(self, message):
        comp = CompContNet1(self, message)
        self.behaviours.append(comp)
        comp.on_start()


class Defender(Agent):

    def __init__(self, aid, pot_disp):
        super(Defender, self).__init__(aid=aid, debug=False)

        self.pot_disp = pot_disp

        comp = CompContNet2(self)

        self.behaviours.append(comp)

class Attacker(Agent):
    
    def __init__(self, aid, pot_disp):
        super(Attacker, self).__init__(aid=aid, debug=False)

        self.pot_disp = pot_disp

        comp = CompContNet2(self)

        self.behaviours.append(comp)
