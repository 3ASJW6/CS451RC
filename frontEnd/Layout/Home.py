# Import <
from dash import html, dcc
from backEnd.API.Utility import getJSON
import dash_bootstrap_components as dbc

# >


# Declaration <
# note: we get a user's data in here
# and not in Login.py. in Login.py we
# set the data for a user.
style = getJSON(file = '/frontEnd/Resource/Home.json')

# >


homeLayout = html.Div(id = 'homeLayoutId',
                      children = [

                          # Header <
                          dbc.Row([

                              dbc.Col(

                                  # Background <
                                  html.Div(id = 'divHeaderBackgroundId',
                                           children = [

                                               # Content <
                                               dbc.Row([

                                                   # Logo <
                                                   dbc.Col(

                                                       html.Img(src = style['logoSrc'],
                                                                style = style['logoStyle']),

                                                   width = 'auto'),

                                                   # >

                                                   # Search <
                                                   dbc.Col(

                                                       dbc.InputGroup([

                                                           dbc.Input(id = 'inputSearchId',
                                                                     placeholder = 'Search'),
                                                           dbc.DropdownMenu(label = 'Role',
                                                                            id = 'dropdownMenuSearchId',
                                                                            color = style['dropdownMenuSearchColor'])

                                                       ]),

                                                   align = 'center', width = 'auto')

                                                   # >

                                               ], justify = 'between')

                                               # >

                                           ], style = style['divHeaderBackgroundStyle']),

                                  # >

                              width = True)

                          ]),

                          # >

                          # Body <
                          dbc.Row([

                              # Navigation Bar <
                              dbc.Col(

                                  html.Div(id = 'divMenuId',
                                           children = [

                                               #

                                           ], style = style['divMenuStyle']),

                              width = 'auto'),

                              # >

                              # Dashboard <
                              dbc.Col(

                                  html.Div(id = 'divDashboardId',
                                           children = [

                                               #

                                           ], style = style['divDashboardStyle']),

                              width = True)

                              # >

                          ], className = 'g-0')

                          # >

                      ], style = style['homeLayoutStyle'])
