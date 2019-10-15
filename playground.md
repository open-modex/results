---
---

# A Jekyll Playground

## Nested Loops

Nested looping is possible. But in order to demonstrate this, we first
have to have something to loop over. The following [`Liquid`][0] code
generates a list containing the names of the immediate subdirectories of
the `"data"` subdirectory of the `data_dir` directory:

{% raw %}
```liquid
{% assign projects = "" | split: "," %}
{% for d in site.data.projects %}
  {% assign projects = projects | push: d[0] %}
{% endfor %}
```
{% endraw%}

{% assign projects = "" | split: "," %}
{% for d in site.data.projects %}
  {% assign projects = projects | push: d[0] %}
{% endfor %}

Once we have this list, which, due to the repository structure, also
contains the list of project names, we can demonstrate how to generate
pairs of project names with a nested loop. Here's what the following
code:

{% raw %}
```liquid
{% for p in projects %}
  {% for q in projects %}
  * {{p}} <-> {{q}}
  {% endfor %}
{% endfor %}
```
{% endraw%}

outputs when interpreted by `Liquid`:

{% for p in projects %}
  {% for q in projects %}
  * {{p}} <-> {{q}}
  {% endfor %}
{% endfor %}


## Traversing the Repository

Apparently, there is a way to traverse the whole repository by using the
[`site.static_files`][1] variable, which is global to Jekyll.

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

[0]: https://shopify.github.io/liquid/
[1]: https://jekyllrb.com/docs/static-files/

<script>
// https://stackoverflow.com/questions/3038901/how-to-get-the-response-of-xmlhttprequest

var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (xhr.readyState == XMLHttpRequest.DONE) {
        console.log(xhr.responseText);
    }
}
xhr.open('GET', 'data/oemof/1/scalars.csv', true);
xhr.send(null);

</script>
