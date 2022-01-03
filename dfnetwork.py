from epynet import Network
from epynet import Node, Junction, Reservoir, Tank, Pipe
import pandas as pd


def DataframeNetwork(Network, initial_dataframe, file_name):
    """
    @param Network: .inp file
    @param initial_dataframe: Initial Dataframe, see README.md
    @param file_name: string with desired name of updated Data Frame (with .xlsx)
    @note: if the argument 'file_name' is equal to name of 'initial_dataframe',
    it will overwrite the initial dataframe.
    @return: updated df
    """

    network = Network
    df = initial_dataframe
    # solve network
    network.solve()

    """
    Get pressure of the pipe
    """
    pipe_pressure = []
    for pipe in df['ID']:
        pipe = str(pipe)
        upstream_pressure = network.pipes[pipe].upstream_node.pressure
        downstream_pressure = network.pipes[pipe].downstream_node.pressure
        pressure = (upstream_pressure + downstream_pressure) * 0.5
        pipe_pressure.append(pressure)
    df['Pipe Pressure'] = pipe_pressure
    # Creating  Water Pressure State Column, and Pipe Material
    list_state_pressure = []
    for pressure in df['Pipe Pressure']:
        if pressure <= 35:
            state_pressure = 'low'
        elif 35 < pressure <= 70:
            state_pressure = 'medium'
        else:
            state_pressure = 'high'
        list_state_pressure.append(state_pressure)
    df['State Pressure'] = list_state_pressure

    """
    Get the pipe material
    """
    pipe_material = []
    for roughness in df['Roughness']:
        if roughness <= 125:
            material = 'metallic'
        elif roughness == 145:
            material = 'cement'
        else:
            material = 'polymeric'
        pipe_material.append(material)
    df['Pipe Material'] = pipe_material

    """
    # Get the velocities of the system
    # """
    pipe_velocity = []
    velocity = network.pipes.velocity
    for i in velocity:
        pipe_velocity.append(i)
    df['Pipe Velocity'] = pipe_velocity

    # Creating Water Velocity State Column, Water Pressure and Pipe Material
    list_state_velocity = []
    for velocity in df['Pipe Velocity']:
        if velocity <= 0.2:
            state_velocity = 'low'
        elif 0.2 < velocity <= 1:
            state_velocity = 'medium'
        else:
            state_velocity = 'high'
        list_state_velocity.append(state_velocity)
    df['State Velocity'] = list_state_velocity

    # Export to Excel File
    df.to_excel(file_name, index=False)

    return
