#!/usr/bin/env python2

"""
Pandoc filter to process code blocks with class "graphviz" into
graphviz-generated images.

add Figure: ... below the code block to make it a figure

```graphviz
graph {
    a -- b
}
```
Figure: a nice graph

"""

import pygraphviz
import hashlib
import os
import sys
from pandocfilters import toJSONFilter, Str, Para, Image


def sha1(x):
    return hashlib.sha1(x).hexdigest()

imagedir = "graphviz-images"

lastgraph = None

def graphviz(key, value, format, meta):
    global lastgraph
    if key == 'Para':
        paragraph = value
        if lastgraph is not None:
            src = lastgraph
            lastgraph = None
            if paragraph[0]['t'] == 'Str' and paragraph[0]['c'] == 'Figure:':
                # make it a figure
                paragraph.pop(0) # remove 'Figure: ' string
                if paragraph[0]['t'] == 'Space':
                    paragraph.pop(0)
                return Para([Image(paragraph, [src, "fig:"])])
            # just a normal paragraph, don't make it a figure
            return [Para([Image([Str('graph')], [src, ""])]), Para(value)]

    if key == 'CodeBlock':
        [[ident, classes, keyvals], code] = value
        if "graphviz" in classes:
            titles = [v for [k,v] in keyvals if k == 'title']
            if len(titles) == 1:
                caption = titles[0]
                tit = "fig:"
            else:
                caption = "graph"
                tit = ""
            filename = sha1(code)
            G = pygraphviz.AGraph(string=code)
            if format == "html":
                filetype = "png"
            elif format == "latex":
                filetype = "pdf"
            else:
                filetype = "png"
            alt = Str(caption)
            src = imagedir + '/' + filename + '.' + filetype
            if not os.path.isfile(src):
                try:
                    os.mkdir(imagedir)
                    sys.stderr.write('Created directory ' + imagedir + '\n')
                except OSError:
                    pass
                G.draw(src, args='-Gmargin=0', prog='dot')
                sys.stderr.write('Created image ' + src + '\n')
            lastgraph = src
            return [] # delete for now, will be readded after parsing 'Figure: '

if __name__ == "__main__":
    toJSONFilter(graphviz)
