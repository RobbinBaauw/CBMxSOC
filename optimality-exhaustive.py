from typing import List, Iterable

from math import ceil, floor, log

from src.util import range_incl

AgentId = int
Time = int

# TODO for (a), find max NF cost, for (b), find min NF cost


def generate_all_path_lenghts(sum_of_costs: int,
                              agents: int,
                              smaller_than: int = -1) -> Iterable[List[int]]:
    """
    Generates a set of path lengths for n agents.
    :return Set of path lengths for agents [1, 2, ..., n]
    """
    if smaller_than == -1:
        smaller_than = sum_of_costs

    if agents == 1 and sum_of_costs >= 1:
        yield [sum_of_costs]
    else:
        min_value = ceil(sum_of_costs / agents)
        for value in range(min_value, sum_of_costs + 1):
            if value < 1 or value > smaller_than:
                continue

            for permutation in generate_all_path_lenghts(
                    sum_of_costs - value, agents - 1, value):
                yield [value, *permutation]


def compute_for_agents(path_length: int, agent_amount: int, minimize: bool,
                       t_max: int) -> (int, List[int]):
    all_lengths = list(generate_all_path_lenghts(path_length, agent_amount))

    def get_cost(t: int, reduced: bool):
        def series_sum(n: int) -> int:
            return int((1 - agent_amount**n) / (1 - agent_amount))

        if reduced:
            return t_max - t - 1
        else:
            return agent_amount * t_max * (t_max - 1) / 2

    cost = 999_999_999 if minimize else 0
    returned_agent_lengths = []

    for agent_lengths in all_lengths:
        curr_cost = 0
        for agent_length in agent_lengths:
            for t in range_incl(0, t_max - 1):
                if t >= agent_length - 1:
                    # Once you're standing still, you get a reduced cost
                    curr_cost += get_cost(t, True)
                elif t <= agent_length - 2:
                    # Due to the definition of path length, the two timesteps before reaching the goal you definitely incur full cost
                    # This is due to the fact that you cannot be on the goal the time before the goal, so you need to step off and on again (costly)
                    curr_cost += get_cost(t, False)

        if minimize and curr_cost < cost:
            cost = curr_cost
            returned_agent_lengths = agent_lengths
        elif not minimize and curr_cost > cost:
            cost = curr_cost
            returned_agent_lengths = agent_lengths

    return cost, returned_agent_lengths


if __name__ == "__main__":
    a_all = list(range(3, 50))
    b_all = list(range(4, 52))

    for a, b in zip(a_all, b_all):
        amount_of_agents = list(range(2, a + 1))

        for agent_amount in amount_of_agents:
            t_max = b + 10

            cost_a, agent_lengths_a = compute_for_agents(a,
                                                         agent_amount,
                                                         minimize=False,
                                                         t_max=t_max)
            cost_b, agent_lengths_b = compute_for_agents(b,
                                                         agent_amount,
                                                         minimize=True,
                                                         t_max=t_max)

            if len(agent_lengths_a) == 0 or len(agent_lengths_b) == 0:
                continue

            print(
                f"{agent_amount} ({a}, {b}): Cost A {cost_a} [{agent_lengths_a}], Cost B {cost_b} [{agent_lengths_b}]"
            )
            assert cost_a < cost_b

        print("\n\n")
