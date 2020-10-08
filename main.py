import dash_bootstrap_components as dbc
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

#####
df_pop_london = pd.read_excel('./central_trend_2017_base.xlsx')
df_pop_london_10y_later = df_pop_london[['district', 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028,2029,2030]].query('district == "London"')
london_y1, london_y2, london_y3, london_y4, london_y5, london_y6, london_y7, london_y8, london_y9, london_y10,london_y11  = df_pop_london_10y_later[2020].sum(),df_pop_london_10y_later[2021].sum(), df_pop_london_10y_later[2022].sum(), df_pop_london_10y_later[2023].sum(), df_pop_london_10y_later[2024].sum(), df_pop_london_10y_later[2025].sum(), df_pop_london_10y_later[2026].sum(), df_pop_london_10y_later[2027].sum(), df_pop_london_10y_later[2028].sum(), df_pop_london_10y_later[2029].sum(),df_pop_london_10y_later[2030].sum()
arrLondonYear = np.arange(2020, 2031, 1)
arrLondonPop = [london_y1, london_y2, london_y3, london_y4, london_y5, london_y6, london_y7, london_y8, london_y9, london_y10,london_y11]
# London_10_year_fig = px.line( x=arrLondonYear, y=arrLondonPop,title='Population of London 10 years later')

#####

main = html.Div([
    # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div('Home page', style={
        'fontSize': '50px',
        'color': 'white',
        'textAlign': 'center'
    }),
    # link to another page
    html.Div([
        dcc.Link('Simple Chart', href='/simple-chart', style={
             'color': '#f5f5f5'
             }),
        dcc.Link('Data Analysis', href='/data-analysis', style={
            'color': '#f5f5f5'
        })
    ], style={
        'display': 'flex',
        'justify-content': 'space-evenly',

    }, className='mt-4'),

    # introduce tag
    html.Div([
        html.Div([
            html.Div('Introducing to project:', style={
                'fontSize': '25px',
                'fontWeight': 'bold',
            }),
            html.Div([
                html.Div( 'this is my project this is my project this is my project this is my project this is my project this is my project this is my project this is my project this is my project ',className='col-8'),
                html.Img(src='./assets/pop.jpg', className='col-4')

            ], className='row', style={ 'fontSize': '15px' })
        ])
    ], className='mt-5 bg-light intro'),
     html.Div([
        html.Div([
            html.Div('About my team:', style={
                'fontSize': '25px',
                'fontWeight': 'bold',
            }),
            html.Div([
                html.Img(src='./assets/team.jpg', className='col-4'),
                html.Div([
                html.Div('18081331 - Nguyễn Công Thành Đạt'),
                html.Div('18089811 - Mai kiên cường'),
                html.Div('18084791 - Trương Công Cường'),
                html.Div('18079251 - Đỗ Tùng Dương'),   
                ],className='col-4 team'),
                 html.Div( [
                html.Div('18092791 - Hoàng Hữu Huy'),
                html.Div('18084851 - Châu Quốc An'),
                html.Div('18072661 - Lại Văn Vượng')       
                ],className='col-4'),
            ], className='row', style={ 'fontSize': '15px' })
        ])
    ], className='mt-5 bg-light intro'),

    #my team
    # background
], className='container mt-5')

##-----------------------------------------------------
#Simple Chart Link
simpleChart = html.Div([
     html.Div(style={
        'width': '100%',
        'height': '100%',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'z-index': '-999'
    }, className='bg-dark'),
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Matplotlib', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Matplotlib', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Introducing to matplotlib:', className='introMatplotlib'),
                html.Span('asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd ',className='content')
            ])
           
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

##-----------------------------------------------------

df = pd.DataFrame({'PDD': ['Pop','Pop','Pop','Pop','Pop','Pop','Pop','Pop','Pop','Pop','Pop',
                                 'Birth','Birth','Birth','Birth','Birth','Birth','Birth','Birth','Birth','Birth','Birth',
                                'Death','Death','Death','Death','Death','Death','Death','Death','Death','Death','Death'],
                   'Units': [9121350.692, 9211390.569,9298979.218,9384393.559,9467486.975,9548200.152,9626818.38,9703526.175,9778659.789,9852408.599,9924970.291,
                            127533.3476,127885.153,128324.9541,128801.6843,129233.04,129600.5457,129961.0983,130317.1128,130663.6129,131047.3682,131487.2486,
                            51176.87663,51135.29448,51177.02141,51294.318,51485.16367,51803.97713,52212.18212,52673.59493,53184.19643,53741.82139,54315.44647
],
                   'Year':[2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,
                             2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,
                             2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,]})

groups = df.groupby(by='PDD')

data = []
colors=['red', 'blue', 'green']

for group, dataframe in groups:
    dataframe = dataframe.sort_values(by=['Year'])
    trace = go.Scatter(x=dataframe.Year.tolist(), 
                       y=dataframe.Units.tolist(),
                       marker=dict(color=colors[len(data)]),
                       name=group)
    data.append(trace)

layout =  go.Layout(xaxis={'title': 'Year'},
                    yaxis={'title': 'Population'},
                    margin={'l': 40, 'b': 40, 't': 50, 'r': 50},
                    hovermode='closest')

test = go.Figure(data=data, layout=layout)  

##-----------------------------------------------------
# Line Chart Link
lineChart = html.Div([
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Matplotlib', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Line Chart', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Description:', className='introMatplotlib'),
                html.Span('asdasdasd asdasdasd asdasdas dasdasdasd asdasdasd asdasdas dasdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd ',className='content')
            ]),
            html.Div([
                 html.Span('When using?:', className='introMatplotlib'),
                html.Span('asdasdasd asdasdasd asdasdas dasdasdasd asdasdasd asdasdas dasdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd ',className='content')
            ]),
            html.Div([
                 html.Span('Type of Charts:', className='introMatplotlib'),
                html.Span('asdasdasd asdasdasd asdasdas dasdasdasd asdasdasd asdasdas dasdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd ',className='content')
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= {
                        'data' : [
                            { 'x': arrLondonYear , 'y': arrLondonPop, 'type' : 'line', 'name' : 'Line Chart'}
                        ] ,
                        'layout' : {
                            'title' : 'Population of London 10 years later',
                            'xaxis' : { 'title': 'year'},
                            'yaxis' : { 'title': 'population'}
                        }
                    }), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= test), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

##-----------------------------------------------------
# and this code to transfer to another link
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/simple-chart':
        return simpleChart
    elif pathname == '/line-chart':
        return lineChart
    else:
        return main
#     elif pathname == '/page2':
#         return page2
#     else:
#         return pageDefault


if __name__ == "__main__":
    app.run_server()
