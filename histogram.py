import plotly.graph_objs as go
import numpy as np
import dash_html_components as html
import dash_core_components as dcc
from plotly import tools
from categoryplot import dfTips

def getHistogram(ddlhist, ddlx):
    color_set = [ '#d43a70', '#f0c09a']
    # looping = len(dfTips[ddlx].unique())
    looping = dfTips[ddlx].nunique()

    meanVal = np.mean(dfTips[ddlhist])
    minimum = meanVal - np.std(dfTips[ddlhist])
    maximum = meanVal + np.std(dfTips[ddlhist])

    rowCol = {
        'day': [2,2],
        'sex': [1,2],
        'smoker': [1,2],
        'time': [1,2]
    }
    row = 1
    col = 1
    
    fig = tools.make_subplots(rows=rowCol[ddlx][0],cols=rowCol[ddlx][1], subplot_titles=dfTips[ddlx].unique())
    # sL = True
    
    for i in range(looping):
        filteredDf = dfTips[dfTips[ddlx] == dfTips[ddlx].unique()[i]]
        traceNormal = go.Histogram(
            x=filteredDf[(filteredDf[ddlhist] >= minimum) & (filteredDf[ddlhist] <= maximum)][ddlhist],
            marker=dict(color=color_set[1]),
            name='Normal ' + str(dfTips[ddlx].unique()[i]),
            # legendgroup = 'Normal',
            # showlegend = sL
        )

        trace = go.Histogram(
            x=filteredDf[(filteredDf[ddlhist] < minimum) | (filteredDf[ddlhist] > maximum)][ddlhist],
            marker=dict(color=color_set[0]),
            name='Not normal ' + str(dfTips[ddlx].unique()[i]),
            # legendgroup = 'Not normal',
            # showlegend = sL
        )       

        # if(i >= 0) : sL = False
        fig['layout'].update(height = 600, width=900, title='Histogram ' + ddlhist.capitalize())
        fig['layout']['xaxis' + str(i+1)].update(title=ddlhist.capitalize())
        fig['layout']['yaxis' + str(i+1)].update(title='Total transaction')

        # x axis and y axis
        # [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
        # [ (2,1) x3,y3 ]  [ (2,2) x4,y4 ]

        fig.append_trace(traceNormal, row, col),
        fig.append_trace(trace, row, col)
      
        col += 1
        
        if(col > rowCol[ddlx][1]):
            row += 1
            col = 1
    
    return [
        html.H4('Min value: ' + str(np.mean(dfTips[ddlhist]) - np.std(dfTips[ddlhist]))),
        html.H4('Max value: ' + str(np.mean(dfTips[ddlhist]) + np.std(dfTips[ddlhist]))),
        dcc.Graph(
            id='histogram',
            figure= fig
    )]