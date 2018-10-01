import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from categoryplot import dfTips, getPlot
from histogram import getHistogram

app = dash.Dash()

app.title = 'Majestic Dash Plotly'
color_set = {
    'sex': ['#ff3fd8','#4290ff'],
    'smoker': ['#32fc7c','#ed2828'],
    'time': ['#0059a3','#f2e200'],
    'day': ['#ff8800','#ddff00','#3de800','#00c9ed']
}

colorHist = {
    'normal': '#ffd820',
    'notNormal': '#4d4d4d'
}

operatorFunction = {
    'count': len,
    'sum': sum,
    'mean': np.mean,
    'std': np.std
}

disabledEstimator = {
    'count': True,
    'sum': False,
    'mean': False,
    'std': False
}

# generate table`
def generate_table(dataframe, max_rows=10):
    return html.Table(
        #head
        [html.Tr([html.Th(col, className = 'table_dataset') for col in dataframe.columns])] + 
        #body
        [html.Tr([
            html.Td(dataframe.iloc[i][col], className = 'table_dataset') for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))],
        className = 'table_dataset'
    )

# change layout
app.layout = html.Div(children=[
    #default tab value = tab-1
    dcc.Tabs(id='tabs', value='tab-1',children=[
        dcc.Tab(label='Tips Data Set', value='tab-1',children=[
            html.Div([
                html.H1(
                    children = 'Tips Data Set',
                    className = 'h1FirstTab'
                ),
                html.Div([
                    dcc.RangeSlider(
                        min=min(dfTips['total_bill']),
                        max=max(dfTips['total_bill']),
                        step=1,
                        value=[min(dfTips['total_bill']), max(dfTips['total_bill'])]
                    ),
                ]),
                html.Div([
                    html.P('Minimum bill '),
                    html.P('Total row :' + str(len(dfTips))),
                    dcc.Graph(
                        id='tableTips',
                        figure = {
                            'data':[
                                go.Table(
                                    header=dict(
                                        values=dfTips.columns,
                                        font=dict(size=18),
                                        height=30,
                                        fill = dict(color='#46a3cb')
                                    ),
                                    cells=dict(
                                        values=[dfTips[col] for col in dfTips.columns],
                                        height=30,
                                        font=dict(size=16),
                                        fill = dict(color='#e5e8ed')
                                    )
                                )
                            ],
                            'layout': go.Layout(height=600, margin={'t':10})
                        }
                    )
                ])
            ])
        ]),
        dcc.Tab(label='Scatter Plot', value='tab-2',children=[
            html.Div([
                html.H1(
                    children = 'Scatter Plot Tips Data Set',
                    className = 'h1FirstTab'
                ),
                 html.Table(
                    html.Tr([
                        html.Td([
                            html.P('Hue: ')
                        ]),
                        html.Td([
                            dcc.Dropdown(
                                id='ddl-hue-category',
                                options=[{'label': 'Sex', 'value': 'sex'},
                                    {'label': 'Day', 'value': 'day'},
                                    {'label': 'Time', 'value': 'time'},
                                    {'label': 'Smoker', 'value': 'smoker'}
                                ],
                                value = 'sex'
                            )
                        ])
                    ]),
                    style = {
                        'width':'100%'
                    }
                 ),
                html.Div(html.P('', id='totalData')),
                dcc.Graph(
                    id = 'scatterPlot',
                    figure = {} 
                ),
                dcc.Slider(
                    id='sizeScatterSlider',
                    min=dfTips['size'].min(),
                    max=dfTips['size'].max(),
                    value=dfTips['size'],
                    step=None,
                    marks={str(size): str(size) for size in dfTips['size'].unique()}
                )
            ])
        ]),
        dcc.Tab(label='Categorical Plot', value='tab-3', children=[
            html.Div([
                html.H1(
                    children = 'Categorical Plot Tips Data Set',
                    className = 'h1FirstTab'
                ),
                html.Table(
                    html.Tr([
                        html.Td([
                            html.P('Type: '),
                            dcc.Dropdown(
                                id='ddl-plot-category',
                                options=[{'label': 'Bar', 'value': 'bar'},
                                    {'label': 'Violin', 'value': 'violin'},
                                    {'label': 'Box', 'value': 'box'}
                                ],
                                value = 'bar'
                            )
                        ]),
                        html.Td([
                            html.P('X axis: '),
                            dcc.Dropdown(
                                id='ddl-x-category',
                                options=[{'label': 'Smoker', 'value': 'smoker'},
                                    {'label': 'Sex', 'value': 'sex'},
                                    {'label': 'Day', 'value': 'day'},
                                    {'label': 'Time', 'value': 'time'}
                                ],
                                value = 'sex'
                            )
                        ])
                    ]),
                    style = {
                        'width':'900px'
                    }
                ),
                dcc.Graph(
                    id = 'categoricalPlot',
                    figure = {}
                )
            ])
        ]),
        dcc.Tab(label='Pie Chart', value='tab-4',children=[
            html.Div([
                html.H1(
                    children = 'Pie Chart Tips Data Set',
                    className = 'h1FirstTab'
                ),
                html.Table(
                    html.Tr([
                        html.Td([
                            html.P('Type: '),
                            dcc.Dropdown(
                                id='ddl-pie-category',
                                options=[{'label': 'Smoker', 'value': 'smoker'},
                                    {'label': 'Sex', 'value': 'sex'},
                                    {'label': 'Day', 'value': 'day'},
                                    {'label': 'Time', 'value': 'time'}
                                ],
                                value = 'sex'
                            )
                        ]),
                        html.Td([
                            html.P('Estimator: '),
                            dcc.Dropdown(
                                id='ddl-estimator',
                                options=[{'label': 'Count', 'value': 'count'},
                                    {'label': 'Sum', 'value': 'sum'},
                                    {'label': 'Mean', 'value': 'mean'},
                                    {'label': 'Std', 'value': 'std'}
                                ],
                                value = 'count'
                            )
                        ]),
                        html.Td([
                            html.P('Column: '),
                            dcc.Dropdown(
                                id='ddl-column-pie',
                                options=[{'label': 'Total bill', 'value': 'total_bill'},
                                    {'label': 'Tip', 'value': 'tip'}
                                ],
                                value = 'total_bill',
                                disabled = False
                            )
                        ])
                    ]),
                    style = {
                    'width':'100%'
                }),
                html.Div(html.P('', id='totalPie')),
                dcc.Graph(
                    id='piePlot',
                    figure={'data':[]}
                )
            ])
        ]),
        dcc.Tab(label='Histogram', value='tab-5',children=[
            html.Div([
                html.H1(
                    children = 'Histogram Tips Data Set',
                    className = 'h1FirstTab'
                ),
                html.Table(
                    html.Tr([
                        html.Td([
                            html.P('Column: '),
                            dcc.Dropdown(
                                id='ddl-histogram-category',
                                options=[{'label': 'Tip', 'value': 'tip'},
                                    {'label': 'Total bill', 'value': 'total_bill'}
                                ],
                                value = 'tip'
                            )
                        ]),
                        html.Td([
                            html.P('X axis: '),
                            dcc.Dropdown(
                                id='ddl-histogram-x',
                                options=[{'label': 'Day', 'value': 'day'},
                                    {'label': 'Sex', 'value': 'sex'},
                                    {'label': 'Smoker', 'value': 'smoker'},
                                    {'label': 'Time', 'value': 'time'}
                                ],
                                value = 'day'
                            )
                        ])
                    ]),
                    style = {
                        'width':'100%'
                    }
                ),
                html.Div('',id='histogramDiv')
            ])
        ])
    ],
    # parent_style = {
    #     'maxWidth': '1000px',
    #     'margin': '0 auto'
    # }
    style = {
        'fontFamily': 'system-ui'
    },
    content_style = {
        'fontFamily': 'Arial',
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'padding': '44px'
    })
],
#same with parent_style
style = {
    'maxWidth': '1000px',
    'margin': '0 auto'
})

@app.callback(
    Output('categoricalPlot', 'figure'),
    [Input('ddl-plot-category', 'value'),
    Input('ddl-x-category', 'value')]
)
def update_category_graph(ddlcateogrytype, ddlxtype):
    return {
        'data':getPlot(ddlcateogrytype, ddlxtype),
        'layout':
            go.Layout(
                xaxis = {'title': ddlxtype.capitalize()},
                yaxis = {'title': 'US$'},
                margin = {'l': 40, 'b':40, 't':10, 'r':10},
                boxmode = 'group', violinmode = 'group',
                #determine the position of legend (x,y)
                # legend = {'x':0, 'y':1},
                hovermode = 'closest'
            )
    }

@app.callback(
    Output('totalData', 'children'),
    [Input('sizeScatterSlider', 'value')]
)
def update_scatter_data(size):
    return 'Total data: ' + str(len(dfTips[dfTips['size'] == size]))

@app.callback(
    Output('scatterPlot', 'figure'),
    [Input('ddl-hue-category', 'value'),
    Input('sizeScatterSlider', 'value')]
)
def update_hue_graph(ddlhuetype, sliderSize):
    return {
        'data':[
            go.Scatter(
                x = dfTips[(dfTips[ddlhuetype] == col) & (dfTips['size'] == sliderSize)]['total_bill'],
                y = dfTips[(dfTips[ddlhuetype] == col) & (dfTips['size'] == sliderSize)]['tip'],
                mode = 'markers',
                marker = dict(color=color_set[ddlhuetype][i], size=10, line={'width':0.5, 'color':'white'}), name=col
            ) for col,i in zip(dfTips[ddlhuetype].unique(),range(len(dfTips[ddlhuetype].unique())))
        ],
        'layout':
            go.Layout(
                xaxis = {'title': 'Total bill'},
                yaxis = {'title': 'Tip'},
                margin = {'l': 40, 'b': 40, 't': 10, 'r': 10},
                hovermode = 'closest'
            )
    }

@app.callback(
    Output('ddl-column-pie', 'disabled'),
    [Input('ddl-estimator', 'value')]
)
def disabled_ddl(estimator):
    return disabledEstimator[estimator]
    
@app.callback(
    Output('piePlot', 'figure'),
    [Input('ddl-pie-category', 'value'),
    Input('ddl-estimator', 'value'),
    Input('ddl-column-pie', 'value')]
)
def update_pie_chart(ddlpiecategory, estimator, column):
    return {
        'data': [
            go.Pie(
                labels=list(dfTips[ddlpiecategory].unique()),
                values=[operatorFunction[estimator](dfTips[dfTips[ddlpiecategory] == s][column]) for s in dfTips[ddlpiecategory].unique()],
                textinfo='value',
                hoverinfo='label+percent',
                marker=dict(colors=color_set[ddlpiecategory], line=dict(color='white', width=2))
            )
        ],
        'layout':
            go.Layout(
                margin={'l':40, 'b':40, 't':10, 'r':10},
                legend={'x':0, 'y':1}
            )
    }

@app.callback(
    Output('histogramDiv', 'children'),
    [Input('ddl-histogram-category', 'value'),
    Input('ddl-histogram-x', 'value')]
)

def update_histogram(ddlhist, ddlx):
    return getHistogram(ddlhist,ddlx)

if __name__ == '__main__':
    #debug True, automatic refresh after update
    app.run_server(debug=True, port=8080)