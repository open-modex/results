---
---

# The `open_MODEX` results repository

## One Node Objective Values

{% assign projects = "" | split: "," %}
{% assign projects = projects | push: "" %}
{% for d in site.data.data %}
  {% assign projects = projects | push: d[0] %}
{% endfor %}

### Projects

{% assign projects = projects | sort %}
{% for p in projects  %}
  {% if p != "" %} * {{p}} {% endif %}
{% endfor %}

### Comparison

<table>
{% for row in projects %}
  {% if forloop.first %}
    <thead><tr>
      {{ projects | join: "</th><th>" | prepend: "<th>" | append: "</th>" }}
    </tr></thead>
  {% else %}
    {% tablerow column in projects %}
      {% if column == "" %}
        <strong>{{ row }}</strong>
      {% else %}
        {% assign rvalue = site.data.data[row]["1"].scalars
           | where: "Name", "objective" | map: "Value" | first
        %}
        {% assign cvalue = site.data.data[column]["1"].scalars
           | where: "Name", "objective" | map: "Value" | first
        %}
        {{ rvalue | minus: cvalue }}
      {% endif %}
    {% endtablerow %}
  {% endif %}
{% endfor %}
</table>

[The jekyll playground.](playground.html)

