# Jinja2 Templating

All of the data files are compiled down to their output formats, in this case HTML.
This is done utilizing the Jinja2 Templating Engine, which is popular in Python web software such as Flask and Django.

The use of templating ensures that we can keep our modules independent and clean.

## Base Notes HTML Template

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>{{content.title}}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/github-markdown.css">
</head>

<style>
    .markdown-body {
        box-sizing: border-box;
        min-width: 200px;
        max-width: 980px;
        margin: 0 auto;
        padding: 45px;
    }

    @media (max-width: 767px) {
        .markdown-body {
            padding: 15px;
        }
    }
</style>

<body>

    <article class="markdown-body">
        {{content.title}}
        {{content.documentID}}
        {{content.author}}
        {{content.last_modified}}
    </article>

    {% for content_block in content.blocks %}
    <article class="markdown-body">
        {{content_block}}
    </article>
    {% endfor %}
    
</body>
</html>
```