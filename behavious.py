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

# class CompRequest(FipaRequestProtocol):
#     """FIPA Request Behaviour of the Time agent.
#     """
#     def __init__(self, agent):
#         super(CompRequest, self).__init__(agent=agent,
#                                           message=None,
#                                           is_initiator=False)

#     def handle_request(self, message):
#         super(CompRequest, self).handle_request(message)
#         display_message(self.agent.aid.localname, 'request message received')
#         now = datetime.now()
#         reply = message.create_reply()
#         reply.set_performative(ACLMessage.INFORM)
#         reply.set_content(now.strftime('%d/%m/%Y - %H:%M:%S'))
#         self.agent.send(reply)


# class CompRequest2(FipaRequestProtocol):
#     """FIPA Request Behaviour of the Clock agent.
#     """
#     def __init__(self, agent, message):
#         super(CompRequest2, self).__init__(agent=agent,
#                                            message=message,
#                                            is_initiator=True)

#     def handle_inform(self, message):
#         display_message(self.agent.aid.localname, message.content)