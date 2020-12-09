import iqplot
import bebi103 

import bokeh.io

from modeling import theor_cdf_custom

bokeh.io.output_notebook()
bebi103.hv.set_defaults()

def plot_conf_ints(estimates, conf_ints, labels):
    '''
    Visualization of confidence intervals 
    
    Arguments:
    estimates: MLEs of parameter of interest
    conf_ints: confidence intervals for MLEs in estimates 
    labels: labels for each confidence interval to be plotted
    
    Website Figures 4, 11, 12
    '''
    
    summaries = [
        dict(estimate=est, conf_int=conf, label=name)
        for est, conf, name in zip(
            estimates, conf_ints, labels
        )
    ]

    p = bebi103.viz.confints(summaries)

    return p


