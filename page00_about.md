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

{% if entry[0] != 'fig5.2a' and entry[0] != 'fig5.2b' and entry[0] != 'fig6.1' and entry[0] != 'fig8.2'
and entry[0] != 'fig9.1a' and entry[0] != 'fig9.1b' and entry[0] != 'fig9.1c' and entry[0] != 'fig9.1d' and entry[0] != 'fig9.1e'
and entry[0] != 'fig9.1f' and entry[0] != 'fig9.1g' and entry[0] != 'fig9.1h'%}
## {{entry[0]}}
{% endif %}

{% if entry[0] == 'fig5.2a' %}
<center>
    {% include 5.2a.html %}
    <figcaption> Figure 2: ECDFs of Time to Catastrophe with Different beta2/beta1 ratios </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig5.2b' %}
<center>
    {% include 5.2b.html %}
    <figcaption> Figure 3: Analytical vs Simulated ECDF of Time to Catastrophe </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig6.1' %}
<center>
    {% include 6.1.html %}
    <figcaption> Figure 1: ECDF of Time to Catastrophe for Labeled vs Unlabeled Tubulin </figcaption>
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
    {% include 9.1a.html %}
    <figcaption> Figure 5: Confidence Intervals for Alpha at Different Concentrations, Gamma Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9.1b' %}
<center>
    {% include 9.1b.html %}
    <figcaption> Figure 6: Confidence Intervals for Beta at Different Concentrations, Gamma Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9.1c' %}
<center>
    {% include 9.1h.html %}
    <figcaption> Figure 7: Predictive ECDF Differences, Custom Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9.1d' %}
<center>
    {% include 9.1g.html %}
    <figcaption> Figure 8: Predictive ECDFs, Custom Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9.1e' %}
<center>
    {% include 9.1d.html %}
    <figcaption> Figure 9: QQ Plot, Custom Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9.1f' %}
<center>
    {% include 9.1f.html %}
    <figcaption> Figure 10: Predictive ECDF Difference, Gamma Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9.1g' %}
<center>
    {% include 9.1e.html %}
    <figcaption> Figure 11: Predictive ECDFs, Gamma Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9.1h' %}
<center>
    {% include 9.1c.html %}
    <figcaption> Figure 12: QQ Plot, Gamma Model </figcaption>
</center>
{% endif %}

{{entry[1]}}

{% endif %}
{% endif %}
{% endfor %}