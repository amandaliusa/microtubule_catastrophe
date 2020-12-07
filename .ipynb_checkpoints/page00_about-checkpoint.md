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
## {{entry[0]}}
{{entry[1]}}
{% endif %}
{% endif %}
{% endfor %}