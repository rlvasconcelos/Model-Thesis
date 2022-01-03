import matplotlib.pyplot as plt
import pandas as pd


def RiskMap(Dataframe_risk):
    df = pd.read_excel(Dataframe_risk)
    # Plot of the nodes
    x = df['X-Coord']
    y = df['Y-Coord']

    #Create a legend
    blue = 'b'
    yellow = 'y'
    red = 'r'

    # See loop
    list_label = []
    #Plot of the pipes
    for index, row in df.iterrows():
        Node1 = row['Node1']
        Node2 = row['Node2']
        #first get the risk and defined the color
        if row['Expected Failure'] <= 1.95:
            color = 'b-' #blue
            label = "EFR <= 1.95"
        elif 1.95 < row['Expected Failure'] <= 2.05:
            color = 'y-' #yellow
            label = "1.95 < EFR <= 2.05"
        else:
            color = 'r-' #red
            label = " 2.05 < EFR"
        # the X's coordinades of the pipe (automatized afterwards)
        x1, x2 = df.loc[df['Node'] == Node1]['X-Coord'].values[0], df.loc[df['Node'] == Node2]['X-Coord'].values[0]
        y1, y2 = df.loc[df['Node'] == Node1]['Y-Coord'].values[0], df.loc[df['Node'] == Node2]['Y-Coord'].values[0]
        if label not in list_label:
            plt.plot([x1, x2], [y1, y2], color, linewidth=3.5, label= label)
        else:
            plt.plot([x1, x2], [y1, y2], color, linewidth=3.5)
        # To avoid print labels each loop
        list_label.append(label)


    # Remove Axes labes
    plt.xticks([])
    plt.yticks([])


    plt.legend(loc="upper left")
    plt.scatter(x, y)
    plt.box(False)

    return

#
#
# for i in df['Node1']:
#     x1 = df.loc[df['Node'] == i]['X-Coord'].values[0]
#     y1 = df.loc[df['Node'] == i]['Y-Coord'].values[0]
# for i in df['Node2']:
#     x2 = df.loc[df['Node'] == i]['X-Coord'].values[0]
#     y2 = df.loc[df['Node'] == i]['Y-Coord'].values[0]
#
