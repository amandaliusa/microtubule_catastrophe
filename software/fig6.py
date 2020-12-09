import iqplot
import bebi103 

import bokeh.io

from modeling import theor_cdf_custom

bokeh.io.output_notebook()
bebi103.hv.set_defaults()

def qq_plot(df, samples, model_name):
    '''Generate QQ plot of generative vs observed quantiles for 
    microtubule catastrophe data
    
    Arguments:
    df: dataframe of experimental measurements
    samples: samples drawn from generative distribution
    model_name: string, either 'Gamma' or 'Custom'
    
    Website Figures 5 and 6
    '''
    p = bebi103.viz.qqplot(
        data=df,
        samples=samples,
        x_axis_label="time to catastrophe (s)",
        y_axis_label="time to catastrophe (s)",
        title='Q-Q Plot for {} Model'.format(model_name)
    )

    return p
