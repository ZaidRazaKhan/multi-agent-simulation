import agents,behavious
from agents import Striker, Crowd
from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaRequestProtocol
from pade.behaviours.protocols import TimedBehaviour

from datetime import datetime
from sys import argv



def main():

    c = 0
    agents_list = list()
    port = argv[1]

    goal_keeper = 'goalkeeper_{}@localhost:{}'.format(port, port)
    time_agent = agents.GoalKeeper(AID(name=goal_keeper))
    agents_list.append(time_agent)

    port =int(port)+ 1000
    winger1 = 'winger_{}@localhost:{}'.format(port, port)
    time_agent = agents.BallReceivingWinger(AID(name=winger1))
    agents_list.append(time_agent)
    
    
    participants = list()
    agent_name = 'Striker_{}@localhost:{}'.format(port+2, port+2)
    participants.append(agent_name)
    agent_pub_1 = Striker(AID(name=agent_name))
    agents_list.append(agent_pub_1)

    msg = ACLMessage(ACLMessage.SUBSCRIBE)
    msg.set_protocol(ACLMessage.FIPA_SUBSCRIBE_PROTOCOL)
    msg.set_content('Goal!!')
    msg.add_receiver(agent_pub_1.aid)
    k = 10
    agent_name = 'Crowd_20010@localhost:20010'
    participants.append(agent_name)
    agent_sub_1 = Crowd(AID(name=agent_name), msg)
    agents_list.append(agent_sub_1)

    agent_name = 'Crowd_19990@localhost:19990'
    agent_sub_2 = Crowd(AID(name=agent_name), msg)
    agents_list.append(agent_sub_2)


    # port =int(port)+ 1000
    # winger2 = 'winger_{}@localhost:{}'.format(port, port)
    # time_agent = agents.Winger(AID(name=winger2))
    # agents_list.append(time_agent)

    # port =int(port)+ 1000
    # attacker = 'attacker_{}@localhost:{}'.format(port, port)
    # time_agent = agents.Striker(AID(name=attacker))
    # agents_list.append(time_agent)

    # port =int(port)+ 1000
    # defender = 'enemy_defender_{}@localhost:{}'.format(port, port)
    # time_agent = agents.Defender(AID(name=defender))
    # agents_list.append(time_agent)

    # port =int(port)+ 1000
    # scorer = 'scorer_{}@localhost:{}'.format(port, port)
    # time_agent = agents.Scorer(AID(name=scorer))
    # agents_list.append(time_agent)

    print("Starting match")
    start_loop(agents_list)





if __name__ == "__main__":
    main()