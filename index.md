---
---

<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.20/css/jquery.dataTables.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.js"></script>

<script>
$(document).ready(function() {
    $('table').DataTable( {
        "paging": false,
        "info": false,
        "searching": false
    } );
} );
</script>

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

{% assign scalars = "" | split: "," %}
{% for p in projects %} {% if p != projects.first %}
  {% for s in scenarios %}
    {% assign new = site.data.data[p][s]["scalars"] | map: "Name" %}
    {% assign scalars = scalars | concat: new %}
  {% endfor %}
{% endif %} {% endfor %}
{% assign scalars = scalars | uniq | sort %}

# The `open_MODEX` results repository

{% for s in scenarios %}
{% assign title = s | to_integer %}
{% assign title = site.data.meta.scenarios[title]["title"] %}
## {{ title }} Objective Values

{% include comparison.md projects=projects scenario=s %}

{% endfor %}

[The jekyll playground.](playground.html)

