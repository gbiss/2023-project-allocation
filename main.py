# %%
from agent_functions import Agent, gen_random_agents
from item_functions import generate_items_from_schedule
from allocation_functions import yankee_swap, SPIRE_algorithm, round_robin
from metric_functions import utilitarian_welfare, nash_welfare, EF, EF_1, EF_X
import matplotlib.pyplot as plt
import random
import numpy as np



items=generate_items_from_schedule('fall2023schedule-2.xlsx')
# for item in items:
#     print('Course:',item.item_id,'Timeslot:',item.timeslot,'Capacity:',item.capacity)
n=2000
for seed in [0,1,2,3,4,5,6,7,8,9]:
    random.seed(seed)
    np.random.seed(seed)
    agents=gen_random_agents(n,items)
    for agent in agents:
        print(agent.id, 'cap:', agent.cap)
        print('desired items: ',agent.desired_items)
    X,time_steps,agents_involved_arr=yankee_swap(agents, items, plot_exchange_graph=False)
    np.savez(f'YS_{n}_{seed}.npz',X=X,time_steps=time_steps,num_agents_involved=agents_involved_arr)


# ####TEST EXAMPLE
# #Create agents with preferences 
# agent1=Agent('student1',[items[0].item_id, items[1].item_id,  items[20].item_id, items[30].item_id,items[25].item_id,items[40].item_id], 10)
# agent2=Agent('student1',[items[0].item_id, items[1].item_id,  items[20].item_id, items[30].item_id], 10)
# agent3=Agent('student1',[items[0].item_id, items[1].item_id], 10)
# agent4=Agent('student1',[items[0].item_id], 10)
# agents=[agent1, agent2,agent3, agent4]
# # #agents=[agent1, agent2,agent3, agent4,agent1, agent2,agent3, agent4,agent1, agent2,agent3, agent4]

# # for i in range(100):
# #      num=random.randint(0, 3)    
# #      agents.append(agents[num])

# #Generate reduced list of items with capacity of 1
# #Reduce capacities
# items[0].capacity=1
# items[1].capacity=1
# items[20].capacity=1
# items[25].capacity=1
# items[30].capacity=1
# items[40].capacity=1
# items=[items[0], items[1],items[20],items[25], items[30], items[40]]


##Running the algorithms

# X=yankee_swap(agents, items, plot_exchange_graph=False)
# print('Yankee Swap Allocation')
# print(X)
# print('Utilitatian: ',utilitarian_welfare(X,agents,items))
# print('Nash: ',nash_welfare(X, agents,items))
# print('EF: ',EF(X, agents,items))
# print('EF_1: ',EF_1(X, agents,items))
# print('EF_X: ',EF_X(X, agents,items))
# X=round_robin(agents,items)
# print('Round Robin Allocation')
# print(X)
# print('Utilitatian: ',utilitarian_welfare(X,agents,items))
# print('Nash: ',nash_welfare(X, agents,items))
# print('EF: ',EF(X, agents,items))
# print('EF_1: ',EF_1(X, agents,items))
# print('EF_X: ',EF_X(X, agents,items))
# X=SPIRE_algorithm(agents,items)
# print(X)
# print('SPIRE Allocation')
# print('Utilitatian: ',utilitarian_welfare(X,agents,items))
# print('Nash: ',nash_welfare(X, agents,items))
# print('EF: ',EF(X, agents,items))
# print('EF_1: ',EF_1(X, agents,items))
# print('EF_X: ',EF_X(X, agents,items))


# %%
