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

{% if entry[0] != 'fig1' and entry[0] != 'fig2' and entry[0] != 'fig3' and entry[0] != 'fig4'
and entry[0] != 'fig5' and entry[0] != 'fig6' and entry[0] != 'fig7' and entry[0] != 'fig8' and entry[0] != 'fig9'
and entry[0] != 'fig10' and entry[0] != 'fig11' and entry[0] != 'fig12'%}
## {{entry[0]}}
{% endif %}

{% if entry[0] == 'fig1' %}
<center>
    {% include fig1.html %}
    <figcaption> Figure 1: ECDF of Time to Catastrophe for Labeled vs Unlabeled Tubulin </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig2' %}
<center>
    {% include fig2.html %}
    <figcaption> Figure 2: ECDFs of Time to Catastrophe with Different beta2/beta1 ratios </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig3' %}
<center>
    {% include fig3.html %}
    <figcaption> Figure 3: Analytical vs Simulated ECDF of Time to Catastrophe </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig4' %}
<center>
    {% include fig4.html %}
    <figcaption> Confidence Intervals for Rates, Both Models </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig5' %}
<center>
    {% include fig5.html %}
    <figcaption> Figure 5: QQ Plot, Gamma Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig6' %}
<center>
    {% include fig6.html %}
    <figcaption> Figure 6: QQ Plot, Custom Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig7' %}
<center>
    {% include fig7.html %}
    <figcaption> Figure 7: Predictive ECDFs, Gamma Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig8' %}
<center>
    {% include fig8.html %}
    <figcaption> Figure 8: Predictive ECDFs, Custom Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig9' %}
<center>
    {% include fig9.html %}
    <figcaption> Figure 9: Predictive ECDF Differences, Gamma Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig10' %}
<center>
    {% include fig10.html %}
    <figcaption> Figure 10: Predictive ECDF Differences, Custom Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig11' %}
<center>
    {% include fig11.html %}
    <figcaption> Figure 11: Confidence Intervals for Alpha at Different Concentrations, Gamma Model </figcaption>
</center>
{% endif %}

{% if entry[0] == 'fig12' %}
<center>
    {% include fig12.html %}
    <figcaption> Figure 12: Confidence Intervals for Beta at Different Concentrations, Gamma Model </figcaption>
</center>
{% endif %}


{{entry[1]}}

{% endif %}
{% endif %}
{% endfor %}