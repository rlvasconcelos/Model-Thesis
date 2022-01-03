import pandas as pd

def Waterquality(quality_parameters):
    df_quality = pd.read_excel(quality_parameters)
    df_quality = df_quality.set_index(['Parameter'])
    """
    Output of this code is a dictionary of node's states
    """

    dic_parameters = {}

    """
    Water pH:
    State    | Value
    Low         pH =< 7
    Medium     7 < pH =< 8     
    High         pH > 8         
    """

    value_ph = df_quality.loc["pH", 'Result']
    if value_ph <= 7:
        state_ph = 'low'
    elif 7 < value_ph <= 8:
        state_ph = 'medium'
    else:
        state_ph = 'high'
    dic_parameters['pH'] = state_ph

    """
    Turbidity:
    State    | Value
    Low         Turb =< 1
    Medium     1 < Turb =< 5     
    High         Turb > 5         
    """

    value_turbidity = df_quality.loc["Turbidity", 'Result']
    if value_turbidity <= 1:
        state_turbidity = 'low'
    elif 1 < value_turbidity <= 5:
        state_turbidity = 'medium'
    else:
        state_turbidity = 'high'
    dic_parameters['turbidity'] = state_turbidity

    """
    Dissolved Oxygen:
    State    | Value
    Low         DO =< 5
    Medium     5 < DO =< 6     
    High         DO > 6
    
    Note: parameter in quality report is called  Oxidisability        
    """

    value_do = df_quality.loc["Oxidisability", 'Result']
    if value_do <= 5:
        state_do = 'low'
    elif 5 < value_do <= 6:
        state_do = 'medium'
    else:
        state_do = 'high'
    dic_parameters['dissolved oxygen'] = state_do

    """
    Total dissolved solids:
    State    | Value
    Low         TDS =< 300
    Medium     300 < TDS =< 600     
    High         TDS > 600
    
    Note: Quality Report gives the Electrical Conductivity (25°C),        
    According to literature TDS = k . Electrical Conductivity,
    where k is usually assumed 0.67
    """
    # EC to TDS conversion
    value_electrical_conductivity = df_quality.loc["Electrical Conductivity (25°C)", 'Result']
    value_tds = 0.67 * value_electrical_conductivity
    if value_tds <= 300:
        state_tds = 'low'
    elif 300 < value_tds <= 600:
        state_tds = 'medium'
    else:
        state_tds = 'high'
    dic_parameters['total dissolved solids'] = state_tds

    """
    Hardness:
    State    | Value
    Low         Hard =< 60
    Medium     60 < Hard =< 180     
    High         Hard > 180
    
    Conversion from degree German hardness to ppm 
    1 °dH = 17.8 mg l-1 CaCO3 (ppm)
    """
    # °dH to ppm conversion
    value_dh = df_quality.loc["Carbonate hardness", 'Result']
    value_hardness = 17.8 * value_dh
    if value_hardness <= 60:
        state_hardness = 'low'
    elif 60 < value_hardness <= 180:
        state_hardness = 'medium'
    else:
        state_hardness = 'high'
    dic_parameters['hardness'] = state_hardness


    """
    Alkalinity:
    State    | Value
    Low         Alk =< 150
    Medium     150 < Alk =< 200     
    High         Alk > 200
    
    Conversion from acid capacity to alkalinity (CaCo3) 
    Vide Table
    """
    # Acid Capacity to mg/l CaCO3 conversion
    value_acid_capacity = df_quality.loc["Acid capacity up to pH 4.3", 'Result']
    value_alkalinity = 50.4 * value_acid_capacity
    if value_alkalinity <= 60:
        state_alkalinity = 'low'
    elif 60 < value_alkalinity <= 180:
        state_alkalinity = 'medium'
    else:
        state_alkalinity = 'high'
    dic_parameters['alkalinity'] = state_alkalinity

    """
    Disinfectant Residual:
    State    | Value
    Low         DR =< .30
    Medium     .30 < DR =< .60     
    High         DR > .60
    
    Since the Trihalomethanes parameter is given, the DR concentration is roughly calculated 
    with the β, regression coefficient from a multiple linear regression analysis from 
    \cite{rodrigues2007factorial}
    regression_coefficient =0.261
    """
    #Defining the function
    thm = df_quality.loc["Trihalomethanes", 'Result']
    regression_coefficient = 0.261
    value_dr = thm / regression_coefficient
    if value_dr <= .30:
        state_dr = 'low'
    elif .3 < value_dr <= .60:
        state_dr = 'medium'
    else:
        state_dr = 'high'
    dic_parameters['disinfectant residual'] = state_dr
    return dic_parameters

