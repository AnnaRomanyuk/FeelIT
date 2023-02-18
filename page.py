import dash
from dash import dcc
from dash import html
import yaml
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
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
    
    html.Div(children='График соотношения организаторов и волонтеров по регионам', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Div(style={'display': 'inline-block'},children=[ dcc.Dropdown(id='region', clearable=False,
                     value="Чеченская Республика",
                     options=[{'label': x, 'value': x} for x in
                              data]),
    html.Div(id="output-div",children=[]),]
    ),
    # dcc.Graph(
    #     style={'display': 'inline-block','width':'50%'},
    #     id='dobro-1',
    #     figure={
    #         'data': [
    #             {'values': [compOrgs[0]["Организаторы"],compOrgs[1]["Волонтёры"]],  'type': 'pie', 'labels': ['организаторы','волонтеры']},
    #             #{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    #         ],
    #         'layout': {
    #             'plot_bgcolor': colors['background'],
    #             'paper_bgcolor': colors['background'],
    #             'font': {
    #                 'color': colors['text']
    #             }
    #         }
    #     }
    # )
])
@app.callback(Output(component_id="output-div", component_property="children"),
              Input(component_id="region", component_property="value"),
)
def buildGraphs(chosenRegion):
    liList=[]
    p_comp=data[chosenRegion]
    for x in p_comp:
          print(str(x))
          liList.append(html.Li(children=html.A(str(x))))  
    p_data=[p_comp[0]["Организаторы"],p_comp[1]["Волонтёры"]]
    fig_comp =px.pie(values=p_data,names=['организаторы','волонтеры'])
    bar_comp=px.bar(x=['организаторы','волонтеры'],y=p_data)
    return html.Div(children=[dcc.Graph(figure=fig_comp) ],style={'display': 'inline-block'}),html.Div(children=[dcc.Graph(figure=bar_comp) ],style={'display': 'inline-block'}),html.Ul(style={'color': colors['text']},children=html.Li(liList))    
if __name__ == '__main__':
    app.run_server(debug=1)