<script>

const scalarData = {
  {% for s in include.scenarios %}
    '{{ s }}': {
      {% for name in include.scalars %}
        '{{ name }}': [
          {% for row in include.projects %}
            {% assign row_value = site.data.projects[row][s].scalars
            | where: "Name", name
            | map: "Value"
            | first
            | default: "N/A"
            %}
            {% if forloop.first %}{% else %}
              [
              {% for column in include.projects %}
                {% assign column_value = site.data.projects[column][s].scalars
                | where: "Name", name
                | map: "Value"
                | first
                | default: "N/A"
                %}
                {% if forloop.first %}
                '{{ row }}'
                {% elsif column == row %}
                '{{ column_value }}'
                {% elsif column_value == "N/A" or row_value == "N/A" %}
                'N/A'
                {% else %}
                '{{ row_value | minus: column_value }}'
                {% endif %}
                {% unless forloop.last %},{% endunless %}{% endfor %}
              ]
          {% endif %}
          {% unless forloop.last or forloop.first %},{% endunless %}{% endfor %}
        ]
      {% unless forloop.last %}, {% endunless %}{% endfor %}
    }
  {% unless forloop.last %},{% endunless %}{% endfor %}
};

const scalars = [
  {% for s in include.scalars %}
    '{{ s }}'
  {% unless forloop.last %},{% endunless %}{% endfor %}
];

</script>

