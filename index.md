---
---

# The `open_MODEX` results repository

## {{ site.data.meta.scenarios[1]["title"] }} Objective Values

{% assign projects = "" | split: "," %}
{% assign projects = projects | push: "" %}
{% for d in site.data.data %}
  {% assign projects = projects | push: d[0] %}
{% endfor %}

### Projects

{% assign projects = projects | sort %}
{% for p in projects %}
  {% if p != "" %} * {{p}} {% endif %}
{% endfor %}

### Comparison

{% include comparison.md projects=projects %}

[The jekyll playground.](playground.html)

