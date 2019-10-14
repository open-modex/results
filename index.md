---
---

{% assign projects = "" | split: "," %}
{% assign projects = projects | push: "" %}
{% assign scenarios = "" | split: "," %}
{% for d in site.data.data %}
  {% assign projects = projects | push: d[0] %}
  {% for s in d[1] %}
    {% assign scenarios = scenarios | push: s[0] %}
  {% endfor %}
  {% assign scenarios = scenarios | uniq | sort %}
{% endfor %}

# The `open_MODEX` results repository

{% for s in scenarios %}
{% assign title = s | to_integer %}
{% assign title = site.data.meta.scenarios[title]["title"] %}
## {{ title }} Objective Values

{% include comparison.md projects=projects scenario=s %}

{% endfor %}

[The jekyll playground.](playground.html)

