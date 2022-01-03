from epynet import Network
import pandas as pd
import dfnetwork
import dfquality
import bbn_Network
import riskmap
import matplotlib.pyplot as plt

# Insert the network file (file.inp)
network = Network('Hanoi_Rev.01.inp')

"""
Initial Dataframe, according with the README file
"""
file_name = 'initial_df.xlsx'
initial_dataframe = pd.read_excel(file_name)
df = dfnetwork.DataframeNetwork(network, initial_dataframe, file_name)

"""
Water quality parameters
"""
#Insert the File path for the water quality parameters
quality_file_name = 'waterquality.xlsx'
input_dict = dfquality.Waterquality(quality_file_name)

"""
Applying the model
A new file name 'Dataframe_Network_Risk.xlsx' will be created.
"""
bbn_Network.ApplyModel(input_dict, 'initial_df.xlsx')

"""
Risk Map
"""
riskmap.RiskMap('Dataframe_Network_Risk.xlsx')

# Show the risk map
plt.show()
