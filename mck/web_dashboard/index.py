# this is the index script used to switch between pages in application

from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app
from style import header_layout
from apps import app1, app2, data, landing_page

#------------------------------------------------------------------------------
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
    ])
#------------------------------------------------------------------------------

@app.callback(
        Output('page-content','children'),
        [Input('url','pathname')])
def dispaly_page(pathname):
    if pathname == '/apps/app1':
        webpage_display = html.Div([header_layout,app1.layout])
        return webpage_display 
    elif pathname == '/apps/app2':
        webpage_display = html.Div([header_layout,app2.layout])
        return webpage_display 
    elif pathname == '/raw+data':
        webpage_display = html.Div([header_layout,data.layout])
        return webpage_display 
    else:
        webpage_display = html.Div([header_layout,landing_page.layout])
        return webpage_display 

#------------------------------------------------------------------------------
app.css.append_css({
     'external_url': (
         'https://rawgit.com/lwileczek/Dash/master/mck_tst0.css'
         #'https://rawgit.com/lwileczek/Dash/master/v5.css'
     )
 })
#------------------------------------------------------------------------------

if __name__=='__main__':
    app.run_server(debug=True)
