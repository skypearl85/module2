import plotly.graph_objs as go
import seaborn as sns

dfTips = sns.load_dataset('tips')

listGoFunc = {
    'bar': go.Bar,
    'violin': go.Violin,
    'box': go.Box
}

def getPlot(typeCategory, xCategory):
    return [
        listGoFunc[typeCategory]
        (
            x = dfTips[xCategory],
            y = dfTips['tip'],
            text = dfTips['day'],
            opacity = 0.7,
            name = 'Tip',
            marker = dict(color='blue'),
            legendgroup = 'Tip'
        ),
        listGoFunc[typeCategory](
            x = dfTips[xCategory],
            y = dfTips['total_bill'],
            text = dfTips['day'],
            opacity = 0.7,
            name = 'Total Bill',
            marker = dict(color='orange'),
            legendgroup = 'Total Bill'
        )
    ]
    