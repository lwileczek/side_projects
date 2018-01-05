# This scripts creates a web based dahsboard using Plot.ly's Dash packages. 

#import scripts used below. 
from dash.dependencies import Input, Output # used for call backs.  
import dash_core_components as dcc # used to create widgets and graphs.
import dash_html_components as html #used to generate html for webpage.

# modules made by me
from app import app    # Another python script we created. 
import style as st

#app.config.suppress_callback_exceptions=True

markdown_text = ''' ### Hello!
Welcome to the MDB dashboard. This will be used to quickly vizualize the
informaition stored in the MDB.

### Tabs:
    1. Summary
    2. Comparison
    3. Data

#### Summary
The summary tab is used to track the perfomance of an entity, ecosystem or
profession over time.

#### Comparison
The comparison tab is used to compare KPIs of entities, ecosystems and 
professions in a single year

#### Data
The Data tab presents the raw data in an HTML table. Unfortunatly not the
best for export. This can be done if requested. '''

layout = html.Div([
    html.Div([
        dcc.Markdown(children = markdown_text)],
        style = {
            'margin':'2%',
            'color': st.colours['black'],
            'backgroundColor': st.colours['white'],
            'borderStyle':'solid',
            'borderColor': st.colours['dark_grey'],
            'borderWidth': 2
            }
        )
    ])
