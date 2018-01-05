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

# the script only works if this line is here. not sure why it is in THIS script.
app.config.suppress_callback_exceptions=True

# We are going to create the layout that will be displayed when we select this page. 
layout = html.Div([
    html.H2('Yearly Comparison'),

    #Div to hold drop downs and inputs
    html.Div([
        html.Div([
            # Structure is label then widget
            html.Label('Entity'),
            dcc.Dropdown(
                id = 'subsidiary',
                options = [
                    {'label':i,'value':i} for i in df.Entity.unique()
                    ],
                value = df.Entity[1]
                )
            ],style = st.style_widgets
            ),
        html.Div([
            html.Label('Ecosytem'),
            dcc.Dropdown(id = 'ecosystem',value = 'Real Estate')],
            style = st.style_widgets
            ),
        html.Div([
            html.Label('Profession'),
            dcc.Dropdown(id = 'prof',value='Real Estate')],
            style = st.style_widgets
            ),
        html.Div([
            html.Label('Education Type'),
            dcc.Dropdown(id = 'education',value='CE')],
            style = st.style_widgets
            ),
        html.Div([
            html.Label('Delivery Method'),
            dcc.Dropdown(id = 'del_met',value='Virtual Classroom')],
            style = st.style_widgets
            ),
        ]), # end of Div holding widgets

    #below is the div containing the graph
    html.Div([
        dcc.Graph(id = 'BarChart',
            config = {'displayModeBar':False}
            ),
        ])
    ])


#-----------------------------------------------------------------------------
# all callbacks below here

@app.callback(Output('BarChart','figure'),
        [Input('subsidiary','value'),
            Input('ecosystem','value'),
            Input('education','value'),
            Input('del_met','value'),
            Input('prof','value')])
def display_chart(ent,eco,edu,delivery,prof):
    # filter dataframe down. Not on one line for easy editting. 
    dff = df
    dff = dff[dff.Entity == ent]
    dff = dff[dff.Ecosystem == eco]
    dff = dff[dff['Education Type'] == edu]
    dff = dff[dff['Delivery Method'] == delivery]
    dff = dff[dff.Profession == prof]
    dff = dff[dff.Metric == 'Net Sales']
    # now to group by and reset index for graphing
    dff = dff.groupby(['Month','Year']).sum()
    dff = dff.reset_index()
    # create a bar chart and give x and y
    data = [{
        'x':dff[dff.Year == i]['Month'],
        'y':dff[dff.Year == i]['Value'],
        'type':'bar',
        'name':i,
        'marker': {
            #'color':st.colours['lite_grey'],
            'line':{
                'color':st.colours['dark_grey'],
                'width':2
                }
            }
        }for i in dff.Year.unique()[1:4]] #creates a bar for three years 
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
                'title':'Month'
                },
            'padding':1,
            'borderStyle':'solid',
            'borderWidth':1,
            'borderColor':st.colours['dark_grey']
            }

    return {'data':data,'layout':layout}

#=================================================
# Widget call backs here. Split by widget

@app.callback(Output('ecosystem','options'),
        [Input('subsidiary','value')])
def ecosytem_options(ent):
    dff = df
    dff = dff[dff.Entity == ent] 
    # o for options
    o = [{'label':j,'value':j} for j in dff.Ecosystem.unique()]
    return o

#=-=-=-=-=-=-=-=-=-=-=-=-=-=#
@app.callback(Output('prof','options'),
        [Input('subsidiary','value'),
            Input('ecosystem','value')])
def prof_options(ent,eco):
    dff = df
    dff = dff[dff.Entity == ent] 
    dff = dff[dff.Ecosystem == eco]
    # o for options
    o = [{'label':j,'value':j} for j in dff.Profession.unique()]
    return o

#=-=-=-=-=-=-=-=-=-=-=-=-=-=#
@app.callback(Output('education','options'),
        [Input('subsidiary','value'),
            Input('ecosystem','value'),
            Input('prof','value')])
def education_options(ent,eco,prof):
    dff = df
    dff = dff[dff.Entity == ent] 
    dff = dff[dff.Ecosystem == eco]
    dff = dff[dff.Profession == prof]
    # o for options
    o = [{'label':j,'value':j} for j in dff['Education Type'].unique()]
    return o


#=-=-=-=-=-=-=-=-=-=-=-=-=-=#
@app.callback(Output('del_met','options'),
        [Input('subsidiary','value'),
            Input('ecosystem','value'),
            Input('prof','value'),
            Input('education','value')])
def delivery_options(ent,eco,prof,edu):
    dff = df
    dff = dff[dff.Entity == ent] 
    dff = dff[dff.Ecosystem == eco]
    dff = dff[dff.Profession == prof]
    dff = dff[dff['Education Type'] == edu]
    # o for options
    o = [{'label':j,'value':j} for j in dff['Delivery Method'].unique()]
    return o

'''
Index([u'Entity', u'Ecosystem', u'Metric', u'Data Type', u'Value', u'Month',
       u'Year', u'State', u'Profession', u'Delivery Method', u'Education Type',
       u'Metric Minus Detail']'''
