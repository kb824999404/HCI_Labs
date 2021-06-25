import dash_echarts
import dash
import dash_html_components as html
from dash_html_components.H1 import H1
from numpy.core.shape_base import stack
import dash_core_components as dcc
import pandas as pd
import numpy as np
import plotly.graph_objs as go

app = dash.Dash("Google Play Store Dashborad")

layouts = []

layout_1 = []
panel_style = {
    "width": '95vw',
    "height": '80vh',
    "margin": "auto",
    "margin-top": "20px",
    "margin-bottom": "10px",
    "padding": "10px 0",
    "box-shadow": "0 2px 4px 3px rgba(0,0,0,0.2)",
}


def showCategoryCount(category_count):
    categories = []
    for i, item in enumerate(list(category_count.keys())[:10]):
        item = item
        if i % 2 == 0:
            categories.append(item)
        else:
            categories.append("\n" + item)
    counts = list(category_count.values)
    option1 = {
        "title": {
            "text": "Numbers of top10 category"
        },
        "tooltip": {
            "trigger": 'axis',
            "axisPointer": {
                "type": 'shadow'
            }
        },
        "xAxis": {
            "type": 'category',
            "data": categories,
            "axisLabel": {
                "interval": 0
            },
            "splitline": {
                "show": False
            }
        },
        "yAxis": {
            "type": 'value',
        },
        "series": [{
            "name": "Number",
            "data": counts,
            "type": 'bar',
            "label": {
                "show": True,
                "position": "top",
            }
        }]
    }
    category_count_bar = dash_echarts.DashECharts(
        option=option1, id='category_count_bar',
        # style=panel_style
        style = {'width': '38%', "height": '70vh', 'display': 'inline-block',
                 'margin': '20px',"padding": "10px 0","box-shadow": "0 2px 4px 3px rgba(0,0,0,0.2)"}
    )
    option2 = {
        "title": {
            "text": "Numbers of each category"
        },
        "tooltip": {
            "trigger": 'item',
        },
        "legend": {
            "type": 'scroll',
            "orient": 'vertical',
            "left": 0,
            "top": 40,
        },
        "series": [{
            "name": "Number",
            "type": 'pie',
            "radius": [50, 100],
            "center": ['50%', '50%'],
            "roseType": 'area',
            "itemStyle": {
                "borderRadius": 1
            },
            "data": [
                {"value": v, "name": key} for (key, v) in category_count.items()
            ]
        }]
    }
    category_count_pie = dash_echarts.DashECharts(
        option=option2, id='category_count_pie',
        # style=panel_style
        style = {'width': '55%', "height": '70vh', 'display': 'inline-block',
                 'margin': '20px', "padding": "10px 0", "box-shadow": "0 2px 4px 3px rgba(0,0,0,0.2)"}
    )
    layouts.append(category_count_pie)
    layouts.append(category_count_bar)

def showCategoryUpdate():
    series = []
    for category, data in category_count_update.items():
        series.append(
            {
                "name": category,
                "data": data,
                "stack": "Number",
                "type": 'line',
            }
        )
    option = {
        "title": {
            "text": "Numbers of updated app each year",
        },
        "tooltip": {
            "trigger": 'axis',
            "axisPointer": {
                "type": 'shadow'
            }
        },
        "legend": {
            "data": list(category_count_update.keys()),
            "width": "45%",
        },
        "xAxis": {
            "type": 'category',
            "data": all_time,
            "axisLabel": {
                "interval": 0
            },
            "axisTick": {
                "alignWithLabel": True
            },
            "splitline": {
                "show": False
            }
        },
        "yAxis": {
            "type": 'value',
        },
        "series": series,
    }
    category_update_line = dash_echarts.DashECharts(
        option=option, id='number_update',
        # style=panel_style
        style={'width': '96%', "height": '70vh', 'display': 'inline-block',
               'margin': '20px',"padding": "10px 0", "box-shadow": "0 2px 4px 3px rgba(0,0,0,0.2)"}
    )
    layouts.append(category_update_line)

@app.callback(
    dash.dependencies.Output('dot', 'figure'),
    [dash.dependencies.Input('x', 'value'),])
def dot_figure(x):
    categories = []
    min = []
    max = []
    mean = []
    for i, item in enumerate(category_install_mean):
        item = item[0][:6]
        if i % 2 == 0:
            categories.append(item)
        else:
            categories.append("\n" + item)
    if x == 'Ratings':
        mean = [item[1] for item in category_rating_mean]
        max = [item[1] for item in category_rating_max]
        min = [item[1] for item in category_rating_min]
    elif x == 'Installs':
        mean = [item[1] for item in category_install_mean]
        max = [item[1] for item in category_install_max]
        min = [item[1] for item in category_install_min]
    elif x == 'Reviews':
        mean = [item[1] for item in category_reviews_mean]
        max = [item[1] for item in category_reviews_max]
        min = [item[1] for item in category_reviews_min]

    return {
        'data': [
            go.Bar(x=categories, y=min, name="Min", marker=dict(color='#8ebad9')),
            go.Bar(x=categories, y=mean, name="Mean", marker=dict(color='#ffbe86')),
            go.Bar(x=categories, y=max, name="Max", marker=dict(color='#95cf95')),
        ],
        'layout': go.Layout(title=x, barmode='group', height=400, )
    }

if __name__ == '__main__':

    df = pd.read_csv('lab3-datasets/google-play-store-apps/googleplaystore.csv')

    category_count = df['Category'].value_counts()

    # 筛选数量大于10的类别
    category_count = category_count[category_count.values > 10]

    showCategoryCount(category_count)
    df_filter = df[df['Category'].isin(category_count.index)]

    data = df_filter.to_dict(orient='records')

    # 筛选有评分的APP
    data_has_rating = [item for item in data if not np.isnan(float(item["Rating"]))]

    # 统计每个类别的评分
    category_rating = {}
    for item in data_has_rating:
        category = item['Category']
        if category not in category_rating:
            category_rating[category] = [float(item['Rating'])]
        else:
            category_rating[category].append(float(item['Rating']))

    category_rating_mean = [[key, np.mean(item)] for (key, item) in category_rating.items()]
    category_rating_max = [[key, np.max(item)] for (key, item) in category_rating.items()]
    category_rating_min = [[key, np.min(item)] for (key, item) in category_rating.items()]

    # 统计每个类别的下载量
    category_install = {}
    for item in data:
        category = item['Category']
        if item['Installs'] == "Free":
            installs = 0
        else:
            if item['Installs'][-1] == "+":
                installs = int(item['Installs'][:-1].replace(',', ''))
            else:
                installs = int(item['Installs'].replace(',', ''))
        if category not in category_install:
            category_install[category] = [installs]
        else:
            category_install[category].append(installs)

    category_install_mean = [[key, int(np.mean(item))] for (key, item) in category_install.items()]
    category_install_max = [[key, int(np.max(item))] for (key, item) in category_install.items()]
    category_install_min = [[key, int(np.min(item))] for (key, item) in category_install.items()]

    # 统计每个类别的评论数
    category_review = {}
    for item in data:
        category = item['Category']
        reviews = int(item['Reviews'])
        if category not in category_review:
            category_review[category] = [reviews]
        else:
            category_review[category].append(reviews)

    category_reviews_mean = [[key, int(np.mean(item))] for (key, item) in category_review.items()]
    category_reviews_max = [[key, int(np.max(item))] for (key, item) in category_review.items()]
    category_reviews_min = [[key, int(np.min(item))] for (key, item) in category_review.items()]


    # 统计每个类别的更新时间数量
    all_time = []
    category_count_update = {}
    for item in data:
        category = item['Category']
        if category not in list(category_count[:10].index):
            continue
        update_time = item['Last Updated'][-2:]
        if update_time not in all_time:
            all_time.append(update_time)
        if category not in category_count_update:
            category_count_update[category] = {update_time: 1}
        else:
            if update_time in category_count_update[category]:
                category_count_update[category][update_time] += 1
            else:
                category_count_update[category][update_time] = 1

    all_time.sort()
    for category, data in category_count_update.items():
        for t in all_time:
            if t not in data:
                category_count_update[category][t] = 0
        category_count_update[category] = [category_count_update[category][t] for t in all_time]

    showCategoryUpdate()

    app.layout = html.Div(
        [
            html.H1("Google Play Store Apps",
                    style={
                        "text-align": "center",
                        "margin": 0,
                        "padding": "10px 0"
                    }),
            html.Div([
                dcc.Tabs(id='x', value='Ratings', children=[
                    dcc.Tab(label='Ratings', value='Ratings'),
                    dcc.Tab(label='Installs', value='Installs'),
                    dcc.Tab(label='Reviews', value='Reviews'),
                ]),
            ], style={'width': '96%', 'margin': '20px', "padding": "10px 0",
                      'display': 'inline-block'}),
            html.Div([dcc.Graph(id='dot')],
                     style={'width': '96%', 'margin': '20px',"padding": "10px 0",
                            "box-shadow": "0 2px 4px 3px rgba(0,0,0,0.2)"}
                     ),

            # html.Div(layout_1),
            html.Div(layouts)
        ]
    )

    app.run_server()
