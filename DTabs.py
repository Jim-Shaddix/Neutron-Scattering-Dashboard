import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from typing import List

# File containing the text that populates the tab
neutron_file = "NeutronText.txt"

def neutron_text() -> List[html.P]:
    """
    :return: a list of the html paragragh objects to use in the tab for 
             describing neutron scattering experiments
    """

    # Value to be returned
    all_paragraphs = []

    # Create Neutron Text
    with open(neutron_file) as fd:

        # Skip first blanck lines
        first_flag = True 
        curr_paragraph = []

        for line in fd:

            # Case: empty first lines
            if first_flag:
                if line.isspace():
                    continue
                else:
                    first_flag = False

            # Case: empty line encountered
            if line.isspace():
                if len(curr_paragraph) != 0:
                    par = "".join(curr_paragraph)
                    all_paragraphs.append(html.P(par))
                else:
                    continue

            # Case: general
            line = line.replace("\n", " ")
            curr_paragraph.append(line)

    return all_paragraphs

    # Case: last paragrph
    if len(curr_paragraph) != 0:
        par = "".join(curr_paragraph)
        all_paragraphs.append(html.P(par))


tabs = \
    html.Div(id='manhattan-control-tabs', className='control-tabs', children=[
            dcc.Tabs(id='manhattan-tabs', value='what-is', children=[
                dcc.Tab(
                    label='About',
                    value='what-is',
                    children=html.Div(className='control-tab', children=[
                        html.H4(className='what-is', children="What's Neutron Scattering All About?"),
                        html.P(
                               'Neutron scattering, the irregular dispersal of free ' 
                               'neutrons by matter, can refer to either the naturally '
                               'occurring physical process itself or to the man-made '
                               'experimental techniques that use the natural process '
                               'for investigating materials. The natural/physical phenomenon'
                               'is of elemental importance in nuclear engineering and '
                               'the nuclear sciences. Regarding the experimental technique,'
                               'understanding and manipulating neutron scattering is fundamental '
                               'to the applications used in crystallography, physics, physical chemistry,'
                               ' biophysics, and materials research.'),
                        html.P('Neutron scattering is practiced at research reactors and '
                               'spallation neutron sources that provide neutron radiation'
                               'of varying intensities. Neutron diffraction (elastic scattering)'
                               'techniques are used for analyzing structures; where inelastic neutron scattering '
                               'is used in studying atomic vibrations and other excitations.'),
                        html.A(
                               dbc.Button("Ross Labs", color="primary", className="mr-1"),
                               href="http://www.rosslabcsu.com/"
                        )
                    ])
                ),
                dcc.Tab(
                    label='Graph',
                    value='graph',
                    children=html.Div(className='control-tab', children=[
                        html.Div(className='app-controls-block', children=[


                            # scroll-bar and input field
                             dbc.Row([

                                 # title and scrollbar
                                 dbc.Col([

                                     html.Div(
                                         html.P("Scan Axis:")
                                     ),

                                     # axis-dropdown
                                     dcc.Dropdown(
                                         options=[
                                             {'label': 'X', 'value': 'x'},
                                             {'label': 'Y', 'value': 'y'}
                                         ],
                                         value='y',
                                         id="dropdown-axis"
                                     ),

                                 ], width=6),


                                 # title and input field
                                 dbc.Col([

                                     html.Div(
                                         html.P("Axis Value:")
                                     ),

                                     dcc.Input(
                                         placeholder='0',
                                         type='number',
                                         readOnly="readOnly",
                                         value='0',
                                         id="input-axis-value"
                                     )

                                 ], width=6)


                             ]),

                            html.Div(
                                className='app-controls-name',
                                children=[
                                    'Set Axis Value'
                                ]
                            ),

                            # slider
                            html.Div([

                                dcc.Slider(
                                    id="slider-heatmap",
                                    value=1,
                                )

                            ], id="div-slider")
                            #dcc.Slider(
                            #    id='mhp-slider-genome',
                            #    className='control-slider',
                            #    vertical=False,
                            #    updatemode='mouseup',
                            #    max=4,
                            #    min=1,
                            #    value=2,
                            #    marks={
                            #        i + 1: '{}'.format(i + 1)
                            #        for i in range(4)
                            #    },
                            #    step=0.05
                            #),
                        ])
                    ])
                )
            ])
        ])