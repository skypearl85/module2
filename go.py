'bar':  
    [go.Bar(
        x = dfTips[xCategory],
        y = dfTips['tip'],
        text = dfTips['day'],
        opacity = 0.7,
        name = 'Tip',
        marker = dict(color='blue'),
        legendgroup = 'Tip'
    ),
    go.Bar(
        x = dfTips[xCategory],
        y = dfTips['total_bill'],
        text = dfTips['day'],
        opacity = 0.7,
        #legend name
        name = 'Total Bill',
        marker = dict(color='orange'),
        # {'color': 'blue'}
        legendgroup = 'Total Bill'
    )],
'violin':
    [go.Violin(
        x = dfTips[xCategory],
        y = dfTips['tip'],
        text = dfTips['day'],
        opacity = 0.7,
        name = 'Tip',
        legendgroup = 'Tip',
        marker = dict(color='blue'),
        # meanline = {'visible': True},
        # showlegend = False
    ),
    go.Violin(
        x = dfTips[xCategory],
        y = dfTips['total_bill'],
        text = dfTips['day'],
        opacity = 0.7,
        name = 'Total Bill',
        legendgroup = 'Total bill',
        marker = dict(color='orange'),
        # meanline = {'visible': True},
        # showlegend = False
    )],
'box':
    [go.Box(
        x = dfTips[xCategory],
        y = dfTips['tip'],
        text = dfTips['day'],
        opacity = 0.7,
        name = 'Tip',
        legendgroup = 'Tip',
        marker = dict(color='blue'),
        # showlegend = False
    ),
    go.Box(
        x = dfTips[xCategory],
        y = dfTips['total_bill'],
        text = dfTips['day'],
        opacity = 0.7,
        name = 'Total Bill',
        legendgroup = 'TotalBill',
        marker = dict(color='orange'),
        # showlegend = False
    )] 