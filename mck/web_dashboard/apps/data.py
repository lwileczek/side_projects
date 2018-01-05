# This scripts creates a web based dahsboard using Plot.ly's Dash packages. 

#import scripts used below. 
from dash.dependencies import Input, Output # used for call backs.  
import dash_core_components as dcc # used to create widgets and graphs.
import dash_html_components as html #used to generate html for webpage.
import pandas as pd # used to load data
from app import app    # Another python script we created. 

# load data
df = pd.read_csv("mdb.csv")

#------------------------------------------------------------------------------
## UDF to generate table

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )  
#------------------------------------------------------------------------------
## the layout below that will be shown on the page

layout = html.Div(children=[
    html.Div([
        html.Div([
            html.H4('Raw Data')],
            style = {
                'display':'inline-block',
                'width':'25%'
                }
            ),
        html.Div([
            html.Label("Number of Rows"),
            dcc.Input(
                id = 'rows',
                placeholder = 'Enter Number of Rows...',
                value = '10',
                type = 'text'
                )],
            style = {
                'display':'inline-block',
                'width':'25%'
                }
            )
        ]),

        # next div should hold the table generated
        html.Div(id = 'tbl')
        ])    
#------------------------------------------------------------------------------
## Callback to create table

@app.callback(Output('tbl','children'),
    [Input('rows','value')])
def make_table(n_rows):
    return generate_table(df,int(n_rows))
