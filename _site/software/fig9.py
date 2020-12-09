import iqplot
import bebi103 

import bokeh.io

from modeling import theor_cdf_custom

bokeh.io.output_notebook()
bebi103.hv.set_defaults()

def predictive_ecdf(data, samples, model_name, diff=False):
    '''
    Generates predictive ECDFs to compare between the generative
    distribution and measured data.
    
    Arguments:
    data: measured data
    samples: generative samples
    model_name: string, either 'Gamma' or 'Custom'
    diff: whether to compute ECDF differences or not
    
    Website Figures 7-10
    '''
    
    if diff:
        p = bebi103.viz.predictive_ecdf(
            samples=samples, 
            data=data, 
            x_axis_label='time to catastrophe (s)', 
            title='Predictive ECDFs for {} Model'.format(model_name),
            diff='ecdf'
        )
    else:
        p = bebi103.viz.predictive_ecdf(
            samples=samples, 
            data=data, 
            x_axis_label='time to catastrophe (s)', 
            title='Predictive ECDFs for {} Model'.format(model_name)
        )
    
    return p
