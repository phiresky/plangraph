#!/usr/bin/env python2

"""
Pandoc filter to process code blocks with class "graphviz" into
graphviz-generated images.
"""

import pygraphviz
import hashlib
import os
import sys
from pandocfilters import toJSONFilter, Str, Para, Image


def sha1(x):
    return hashlib.sha1(x).hexdigest()

imagedir = "graphviz-images"


def graphviz(key, value, format, meta):
    if key == 'CodeBlock':
        [[ident, classes, keyvals], code] = value
        caption = "caption"
        if "graphviz" in classes:
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
            tit = ""
            return Para([Image([alt], [src, tit])])

if __name__ == "__main__":
    toJSONFilter(graphviz)
