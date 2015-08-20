#!/usr/bin/env python2

"""
Pandoc filter to process images with extension '.dot' through graphviz 
"""

import pygraphviz
import hashlib
import os
import sys
from pandocfilters import toJSONFilter, Str, Para, Image

def run_graphviz(filename, format):
    G = pygraphviz.AGraph(filename)
    filetype = "png" # format = e.g. html
    if format == "latex":
        filetype = "pdf"
    output = filename[0:-4] + "_dot." + filetype
    if os.path.isfile(output) and os.stat(output).st_mtime > os.stat(filename).st_mtime:
        sys.stderr.write('Skipping ' + output + '\n')
    else:
        G.draw(output, 
            # args='-Gmargin=0',
            prog='dot')
        sys.stderr.write('Created image ' + output + '\n')
    return output


def graphviz(key, value, format, meta):
    global lastgraph
    if key == 'Image':
        [label, [filename, figure]] = value
        if not filename.endswith('.dot'):
            return
        return Image(label, [run_graphviz(filename, format), figure])

if __name__ == "__main__":
    toJSONFilter(graphviz)
