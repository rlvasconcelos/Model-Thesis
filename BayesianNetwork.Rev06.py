import numpy
import graphviz


bbn = graphviz.Digraph('bbn', node_attr={'shape':'oval', 'fontname': 'arial', 'fontsize': '35'})
bbn.attr(rankdir = 'TB')

""""""
"""
Water Quality Parameters
"""
bbn.node('Temp', 'Temperature')
bbn.node('Ph', 'pH')
bbn.node('Alk', 'Alkalinity')
bbn.node('Tur', 'Turbidity')
bbn.node('DIR', 'Disinfectant Residual')
bbn.node('DO', 'Dissolved Oxygen')
bbn.node('HD', 'Hardness')
bbn.node('TDS', 'Total Dissolved Solids')
bbn.node('Col', 'Color')
bbn.node('WV', 'Water Velocity')
bbn.node('WP', 'Water Pressure')
# bbn.node('DisBy', 'Disinfection By-Products')

"""
Biofilm
"""
bbn.node('Biof', 'Biofilm')
bbn.edge('DIR', 'Biof')
bbn.edge('DIR', 'BacGro')


"""
Operation
"""
bbn.node('HYC', 'Hydraulic Capacity')
bbn.edge('WV', 'HYC')
bbn.edge('WP', 'HYC')
bbn.edge('WV', 'DIR')
""" 
Water Acidity
"""
bbn.node('WAG', 'Water Aggressiveness')
bbn.edge('HD', 'InoMat')
bbn.edge('Ph', 'WAG')
bbn.edge('Alk', 'WAG')

"""
Temperature
"""
bbn.edge('Temp', 'DO')

"""
Water Corrosion
"""
bbn.edge('WAG', 'Cor')
# bbn.edge('DO', 'Cor')
bbn.node('Cor', 'Water Corrosion')


"""
Failure risk
"""
bbn.node('FR', 'Failure Risk')
bbn.edge('TDS', 'InoMat' )

"""
Pipe Scales
"""
bbn.node('PiS', 'Pipe Scales')
bbn.edge('WAG','PiS')

"""
Harbored Material
"""
bbn.node('ACC', 'Material Accumulation')
bbn.node('WQR', 'Water Quality Risk')
bbn.edge('Biof', 'ACC')
bbn.edge('PiS', 'ACC')
bbn.edge('ParDep', 'PiS')
bbn.edge('Temp','DIR')
bbn.edge('Col', 'WQR')
bbn.edge('WQR', 'FR')


bbn.edge('ACC', 'Col')
bbn.edge('Tur', 'Col')

"""
Oxidation Potential
"""
bbn.node('CorRis', 'Corrosion')
bbn.node('MicCor', 'Microbial Corrosion')
bbn.node('ParDep', 'Particle Deposition')
bbn.node('ParRes', 'Particle Resuspension')
bbn.node('BacGro', 'Bacteria Growth')
bbn.node('ORP', 'Oxidation Potential')
bbn.node('InoMat', 'Inorganic Matter')
bbn.edge('InoMat', 'PiS')


bbn.edge('DO', 'ORP')
bbn.edge('DIR', 'ORP')

bbn.edge('ORP', 'Cor')

bbn.edge('HYC', 'ParDep')
bbn.edge('HYC', 'ParRes')
bbn.edge('ParRes', 'Col')

bbn.node('EnvCon', 'Environmental Conditions')
bbn.edge('Temp', 'EnvCon')
bbn.edge('Ph', 'EnvCon')
bbn.edge('EnvCon', 'BacGro')
bbn.edge('BacGro', 'WQR')
bbn.edge('Cor', 'CorRis')
bbn.edge('Biof', 'MicCor')
bbn.edge('MicCor', 'CorRis')


"""
Pipe Material
"""
bbn.node('PipMat', 'Pipe Material')
bbn.node('IntDet', 'Internal Deterioration')
bbn.edge('PipMat', 'IntDet')
bbn.edge('CorRis', 'IntDet')
bbn.edge('IntDet', 'FR')

#Visualization
#
# bbn.view()

bbn.render('Graph/BBN_Rev.06')