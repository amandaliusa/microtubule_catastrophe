import iqplot
import bebi103 

import bokeh.io

from modeling import theor_cdf_custom

bokeh.io.output_notebook()
bebi103.hv.set_defaults()

"""
Functions to plot microtubule catastrophe data
"""

def ecdf_labeled_unlabeled(df):
    '''Generates ECDF plot for times to catastrophe
    for labeled and unlabeled tubulin
    
    Website Figure 1
    '''
    p = iqplot.ecdf(
        data=df,
        q='time to catastrophe (s)',
        cats='labeled',
        conf_int=True,
        x_axis_label='time (sec)',
        y_axis_label='empirical ecdf',
        title='ECDF of Time to Catastrophe'
    )
    
    return p
