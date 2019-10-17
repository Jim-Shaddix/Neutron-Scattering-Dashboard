# Neutron-Scattering-Dashboard
Dashboard application displaying Neutron Scattering data for [Dr. Kate Ross's web site](http://www.rosslabcsu.com/).
 
## Dash Application:
![](assets/images/Neutron-Scattering.png)

## Description:
This repository contains code for generating a dashboard application
that displays  [neurtron scattering][https://en.wikipedia.org/wiki/Neutron_scattering] 
experiments.

This dashboard application was built using Python's dash library. 
It allows for the user to sweep across a heat map that displays 
Neutron Intensities that were recieved during an experiment. As you 
sweep across the heatmap, a plot is updated that displays data associated
with the current cross section. 


## Dependencies
* python3.7
* Third party python libraries listed in **requirements.txt**

## Installation Instructions

1. Clone the repo
```Bash
git clone https://github.com/Jim-Shaddix/Personal-Website.git
```
2. You can than use the following command to download all the third party libraries
needed to run this program.
```Bash
pip install -r requirements.txt
```
3. Run the application!
```Bash
python app.py
```

#### Files
* main.py: contains code for running the application.
* Dtabs.py: contains code for generating the ``Description`` and ``Graph`` tabs.
* graphs.py: generates surface and scatter plots for the data.

## Citations
* The code for the tab bar (as well as the CSS colorscheme I used) was largely 
based on (or taken from) the code examples in the [dash-bio repository](https://github.com/plotly/dash-bio/blob/master/tests/test_manhattan_plot.py).
