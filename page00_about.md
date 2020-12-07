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

{% if entry[0] != 'fig' %}
## {{entry[0]}}
{{entry[1]}}
{% endif %}

{% if entry[0] == 'fig' %}

{% for fig in site.data.figures %}

{% if fig.pic == '2.2_ecdfs.png' %}

![fig.desc](fig.pic "ECDFs")

{% endif %}

{% endfor %}

{% endif %}

{% endif %}
{% endif %}
{% endfor %}