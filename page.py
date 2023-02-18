import dash
import pandas as pd
import plotly.express as px
import yaml
from dash import dcc, html
from dash.dependencies import Input, Output, State


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Читаем файл и записываем все данные оттуда
with open("data.yaml", "r", encoding='utf-8') as f:
    data = yaml.safe_load(f)

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
    html.Div(style={'display': 'inline-block'}, children=[dcc.Dropdown(id='region', clearable=False,
                                                                       value="Чеченская Республика",
                                                                       options=[{'label': x, 'value': x} for x in
                                                                                data]),
                                                          html.Div(id="output-dobro-div", children=[]), html.Div(id="output-excel-div", children=[])]
             ),

])


@app.callback(Output(component_id="output-dobro-div", component_property="children"),
              Input(component_id="region", component_property="value"),
              )  # Берет параметр value у компонентов с id region и передает результат последующей функции в компонент с id output-div
def buildDobroGraphs(chosenRegion):
    """
    Входной параметр передается через value у объекта с  id region
    Функция возвращает разметку страницы, которая содержит подгружаемые динамически данные 

    """
    liList = []
    # Берет все строки с регионом
    p_comp = data[chosenRegion]
    for x in p_comp:
        print(str(x))
        liList.append(html.Li(children=html.A(str(x))))
    p_data = [p_comp[0]["Организаторы"],
              p_comp[1]["Волонтёры"]]
    fig_comp = px.pie(values=p_data, names=[
                      'организаторы', 'волонтеры'])  # График пирог
    bar_comp = px.bar(x=['организаторы',
                      'волонтеры'], y=p_data)  # График столбцы
    return html.Div(children=[
        dcc.Graph(figure=fig_comp)],
        style={
            'display': 'inline-block'}), html.Div(
        children=[dcc.Graph(figure=bar_comp)], style={'display': 'inline-block'}), html.Ul(
        style={'color': colors['text']}, children=html.Li(liList))


@app.callback(Output(component_id="output-excel-div", component_property="children"),
              Input(component_id="region", component_property="value"),
              )
def BuildForm1Graphs(chosenRegion):
    # TODO: Обработать данные из csv файла
    return html.A(f"Здесь описать вывод данных по файлу excel для {chosenRegion}", style={'color': colors['text']},)


if __name__ == '__main__':
    app.run_server(debug=1)
