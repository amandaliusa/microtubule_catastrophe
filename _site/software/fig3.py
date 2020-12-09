import iqplot
import bebi103 

import bokeh.io

from modeling import theor_cdf_custom

bokeh.io.output_notebook()
bebi103.hv.set_defaults()

def ecdf_vs_theor_cdf(beta1, beta2):
    '''Plots theoretical CDF vs simulated ECDF of custom model
    given parameters beta1, beta2
    
    Website Figure 3
    '''
    
    # simulated ECDF values
    df = ecdf_beta_ratios_df([beta1], [beta2])

    p = iqplot.ecdf(data=df,
            q = 'total time (1/beta1)',
            cats = ['beta2/beta1 ratio'],
            show_legend=False,
            title='Analytical CDF vs Simulated ECDF for Time to Catastrophe'
        )

    # plot analytical CDF
    t = np.linspace(0, max(df['total time (1/beta1)']))
    f = theor_cdf_custom(beta1, beta2)

    p.line(x=t, y=f, line_width=2, line_color='red')

    # add a legend
    legend = bokeh.models.Legend(
                items=[('analytical CDF', [p.circle(color='red')]),
                       ('ECDF', [p.circle(color='blue')])
                      ],
                location='center')
    p.add_layout(legend, 'right')

    return p
