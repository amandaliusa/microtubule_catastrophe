---
layout: page
title: Home
description: Microtubule Catastrophe
img: #about.png # Add image post (optional)
caption: #"A Serious Man (2010)"
permalink: index.html
sidebar: true
---

---


# {{site.data.about.title}}
{{site.data.about.authors}}

{% for entry in site.data.about %}

{% if entry[0] != 'title' %}
{% if entry[0] != 'authors' %}

{% if entry[0] != 'fig2.2' and entry[0] != 'fig5.2a' and entry[0] != 'fig5.2b' and entry[0] != 'fig6.1' and entry[0] != 'fig8.2'
and entry[0] != 'fig9.1a' and entry[0] != 'fig9.1b' and entry[0] != 'fig9.1c' and entry[0] != 'fig9.1d' and entry[0] != 'fig9.1e'
and entry[0] != 'fig9.1f' and entry[0] != 'fig9.1g' and entry[0] != 'fig9.1h'%}
## {{entry[0]}}
{% endif %}

{% if entry[0] == 'fig2.2' %}
<center>
    <img src="assets/img/2.2_ecdfs.png" width="500" height="400"/>
    <figcaption> ECDFs of Time to Catastrophe for Labeled vs Unlabeled Tubulin </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig5.2a' %}
<center>
    <img src="assets/img/5.2_ecdf_diff_b2_b1_ratios.png" width="500" height="400"/>
    <figcaption> ECDFs of Time to Catastrophe with Different b2/b1 ratios </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig5.2b' %}
<center>
    <img src="assets/img/5.2_ecdf_model2_vs_data.png" width="500" height="400"/>
    <figcaption> Analytical vs Simulated ECDF of Time to Catastrophe </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig6.1' %}
<center>
    <img src="assets/img/6.1_ecdf_unlabeled_labeled.png" width="500" height="400"/>
    <figcaption> ECDF of Time to Catastrophe for Labeled vs Unlabeled Tubulin, with Confidence Intervals </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig8.2' %}
<center>
    <img src="assets/img/8.2_beta_conf_int_comparison.png" width="500" height="400"/>
    <figcaption> Confidence Intervals for Rates, Both Models </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9.1a' %}
<center>
    <img src="assets/img/9.1_alpha_conf_int.png" width="500" height="400"/>
    <figcaption> Confidence Intervals for Alpha at Different Concentrations, Gamma Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9.1b' %}
<center>
    <img src="assets/img/9.1_beta_conf_int.png" alt="Beta Confidence Interval" width="500" height="400"/>
    <figcaption> Confidence Intervals for Beta at Different Concentrations, Gamma Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9.1c' %}
<center>
    <img src="assets/img/9.1_custom_model_predictive_ecdf_diff.png" alt="Custom Model Predictive ECDF Difference" width="500" height="400"/>
    <figcaption> Predictive ECDF Differences, Custom Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9.1d' %}
<center>
    <img src="assets/img/9.1_custom_model_predictive_ecdf.png" alt="Custom Model Predictive ECDF" width="500" height="400"/>
    <figcaption> Predictive ECDFs, Custom Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9.1e' %}


<div class="imageContainer" style="text-align:center;">
    <div style="margin-left: auto;float:left;margin-right:5px;">
        <img src="assets/img/9.1_custom_model_QQ_plot.png" height="400" width="500"  />
        <figcaption style="text-align:center;"> QQ Plot, Custom Model </figcaption>
    </div>
    <div style="float:left;margin-right:5px;">
        <img src="assets/img/9.1_gamma_QQ_plot.png" height="400" width="500" />
        <figcaption style="text-align:center;"> QQ Plot, Gamma Model </figcaption>
    </div>
</div>

{% endif %}

{% if entry[0] == 'fig9.1f' %}
<center>
    <img src="assets/img/9.1_gamma_model_predictive_ecdf_diff.png" alt="Gamma Model Predictive ECDF Difference" width="500" height="400"/>
    <figcaption> Predictive ECDF Difference, Gamma Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9.1g' %}
<center>
    <img src="assets/img/9.1_gamma_model_predictive_ecdf.png" alt="Gamma Model Predictive ECDF" width="500" height="400"/>
    <figcaption> Predictive ECDFs, Gamma Model </figcaption>
</center>
{% endif %}

{{entry[1]}}

{% endif %}
{% endif %}
{% endfor %}