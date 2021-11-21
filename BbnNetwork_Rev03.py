import pybbn
from pybbn.graph.potential import Potential
from pybbn.generator.bbngenerator import convert_for_drawing
from pybbn.graph.dag import Bbn
from pybbn.graph.dag import Dag
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
import math
from pybbn.pptc.inferencecontroller import InferenceController
import matplotlib.pyplot as plt
from BbnNodes_Rev03 import *
from pybbn.graph.graph import Graph
from pybbn.graph.dag import Dag
import networkx as nx
import warnings
import pygraphviz
import graphviz
bbn = Bbn()\
    .add_node(pH)\
    .add_node(alkalinity)\
    .add_node(hardness)\
    .add_node(turbidity)\
    .add_node(color)\
    .add_node(tds)\
    .add_node(temperature)\
    .add_node(water_pressure)\
    .add_node(water_velocity)\
    .add_node(dissolved_oxygen)\
    .add_node(disinfectant_residual)\
    .add_node(pipe_scales)\
    .add_node(hydraulic_capacity)\
    .add_node(oxidation_potential)\
    .add_node(biofilm)\
    .add_node(water_corrosion)\
    .add_node(material_accumulation)\
    .add_node(failures_risk)\
    .add_node(environmental_condition)\
    .add_node(water_aggressiveness)\
    .add_node(inorganic_matter)\
    .add_node(particle_deposition)\
    .add_node(particle_resuspension)\
    .add_node(bacteria_growth)\
    .add_node(microbial_corrosion)\
    .add_node(corrosion)\
    .add_node(water_quality_risk)\
    .add_edge(Edge(water_velocity, hydraulic_capacity, EdgeType.DIRECTED))\
    .add_edge(Edge(water_pressure, hydraulic_capacity, EdgeType.DIRECTED))\
    .add_edge(Edge(hydraulic_capacity, particle_resuspension, EdgeType.DIRECTED))\
    .add_edge(Edge(hydraulic_capacity, particle_deposition, EdgeType.DIRECTED))\
    .add_edge(Edge(particle_resuspension, color, EdgeType.DIRECTED))\
    .add_edge(Edge(particle_deposition, pipe_scales, EdgeType.DIRECTED))\
    .add_edge(Edge(inorganic_matter, pipe_scales, EdgeType.DIRECTED))\
    .add_edge(Edge(water_aggressiveness, pipe_scales, EdgeType.DIRECTED))\
    .add_edge(Edge(pipe_scales, material_accumulation, EdgeType.DIRECTED))\
    .add_edge(Edge(material_accumulation, color, EdgeType.DIRECTED))\
    .add_edge(Edge(turbidity, color, EdgeType.DIRECTED))\
    .add_edge(Edge(color, water_quality_risk, EdgeType.DIRECTED))\
    .add_edge(Edge(tds, inorganic_matter, EdgeType.DIRECTED))\
    .add_edge(Edge(hardness, inorganic_matter, EdgeType.DIRECTED))\
    .add_edge(Edge(pH, environmental_condition, EdgeType.DIRECTED))\
    .add_edge(Edge(pH, water_aggressiveness, EdgeType.DIRECTED))\
    .add_edge(Edge(temperature, environmental_condition, EdgeType.DIRECTED))\
    .add_edge(Edge(temperature, disinfectant_residual, EdgeType.DIRECTED))\
    .add_edge(Edge(water_velocity, disinfectant_residual, EdgeType.DIRECTED))\
    .add_edge(Edge(temperature, dissolved_oxygen, EdgeType.DIRECTED))\
    .add_edge(Edge(disinfectant_residual, oxidation_potential, EdgeType.DIRECTED))\
    .add_edge(Edge(dissolved_oxygen, oxidation_potential, EdgeType.DIRECTED))\
    .add_edge(Edge(water_aggressiveness, water_corrosion, EdgeType.DIRECTED))\
    .add_edge(Edge(oxidation_potential, water_corrosion, EdgeType.DIRECTED))\
    .add_edge(Edge(disinfectant_residual, bacteria_growth, EdgeType.DIRECTED))\
    .add_edge(Edge(disinfectant_residual, biofilm, EdgeType.DIRECTED))\
    .add_edge(Edge(environmental_condition, bacteria_growth, EdgeType.DIRECTED))\
    .add_edge(Edge(biofilm, microbial_corrosion, EdgeType.DIRECTED))\
    .add_edge(Edge(microbial_corrosion, corrosion, EdgeType.DIRECTED))\
    .add_edge(Edge(water_corrosion, corrosion, EdgeType.DIRECTED))\
    .add_edge(Edge(corrosion, failures_risk, EdgeType.DIRECTED))\
    .add_edge(Edge(water_quality_risk, failures_risk, EdgeType.DIRECTED))\
    .add_edge(Edge(bacteria_growth, water_quality_risk, EdgeType.DIRECTED))\
    .add_edge(Edge(biofilm, material_accumulation, EdgeType.DIRECTED))\
    .add_edge(Edge(alkalinity, water_aggressiveness, EdgeType.DIRECTED))\







# .add_edge(Edge(color, col, EdgeType.DIRECTED))\
"""
with warnings.catch_warnings():
    warnings.simplefilter('ignore')

    graph = convert_for_drawing(bbn)
    pos = nx.nx_agraph.graphviz_layout(graph, prog='neato')
plt.figure(figsize=(20, 10))
plt.subplot(121)
labels = dict([(k, node.variable.name) for k, node in bbn.nodes.items()])
nx.draw(graph, pos=pos, with_labels=True, labels=labels)
plt.title('BBN DAG')

plt.show()

"""

join_tree = InferenceController.apply(bbn)


"""
Creating Evidences
"""
ev1 = EvidenceBuilder() \
    .with_node(join_tree.get_bbn_node_by_name('corrosion')) \
    .with_evidence('low', 1) \
    .build()
# ev2 = EvidenceBuilder() \
#     .with_node(join_tree.get_bbn_node_by_name('environmental condition')) \
#     .with_evidence('medium', 1) \
#     .build()

# ev3 = EvidenceBuilder() \
#     .with_node(join_tree.get_bbn_node_by_name('particle deposition')) \
#     .with_evidence('low', 1) \
#     .build()

"""
Insert Evidences into the model#
"""

join_tree.set_observation(ev1)
# join_tree.set_observation(ev2)
# join_tree.set_observation(ev3)

"""
Print the marginal probabilities
"""

parent_state1 = join_tree.get_bbn_potential(corrosion)
# parent_state2 = join_tree.get_bbn_potential(environmental_condition)
# parent_state3 = join_tree.get_bbn_potential(particle_deposition)
print()
print(parent_state1)
print('--------------------->')
# print()
# print(parent_state2)
# print('--------------------->')
# # print()
# print(parent_state3)
# print('--------------------->')

"""
Print the posterior probabilities
"""

potential = join_tree.get_bbn_potential(failures_risk)

print(potential)
print('--------------------->')

# def evidence(ev, nod, cat, val):
#     ev = EvidenceBuilder() \
#     .with_node(join_tree.get_bbn_node_by_name(nod)) \
#     .with_evidence(cat, val) \
#     .build()
#     join_tree.set_observation(ev)
#r