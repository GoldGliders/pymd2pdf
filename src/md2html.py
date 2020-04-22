"""
This script is for converting Markdown to HTML.
"""
import sys
import markdown


# enable math notation using javascript
math = r'''<script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>
<script type="text/x-mathjax-config">
 MathJax.Hub.Config({
 tex2jax: {
 inlineMath: [["\\(","\\)"] ],
 displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
 }
 });
</script>'''


def main(IN, OUT, CSS):
    # make the input file to one str &
    # make it escaped: "&", "<", ">", '"' and "'" for html.
    with open(IN, "r") as f:
        lines = "".join(f.readlines()) \
            .replace("&", "&amp;")\
            .replace("<", "&lt;")\
            .replace(">", "&gt;")\
            .replace('"', "&quot;")\
            .replace("'", "&#39;")

    md = markdown.Markdown()
    body = md.convert(lines)
    # make the str to html style
    html = "".join([
        '<html lang="ja"><meta charset="utf-8"><body>',
        '<link rel="stylesheet" type="text/css" href="{}">\n'.format(CSS),
        math,
        body,
        '</body></html>'
        ])
    with open(OUT, "a") as f:
        f.write(html)


if __name__ == "__main__":
    IN = sys.argv[1]
    OUT = sys.argv[2]
    CSS = sys.argv[3]
    main(IN, OUT, CSS)
