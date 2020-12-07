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

{% if entry[0] != 'fig2.2' %}
## {{entry[0]}}
{% endif %}

{% if entry[0] == 'fig2.2' %}

<center>
    <img src="assets/img/2.2_ecdfs.png" alt="ECDFs of Times to Catastrophe for Labeled vs Unlabeled Tubulin" width="500" height="400"/>
</center>
{% endif %}

{% if entry[0] != 'fig2.2' %}
## {{entry[0]}}
{% endif %}

{% if entry[0] == 'fig2.2' %}

<center>
    <img src="assets/img/2.2_ecdfs.png" alt="ECDFs of Times to Catastrophe for Labeled vs Unlabeled Tubulin" width="500" height="400"/>
</center>
{% endif %}

{{entry[1]}}

{% endif %}
{% endif %}
{% endfor %}