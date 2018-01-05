# This scripts creates a web based dahsboard using Plot.ly's Dash packages. 

#import scripts used below. 
from dash.dependencies import Input, Output # used for call backs.  
import dash_core_components as dcc # used to create widgets and graphs.
import dash_html_components as html #used to generate html for webpage.
import pandas as pd # used to load data
import style as st  # another python script style dictionaries and colors
from app import app    # Another python script we created. 

#load in the data
df = pd.read_csv("mdb.csv")

# We are going to create the layout that will be displayed when we select this page. 
layout = html.Div([
    html.H2('State comparison'),

    #Div to hold drop downs and inputs
    html.Div([
        html.Div([
            # Structure is label then widget
            html.Label('Entity'),
            dcc.Dropdown(
                id = 'subsidiary2',
                options = [
                    {'label':i,'value':i} for i in df.Entity.unique()
                    ],
                value = 'McKissock'
                )
            ],style = st.style_widgets
            ),
        html.Div([
            html.Label('Ecosytem'),
            dcc.Dropdown(id = 'ecosystem2',value='Real Estate')],
            style = st.style_widgets
            ),
        html.Div([
            html.Label('Profession'),
            dcc.Dropdown(id = 'prof2',value='Appraisal')],
            style = st.style_widgets
            ),
        html.Div([
            html.Label('Education Type'),
            dcc.Dropdown(id = 'education2',value='CE')],
            style = st.style_widgets
            ),
        html.Div([
            html.Label('Delivery Method'),
            dcc.Dropdown(id = 'deliveryMeth2',value = 'Virtual Classroom')],
            style = st.style_widgets
            ),
        html.Div([
            html.Label('Metric'),
            dcc.Dropdown(id = 'metric',value = 'Net Sales')],
            style = st.style_widgets
            )
        ]), # end of Div holding widgets

    #below is the div containing the graph
    html.Div([
        dcc.Graph(id = 'barChart2',
            config = {'displayModeBar':False}
            ),
        ])
    ])


#-----------------------------------------------------------------------------
# all callbacks below here

@app.callback(Output('barChart2','figure'),
        [Input('subsidiary2','value'),
            Input('ecosystem2','value'),
            Input('education2','value'),
            Input('deliveryMeth2','value'),
            Input('prof2','value'),
            Input('metric','value')])
def display_chart(ent,eco,edu,delivery,prof2,met):
    # filter dataframe down. Not on one line for easy editting. 
    dff = df
    dff = dff[dff.Entity == ent]
    dff = dff[dff.Ecosystem == eco]
    dff = dff[dff['Education Type'] == edu]
    dff = dff[dff['Delivery Method'] == delivery]
    dff = dff[dff.Profession == prof2]
    dff = dff[dff.Metric == met]
    # now to group by and reset index for graphing
    dff = dff.groupby(['State']).sum()
    dff = dff.reset_index()
    # create a bar chart and give x and y
    data = [{
        'x':dff[dff.State == i]['State'],
        'y':dff[dff.State == i]['Value'],
        'type':'bar',
        'name':i,
        'marker': {
            #'color':st.colours['lite_grey'],
            'line':{
                'color':st.colours['dark_grey'],
                'width':2
                }
            }
        }for i in dff.State.unique()[1:4]] #creates a bar for three years 
    # layout of chart
    layout = {
            # the following are commented out because they are defaults
            #'plot_bgcolor':st.colours['white'],
            #'paper_bgcolor':st.colours['lite_grey'],
            #'font':{
            #    'color':st.colours['black']
            #    },
            'title':'Yearly Comparison of Sales',
            'yaxis': {
                'title':'Sales'
                },
            'xaxis':{
                'title':'State'
                },
            'padding':1,
            'borderStyle':'solid',
            'borderWidth':1,
            'borderColor':st.colours['dark_grey']
            }

    return {'data':data,'layout':layout}

#=================================================
# Widget call backs here. Split by widget

@app.callback(Output('ecosystem2','options'),
        [Input('subsidiary2','value')])
def ecosytem_options(ent):
    dff = df
    dff = dff[dff.Entity == ent] 
    # o for options
    o = [{'label':j,'value':j} for j in dff.Ecosystem.unique()]
    return o

#=-=-=-=-=-=-=-=-=-=-=-=-=-=#
@app.callback(Output('prof2','options'),
        [Input('subsidiary2','value'),
            Input('ecosystem2','value')])
def prof2_options(ent,eco):
    dff = df
    dff = dff[dff.Entity == ent] 
    dff = dff[dff.Ecosystem == eco]
    # o for options
    o = [{'label':j,'value':j} for j in dff.Profession.unique()]
    return o

#=-=-=-=-=-=-=-=-=-=-=-=-=-=#
@app.callback(Output('metric','options'),
        [Input('subsidiary2','value'),
            Input('ecosystem2','value'),
            Input('prof2','value')])
def metric_options(ent,eco,prof2):
    dff = df
    dff = dff[dff.Entity == ent] 
    dff = dff[dff.Ecosystem == eco]
    dff = dff[dff.Profession == prof2]
    # o for options
    o = [{'label':j,'value':j} for j in dff.Metric.unique()]
    return o

#=-=-=-=-=-=-=-=-=-=-=-=-=-=#
@app.callback(Output('education2','options'),
        [Input('subsidiary2','value'),
            Input('ecosystem2','value'),
            Input('prof2','value')])
def education2_options(ent,eco,prof2):
    dff = df
    dff = dff[dff.Entity == ent] 
    dff = dff[dff.Ecosystem == eco]
    dff = dff[dff.Profession == prof2]
    # o for options
    o = [{'label':j,'value':j} for j in dff['Education Type'].unique()]
    return o


#=-=-=-=-=-=-=-=-=-=-=-=-=-=#
@app.callback(Output('deliveryMeth2','options'),
        [Input('subsidiary2','value'),
            Input('ecosystem2','value'),
            Input('prof2','value'),
            Input('education2','value')])
def delivery_options(ent,eco,prof2,edu):
    dff = df
    dff = dff[dff.Entity == ent] 
    dff = dff[dff.Ecosystem == eco]
    dff = dff[dff.Profession == prof2]
    dff = dff[dff['Education Type'] == edu]
    # o for options
    o = [{'label':j,'value':j} for j in dff['Delivery Method'].unique()]
    return o

'''
Index([u'Entity', u'Ecosystem', u'Metric', u'Data Type', u'Value', u'Month',
       u'Year', u'State', u'Profession', u'Delivery Method', u'Education Type',
       u'Metric Minus Detail']'''
