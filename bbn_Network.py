from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController
import functions
import pandas as pd
import time

def ApplyModel(Dictionary_Quality, Dataframe_Network):
    pH = BbnNode(Variable(0, 'pH', ['low', 'medium', 'high']), [0.25, 0.5, 0.25])
    alkalinity = BbnNode(Variable(1, 'alkalinity', ['low', 'medium', 'high']), [0.34, 0.33, 0.33])
    hardness = BbnNode(Variable(2, 'hardness', ['low', 'medium', 'high']), [0.34, 0.33, 0.33])
    turbidity = BbnNode(Variable(3, 'turbidity', ['low', 'medium', 'high']), [0.34, 0.33, 0.33])
    dissolved_oxygen = BbnNode(Variable(4, 'dissolved oxygen', ['low', 'medium', 'high']),[0.05, 0.05, 0.9,
                                                                                           0.05, 0.9, 0.05,
                                                                                           0.9, 0.05, 0.05])
    temperature = BbnNode(Variable(5, 'temperature', ['low', 'medium', 'high']), [0.34, 0.33, 0.33])
    tds = BbnNode(Variable(6, 'total dissolved solids', ['low', 'medium', 'high']), [0.34, 0.33, 0.33])
    water_velocity = BbnNode(Variable(7, 'water velocity', ['low', 'medium', 'high']), [0.33, 0.34, 0.33])
    water_pressure = BbnNode(Variable(8, 'water pressure', ['low', 'medium', 'high']), [0.33, 0.34, 0.33])
    hydraulic_capacity = BbnNode(Variable(9, 'hydraulic capacity', ['low', 'medium', 'high']), [0.85, 0.15, 0.0,
                                                                                                0.70, 0.25, 0.05,
                                                                                                0.5, 0.40, 0.1,
                                                                                                0.2, 0.70, 0.1,
                                                                                                0.09, 0.85, 0.06,
                                                                                                0.05, 0.7, 0.25,
                                                                                                0.1, 0.2, 0.70,
                                                                                                0.05, 0.2, 0.75,
                                                                                                0, 0.15, 0.85])
    inorganic_matter = BbnNode(Variable(10, 'inorganic matter', ['low', 'medium', 'high']), [0.82, 0.09, 0.09,
                                                                                             0.56, 0.36, 0.08,
                                                                                             0.45, 0.45, 0.10,
                                                                                             0.4, 0.5, 0.10,
                                                                                             0.1, 0.72, 0.18,
                                                                                             0.05, 0.65, 0.30,
                                                                                             0.15, 0.58, 0.27,
                                                                                             0.08, 0.35, 0.57,
                                                                                             0.0, 0.1, 0.9])
    disinfectant_residual = BbnNode(Variable(11, 'disinfectant residual', ['low', 'medium', 'high']), [0.10, 0.40, 0.5,
                                                                                                       0.40, 0.45, 0.15,
                                                                                                       0.85, 0.1, 0.05,
                                                                                                       0.15, 0.50, 0.35,
                                                                                                       0.2, 0.6, 0.2,
                                                                                                       0.31, 0.52, 0.17,
                                                                                                       0.0, 0.17, 0.83,
                                                                                                       0.10, 0.25, 0.65,
                                                                                                       0.17, 0.31, 0.52])
    oxidation_potential = BbnNode(Variable(12, 'oxidation potential', ['low', 'medium', 'high']), [0.9, 0.1, 0,
                                                                                                   0.65, 0.30, 0.05,
                                                                                                   0.55, 0.35, 0.1,
                                                                                                   0.25, 0.70, 0.05,
                                                                                                   0.15, 0.75, 0.1,
                                                                                                   0.05, 0.8, 0.15,
                                                                                                   0.05, 0.30, 0.65,
                                                                                                   0, 0.25, 0.75,
                                                                                                   0, 0.15, 0.85])
    water_corrosion = BbnNode(Variable(13, 'water corrosion', ['low', 'medium', 'high']), [0.9, 0.1, 0,
                                                                                           0.5, 0.45, 0.05,
                                                                                           0.35, 0.50, 0.15,
                                                                                           0.7, 0.25, 0.05,
                                                                                           0.15, 0.60, 0.25,
                                                                                           0.10, 0.25, 0.65,
                                                                                           0.10, 0.45, 0.45,
                                                                                           0.05, 0.35, 0.60,
                                                                                           0.0, 0.1, 0.9])
    water_aggressiveness = BbnNode(Variable(14, 'water aggressiveness', ['low', 'medium', 'high']), [0.05, 0.2, 0.75,
                                                                                                     0.05, 0.30, 0.65,
                                                                                                     0.15, 0.25, 0.60,
                                                                                                     0.25, 0.5, 0.25,
                                                                                                     0.2, 0.6, 0.2,
                                                                                                     0.15, 0.7, 0.15,
                                                                                                     0.54, 0.27, 0.19,
                                                                                                     0.58, 0.25, 0.17,
                                                                                                     0.8, 0.15, 0.05])
    corrosion = BbnNode(Variable(15, 'corrosion', ['low', 'medium', 'high']), [0.82, 0.15, 0.03,
                                                                               0.60, 0.32, 0.08,
                                                                               0.50, 0.40, 0.10,
                                                                               0.3, 0.55, 0.15,
                                                                               0.18, 0.64, 0.18,
                                                                               0.12, 0.55, 0.33,
                                                                               0.10, 0.37, 0.53,
                                                                               0.05, 0.27, 0.68,
                                                                               0.09, 0.09, 0.82])
    microbial_corrosion = BbnNode(Variable(16, 'microbial corrosion', ['low', 'medium', 'high']), [0.7, 0.2, 0.1,
                                                                                                   0.25, 0.5, 0.25,
                                                                                                   0.1, 0.2, 0.7])
    biofilm = BbnNode(Variable(17, 'biofilm', ['low', 'medium', 'high']), [0.1, 0.2, 0.7,
                                                                           0.25, 0.5, 0.25,
                                                                           0.7, 0.2, 0.1])
    particle_deposition = BbnNode(Variable(18, 'particle deposition', ['low', 'medium', 'high']), [0.05, 0.2, 0.75,
                                                                                                   0.15, 0.65, 0.2,
                                                                                                   0.7, 0.2, 0.1])
    particle_resuspension = BbnNode(Variable(19, 'particle resuspension', ['low', 'medium', 'high']), [0.75, 0.2, 0.05,
                                                                                                       0.15, 0.70, 0.15,
                                                                                                       0.05, 0.2, 0.75])
    failures_risk = BbnNode(Variable(20, 'failure risk', ['low', 'medium', 'high']), [0.82, 0.09, 0.09,
                                                                                      0.55, 0.27, 0.18,
                                                                                      0.27, 0.46, 0.27,
                                                                                      0.55, 0.27, 0.18,
                                                                                      0.18, 0.64, 0.18,
                                                                                      0.18, 0.27, 0.55,
                                                                                      0.27, 0.46, 0.27,
                                                                                      0.18, 0.27, 0.55,
                                                                                      0.09, 0.09, 0.82])
    water_quality_risk = BbnNode(Variable(21, 'water quality risk', ['low', 'medium', 'high']), [0.82, 0.09, 0.09,
                                                                                                 0.55, 0.27, 0.18,
                                                                                                 0.27, 0.46, 0.27,
                                                                                                 0.55, 0.27, 0.18,
                                                                                                 0.18, 0.64, 0.18,
                                                                                                 0.18, 0.27, 0.55,
                                                                                                 0.27, 0.46, 0.27,
                                                                                                 0.18, 0.27, 0.55,
                                                                                                 0.09, 0.09, 0.82])
    material_accumulation = BbnNode(Variable(22, 'material accumulation', ['low', 'medium', 'high']), [0.82, 0.09, 0.09,
                                                                                                       0.45, 0.45, 0.1,
                                                                                                       0.2, 0.63, 0.17,
                                                                                                       0.40, 0.45, 0.15,
                                                                                                       0.13, 0.77, 0.10,
                                                                                                       0.08, 0.50, 0.52,
                                                                                                       0.2, 0.53, 0.27,
                                                                                                       0.05, 0.2, 0.75,
                                                                                                       0.03, 0.15, 0.82])
    environmental_condition = BbnNode(Variable(23, 'environmental condition', ['low', 'medium', 'high']), [0.82, 0.09, 0.09,
                                                                                                           0.56, 0.26, 0.18,
                                                                                                           0.29, 0.44, 0.27,
                                                                                                           0.27, 0.55, 0.18,
                                                                                                           0.18, 0.64, 0.18,
                                                                                                           0.11, 0.64, 0.25,
                                                                                                           0.27, 0.46, 0.27,
                                                                                                           0.16, 0.28, 0.56,
                                                                                                           0.09, 0.09, 0.82])
    bacteria_growth = BbnNode(Variable(24, 'bacteria growth', ['low', 'medium', 'high']), [0.72, 0.2, 0.08,
                                                                                            0.05, 0.1, 0.85,
                                                                                            0.72, 0.2, 0.08,
                                                                                            0.8, 0.2, 0,
                                                                                            0.1, 0.2, 0.7,
                                                                                            0.8, 0.2, 0,
                                                                                            0.85, 0.15, 0,
                                                                                            0.25, 0.2, 0.55,
                                                                                            0.85, 0.15, 0])
    pipe_scales = BbnNode(Variable(25, 'pipe scales', ['low', 'medium', 'high']), [0.85, 0.15, 0,
                                                                                   0.75, 0.2, 0.05,
                                                                                   0.65, 0.25, 0.1,
                                                                                   0.15, 0.6, 0.25,
                                                                                   0.1, 0.55, 0.35,
                                                                                   0.05, 0.5, 0.45,
                                                                                   0.05, 0.35, 0.6,
                                                                                   0.05, 0.4, 0.55,
                                                                                   0, 0.4, 0.6,
                                                                                   0.6, 0.35, 0.05,
                                                                                   0.55, 0.4, 0.05,
                                                                                   0.45, 0.4, 0.15,
                                                                                   0.05, 0.7, 0.25,
                                                                                   0.05, 0.8, 0.15,
                                                                                   0, 0.75, 0.25,
                                                                                   0, 0.25, 0.75,
                                                                                   0, 0.2, 0.8,
                                                                                   0, 0.1, 0.9,
                                                                                   0.3, 0.6, 0.1,
                                                                                   0.25, 0.65, 0.1,
                                                                                   0.15, 0.65, 0.2,
                                                                                   0.05, 0.6, 0.35,
                                                                                   0.05, 0.55, 0.4,
                                                                                   0, 0.5, 0.5,
                                                                                   0.1, 0.15, 0.75,
                                                                                   0.05, 0.2, 0.75,
                                                                                   0, 0.2, 0.8])
    color = BbnNode(Variable(26, 'color', ['low', 'medium', 'high']), [0.85, 0.15, 0,
                                                                       0.75, 0.2, 0.05,
                                                                       0.65, 0.25, 0.1,
                                                                       0.15, 0.6, 0.25,
                                                                       0.1, 0.55, 0.35,
                                                                       0.05, 0.5, 0.45,
                                                                       0.05, 0.35, 0.6,
                                                                       0.05, 0.4, 0.55,
                                                                       0, 0.4, 0.6,
                                                                       0.6, 0.35, 0.05,
                                                                       0.55, 0.4, 0.05,
                                                                       0.45, 0.4, 0.15,
                                                                       0.05, 0.7, 0.25,
                                                                       0.05, 0.8, 0.15,
                                                                       0, 0.75, 0.25,
                                                                       0, 0.25, 0.75,
                                                                       0, 0.2, 0.8,
                                                                       0, 0.1, 0.9,
                                                                       0.3, 0.6, 0.1,
                                                                       0.25, 0.65, 0.1,
                                                                       0.15, 0.65, 0.2,
                                                                       0.05, 0.6, 0.35,
                                                                       0.05, 0.55, 0.4,
                                                                       0, 0.5, 0.5,
                                                                       0.1, 0.15, 0.75,
                                                                       0.05, 0.2, 0.75,
                                                                       0, 0.2, 0.8])
    pipe_material = BbnNode(Variable(27, 'pipe material', ['metallic', 'polymeric', 'cement']), [0.34, 0.33, 0.33])
    internal_deterioration = BbnNode(Variable(28, 'internal deterioration', ['low', 'medium', 'high']), [0.83, 0.15, 0.02,
                                                                                                         0.95, 0.05, 0,
                                                                                                         0.1, 0.2, 0.7,
                                                                                                         0.16, 0.75, 0.09,
                                                                                                         0.6, 0.3, 0.1,
                                                                                                         0.35, 0.55, 0.1,
                                                                                                         0, 0.1, 0.9,
                                                                                                         0.1, 0.25, 0.65,
                                                                                                         0.7, 0.2, 0.1])




    bbn = Bbn() \
        .add_node(pH) \
        .add_node(alkalinity) \
        .add_node(hardness) \
        .add_node(turbidity) \
        .add_node(color) \
        .add_node(tds) \
        .add_node(temperature) \
        .add_node(water_pressure) \
        .add_node(water_velocity) \
        .add_node(dissolved_oxygen) \
        .add_node(disinfectant_residual) \
        .add_node(pipe_scales) \
        .add_node(hydraulic_capacity) \
        .add_node(oxidation_potential) \
        .add_node(biofilm) \
        .add_node(water_corrosion) \
        .add_node(material_accumulation) \
        .add_node(failures_risk) \
        .add_node(environmental_condition) \
        .add_node(water_aggressiveness) \
        .add_node(inorganic_matter) \
        .add_node(particle_deposition) \
        .add_node(particle_resuspension) \
        .add_node(bacteria_growth) \
        .add_node(microbial_corrosion) \
        .add_node(corrosion) \
        .add_node(water_quality_risk) \
        .add_node(pipe_material) \
        .add_edge(Edge(water_velocity, hydraulic_capacity, EdgeType.DIRECTED)) \
        .add_edge(Edge(water_pressure, hydraulic_capacity, EdgeType.DIRECTED)) \
        .add_edge(Edge(hydraulic_capacity, particle_resuspension, EdgeType.DIRECTED)) \
        .add_edge(Edge(hydraulic_capacity, particle_deposition, EdgeType.DIRECTED)) \
        .add_edge(Edge(particle_resuspension, color, EdgeType.DIRECTED)) \
        .add_edge(Edge(particle_deposition, pipe_scales, EdgeType.DIRECTED)) \
        .add_edge(Edge(inorganic_matter, pipe_scales, EdgeType.DIRECTED)) \
        .add_edge(Edge(water_aggressiveness, pipe_scales, EdgeType.DIRECTED)) \
        .add_edge(Edge(pipe_scales, material_accumulation, EdgeType.DIRECTED)) \
        .add_edge(Edge(material_accumulation, color, EdgeType.DIRECTED)) \
        .add_edge(Edge(turbidity, color, EdgeType.DIRECTED)) \
        .add_edge(Edge(color, water_quality_risk, EdgeType.DIRECTED)) \
        .add_edge(Edge(tds, inorganic_matter, EdgeType.DIRECTED)) \
        .add_edge(Edge(hardness, inorganic_matter, EdgeType.DIRECTED)) \
        .add_edge(Edge(pH, environmental_condition, EdgeType.DIRECTED)) \
        .add_edge(Edge(pH, water_aggressiveness, EdgeType.DIRECTED)) \
        .add_edge(Edge(temperature, environmental_condition, EdgeType.DIRECTED)) \
        .add_edge(Edge(temperature, disinfectant_residual, EdgeType.DIRECTED)) \
        .add_edge(Edge(water_velocity, disinfectant_residual, EdgeType.DIRECTED)) \
        .add_edge(Edge(temperature, dissolved_oxygen, EdgeType.DIRECTED)) \
        .add_edge(Edge(disinfectant_residual, oxidation_potential, EdgeType.DIRECTED)) \
        .add_edge(Edge(dissolved_oxygen, oxidation_potential, EdgeType.DIRECTED)) \
        .add_edge(Edge(water_aggressiveness, water_corrosion, EdgeType.DIRECTED)) \
        .add_edge(Edge(oxidation_potential, water_corrosion, EdgeType.DIRECTED)) \
        .add_edge(Edge(disinfectant_residual, bacteria_growth, EdgeType.DIRECTED)) \
        .add_edge(Edge(disinfectant_residual, biofilm, EdgeType.DIRECTED)) \
        .add_edge(Edge(environmental_condition, bacteria_growth, EdgeType.DIRECTED)) \
        .add_edge(Edge(biofilm, microbial_corrosion, EdgeType.DIRECTED)) \
        .add_edge(Edge(microbial_corrosion, corrosion, EdgeType.DIRECTED)) \
        .add_edge(Edge(water_corrosion, corrosion, EdgeType.DIRECTED)) \
        .add_edge(Edge(corrosion, internal_deterioration, EdgeType.DIRECTED)) \
        .add_edge(Edge(pipe_material, internal_deterioration, EdgeType.DIRECTED)) \
        .add_edge(Edge(internal_deterioration, failures_risk, EdgeType.DIRECTED)) \
        .add_edge(Edge(water_quality_risk, failures_risk, EdgeType.DIRECTED)) \
        .add_edge(Edge(bacteria_growth, water_quality_risk, EdgeType.DIRECTED)) \
        .add_edge(Edge(biofilm, material_accumulation, EdgeType.DIRECTED)) \
        .add_edge(Edge(alkalinity, water_aggressiveness, EdgeType.DIRECTED)) \

    join_tree = InferenceController.apply(bbn)

    start = time.time()
    input_dict = Dictionary_Quality
    """
    Implementing the model
    """
    col_Names = ['ID', 'Node1', 'Node2', 'Length', 'Diameter', 'Roughness', 'MinorLoss', 'Status', 'Node', 'X-Coord',
                 'Y-Coord', 'Pipe Pressure', 'State Pressure', 'Pipe Material', 'Pipe Velocity', 'State Velocity']

    df = pd.read_excel(Dataframe_Network, names=col_Names)
    list_expected_failure = []
    count = 0

    # Calculate the Expected Failure Risk for each pipe
    for index, row in df.iterrows():
        # State pressure
        input_dict['water pressure'] = row['State Pressure']
        # State velocity
        input_dict['water velocity'] = row['State Velocity']
        # Pipe Material
        input_dict['pipe material'] = row['Pipe Material']
        # # Calculating the expected risk for each pipe
        distribution = functions.get_pipe_failure_risk(input_dict, failures_risk, join_tree)
        expected_failure_risk = functions.get_scale('failure risk', join_tree)
        list_expected_failure.append(expected_failure_risk)
        count += 1
        print(count)
    df['Expected Failure'] = list_expected_failure


    # Export to Excel File
    df.to_excel('Dataframe_Network_Risk.xlsx', index=False)

    end = time.time()
    print(end - start)
    return

