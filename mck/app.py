''' Following Plot.ly's sytle guide for multi-page applications.
https://plot.ly/dash/urls '''

import dash

app = dash.Dash()

# server = app.server
# app.config.surpress_callback_exceptions = True

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
