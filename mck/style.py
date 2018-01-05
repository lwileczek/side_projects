# This scripts creates a web based dahsboard using Plot.ly's Dash packages. 

#import scripts used below. 
import dash_core_components as dcc # used to create widgets and graphs.
import dash_html_components as html #used to generate html for webpage.

#------------------------------------------------------------------------------
# setting up standard colors for consistancy across tabs
colours = {
        'blue':'#093162', #Penn State Blue 
        'white':'#FFFFFF',
        'black':'#000000',
        'dark_grey':'#555555',
        'lite_grey':'#DDDDDD',
        'red':'#91092F', #Chicago maroon
        'green':'#18453B' # MSU green
        }

#------------------------------------------------------------------------------
# Putting standard styles to be used below and elsewhere

style_title_links = {
        'width':'20%',
        'display':'inline-block',
        #'color':colours['white'],
        'textAlign':'center'
        }

style_widgets = {
        'width':'15%',
        'display':'inline-block',
        'padding':1
        }
#------------------------------------------------------------------------------
# The following will be the header/title at the top of all web pages. 
header_layout = html.Div([

    html.Div([
        #the next div holds the app title. 
        html.Div([
            html.H1(
                'MDB Analysis',
                style={
                    'color':colours['white']
                    }
                )
            ], style ={
                'marginLeft':'30%',
                'width':'50%',
                'textAlign':'center',
                'display':'inline-block'
                }
            ),

        html.Div([
            html.H3(
                dcc.Link(
                    'Index Page',
                    href='/'),
                style= style_title_links
                ),
            html.H3(
                dcc.Link(
                    'Summary',
                    href='/apps/app1'),
                style=style_title_links
                ),
            html.H3(
                dcc.Link(
                    'Comparison',
                    href='/apps/app2'),
                style=style_title_links
                ),
            html.H3(
                dcc.Link(
                    'Data',
                    href='/raw+data'),
                style=style_title_links
                ),
            ],
            style = {
                'marginLeft':'25%'
                }
            ) # end div holding links

        ],
        style = {
            'width':'90%',
            'display':'inline-block'
            }
        ),

        html.Div([
            html.Img(
                src='https://cdn.rawgit.com/lwileczek/Dash/79165bc9/colibri.png',
                style = {
                    'width':'90%',
                    'height':'90%',
                    'float':'left'
                    }
                )
            ],
            style = {
                'display':'inline-block',
                'width':'10%'
                }
            )

    ],#style for entire header/title div
    style = {
        'backgroundColor':colours['blue'],
        'color': colours['white'],
        #'display':'inline-block',
        'width':'100%',
        'borderStyle':'solid',
        'borderColor':colours['dark_grey'],
        'borderWidth':3
        }
)#end of header
