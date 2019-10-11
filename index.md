---
---

# The `open_MODEX` results repository

## One Node Objective Values

{% assign projects = "" | split: "," %}
{% assign projects = projects | push: "" %}
{% for d in site.data.data %}
  {% assign projects = projects | push: d[0] %}
{% endfor %}

[The jekyll playground.](playground.html)

