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
    {% assign row_value = site.data.data[row]["1"].scalars
    | where: "Name", "objective"
    | map: "Value"
    | first
    | default: "N/A"
    %}
    {% tablerow column in projects %}
      {% assign column_value = site.data.data[column]["1"].scalars
      | where: "Name", "objective"
      | map: "Value"
      | first
      | default: "N/A"
      %}
      {% if column == "" %}
        <strong>{{ row }}</strong>
      {% else %}
        {{ row_value | minus: column_value }}
      {% endif %}
    {% endtablerow %}
  {% endif %}
{% endfor %}
</table>

[The jekyll playground.](playground.html)

