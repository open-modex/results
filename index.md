---
---

{% assign projects = "" | split: "," %}
{% assign scenarios = "" | split: "," %}
{% for d in site.data.projects %}
  {% assign projects = projects | push: d[0] %}
  {% for s in d[1] %}
    {% assign scenarios = scenarios | push: s[0] %}
  {% endfor %}
  {% assign scenarios = scenarios | uniq | sort %}
{% endfor %}
{% assign projects = projects | sort | unshift: "" %}

{% assign scalars = "" | split: "," %}
{% for p in projects %} {% if p != projects.first %}
  {% for s in scenarios %}
    {% assign new = site.data.projects[p][s]["scalars"] | map: "Name" %}
    {% assign scalars = scalars | concat: new %}
  {% endfor %}
{% endif %} {% endfor %}
{% assign scalars = scalars | uniq | sort %}

# The `open_MODEX` results repository

{% include scalar-data.js projects=projects scenarios=scenarios scalars=scalars %}
{% include tables.html projects=projects scenarios=scenarios scalars=scalars %}

---

[The jekyll playground.](playground.html)

