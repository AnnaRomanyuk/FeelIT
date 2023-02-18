import dash
from dash import dcc
from dash import html
import yaml

compOrgs=[]
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

with open("data.yaml", "r", encoding='utf-8') as f:
                data = yaml.safe_load(f)
                compOrgs=data['Архангельская область']
app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Заготовка под дашборд',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='График соотношения организаторов и волонтеров в Архангельской области', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'values': [compOrgs[0]["Организаторы"],compOrgs[1]["Волонтёры"]],  'type': 'pie', 'labels': ['организаторы','волонтеры']},
                #{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)