<table class="comparison-table">
{% for row in include.projects %}
  {% if forloop.first %}
    <thead><tr>
      {{ include.projects
      | join: "</th><th>"
      | prepend: "<th>"
      | append: "</th>"
      }}
    </tr></thead>
  {% else %}
    {% assign row_value = site.data.projects[row][include.scenario].scalars
    | where: "Name", include.scalar
    | map: "Value"
    | first
    | default: "N/A"
    %}
    {% tablerow column in include.projects %}
      {% assign column_value = site.data.projects[column][include.scenario].scalars
      | where: "Name", include.scalar
      | map: "Value"
      | first
      | default: "N/A"
      %}
      {% if column == "" %}
        <strong>{{ row }}</strong>
      {% elsif column == row %}
        {{ column_value }}
      {% elsif column_value == "N/A" or row_value == "N/A" %}
        N/A
      {% else %}
        {{ row_value | minus: column_value }}
      {% endif %}
    {% endtablerow %}
  {% endif %}
{% endfor %}
</table>
