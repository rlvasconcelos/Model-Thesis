# from BbnNetwork_Rev03 import *
import random
from pybbn.graph.jointree import EvidenceBuilder

"""
Definition of Input Variables
"""
input_variables = ['temperature', 'pH', 'alkalinity', 'total dissolved solids',
                   'hardness', 'water pressure', 'water velocity', 'turbidity']


# Check if the input parameters exist
# improve the documentation of the code

def check_input(input_variables, join_tree):
    """
    This function will check if the given input variables are correct
    :returns  If a wrong input_variable is wrong or nonexistent
    """
    for node_name in input_variables:
        node = join_tree.get_bbn_node_by_name(node_name)
        if node is None:
            return print(f"Wrong Input: {node_name}")


def random_state():
    """
    On absence of data, this function gives the node a random state
    :return: Node State
    """
    list_of_states = ['low', 'medium', 'high']
    state = random.choice(list_of_states)
    return state


def random_dictionary_input(input_variables):
    input_dictionary = {}
    list_of_states = ['low', 'medium', 'high']
    for node in input_variables:
        new_state = random.choice(list_of_states)
        input_dictionary[node] = new_state
    return input_dictionary


def set_observation(dictionary_input, join_tree):
    for key, value in dictionary_input.items():
        evidence = EvidenceBuilder() \
            .with_node(join_tree.get_bbn_node_by_name(key)) \
            .with_evidence(value, 1) \
            .build()
        join_tree.set_observation(evidence)
    return join_tree


def creating_pipe(parameters_dictionary):
    pipe_proprieties = parameters_dictionary
    return pipe_proprieties


def get_pipe_failure_risk(pipe, risk_node, bbn):
    join_tree1 = set_observation(pipe, bbn)
    potential = join_tree1.get_bbn_potential(risk_node)
    return potential


def get_scale(node, bbn):
    dict_probabilities = bbn.get_posteriors()
    weight_low = 1
    weight_medium = 2
    weight_high = 3
    for state, value in dict_probabilities[node].items():
        if state == 'low':
            scaled_low = value * weight_low
        elif state == 'medium':
            scaled_medium = value * weight_medium
        elif state == 'high':
            scaled_high = value * weight_high
    value = ((scaled_low + scaled_medium + scaled_high) - 1) / 2
    return round(value, 3)


