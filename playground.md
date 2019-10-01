---
---

# A Jekyll Playground

Apparently, there is a way to traverse the whole repository by using the
[`site.static_files`][0] variable, which is global to Jekyll.

Behold what:

<script>
// https://dev-notes.eu/2015/11/js-variables-in-markdown-includes/

var filepaths = [

  {% for file in site.static_files %}
      '{{ file.path }}'{% unless forloop.last %},{% endunless %}
  {% endfor %}
];

console.log(filepaths);

</script>

{% raw %}
```liquid
{% for f in site.static_files %}
`{{f.name}}`:

  * `Path`: [.{{f.path}}](.{{f.path}})
  * `Mod.`: {{f.modified_time}}

{% endfor %}
```
{% endraw %}

will create:

{% for f in site.static_files %}
`{{f.name}}`:

  * `Path`: [.{{f.path}}](.{{f.path}})
  * `Mod.`: {{f.modified_time}}

{% endfor %}

[0]: https://jekyllrb.com/docs/static-files/

<script>
// https://stackoverflow.com/questions/3038901/how-to-get-the-response-of-xmlhttprequest

var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (xhr.readyState == XMLHttpRequest.DONE) {
        alert(xhr.responseText);
    }
}
xhr.open('GET', 'oemof/1/objective.csv', true);
xhr.send(null);

</script>
