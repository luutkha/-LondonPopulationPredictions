import dash_bootstrap_components as dbc
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

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

    # background
    html.Div(style={
        'width': '100%',
        'height': '100%',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'z-index': '-999'
    }, className='bg-dark')
], className='container mt-5')

# and this code to transfer to another link


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return main
#     elif pathname == '/page2':
#         return page2
#     else:
#         return pageDefault


if __name__ == "__main__":
    app.run_server()
