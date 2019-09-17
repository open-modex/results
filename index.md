---
---

# The `open_MODEX` results repository

Apparently, there is a way to traverse the whole repository by using the
[`site.static_files`][0] variable, which is global to Jekyll.

Behold what:

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
