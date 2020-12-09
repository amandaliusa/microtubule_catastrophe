import iqplot
import bebi103 

import bokeh.io

from modeling import theor_cdf_custom

bokeh.io.output_notebook()
bebi103.hv.set_defaults()

def ecdf_beta_ratios_df(beta1, beta2):
    '''Generates dataframe for plotting ECDF of Times to Catastrophe 
    according to custom model parametrized by various rates
    
    Arguments: 
    beta1: array of rates for first Poisson process
    beta2: array of rates for second Poisson process
    '''

    # compute ratios between beta2 and beta1
    ratio = []
    for j in range(len(beta1)):
        ratio.append(beta2[j] / beta1[j])

    # creating column for beta2/beta1 ratios to use in DataFrame
    ratio_col = []
    for i in ratio:
        ratio_col.append([i]*150)

    ratio_col = np.array(ratio_col).flatten()

    # create column of time values
    val_col = []
    for i in range(len(beta1)):
        x1 = np.random.exponential(1/beta1[i], 150)
        x2 = np.random.exponential(1/beta2[i], 150)
        val_col.append(x1 + x2)

    val_col = np.array(val_col).flatten()

    # create the dataframe
    df = pd.DataFrame({'beta2/beta1 ratio': ratio_col, 'total time (1/beta1)': val_col})
    
    return df

def ecdf_beta_ratios(df):
    '''Plots ECDF of Times to Catastrophe according to 
    custom model parametrized by various rates
    
    Website Figure 2
    '''
    p = iqplot.ecdf(
        data=df,
        q = 'total time (1/beta1)',
        cats = ['beta2/beta1 ratio'],
        style='staircase',
        title='Time to Catastrophe for Different Beta2/Beta1'
    )

    p.legend.title = 'beta2/beta1'

    return p