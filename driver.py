import agents,behavious

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
    time_agent = agents.Winger(AID(name=winger1))
    agents_list.append(time_agent)

    port =int(port)+ 1000
    winger2 = 'winger_{}@localhost:{}'.format(port, port)
    time_agent = agents.Winger(AID(name=winger2))
    agents_list.append(time_agent)

    port =int(port)+ 1000
    attacker = 'attacker_{}@localhost:{}'.format(port, port)
    time_agent = agents.Striker(AID(name=attacker))
    agents_list.append(time_agent)

    port =int(port)+ 1000
    defender = 'enemy_defender_{}@localhost:{}'.format(port, port)
    time_agent = agents.Defender(AID(name=defender))
    agents_list.append(time_agent)

    port =int(port)+ 1000
    scorer = 'scorer_{}@localhost:{}'.format(port, port)
    time_agent = agents.Scorer(AID(name=scorer))
    agents_list.append(time_agent)

    print("Starting match")
    start_loop(agents_list)





if __name__ == "__main__":
    main()