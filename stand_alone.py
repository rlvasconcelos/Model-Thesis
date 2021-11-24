import bbnNodes_Rev03
import bbnNetwork_Rev03
import pybbn
from functions import *
import time
from tabulate import tabulate

input_variables = ['temperature', 'pH', 'alkalinity', 'disinfectant residual']
pipe2 = random_dictionary_input(input_variables)
distribution = get_pipe_failure_risk(pipe2, bbnNetwork_Rev03.failures_risk, bbnNetwork_Rev03.join_tree)
risk_factor = get_scale('failure risk', bbnNetwork_Rev03.join_tree)
print(tabulate(pipe2.items(), headers=['Parameter', 'State'], tablefmt="grid"))

print('Risk factor:  {}'.format(risk_factor))

print('Risk distribution: \n{}'.format(distribution))
