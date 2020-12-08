import numpy as np
import pandas as pd
import scipy.stats

import iqplot
import bebi103 

import numba

import bokeh.io

bebi103.hv.set_defaults()


def plot_fig1(df):

    p = iqplot.ecdf(
        data=df,
        q='time to catastrophe (s)',
        cats='labeled',
        conf_int=True,
        x_axis_label='time (sec)',
        y_axis_label='empirical ecdf',
        title='ECDF of Time to Catastrophe'
    )
    bokeh.io.show(p)