#!/usr/bin/env python3
"""
single file script!!!
=====================

universal commandline options:
==============================
pdftools < tool > < --flags ... > --suffix "-{%d}-better" < files ... >  ===>  apply tool with set flags on each file, applying changes to new files with configured suffix
pdftools config suffix "-output-{%d}"  %d=digit

pdftools < tool > < --flags ... > < files ... > --inplace  ===> apply tool with set flags on each file, applying changes inplace 

pdftools < tool > < --flags ... > < file > -o < file >  ===> apply chanegs to new file with custom name

pdftools < tool > < --flags ... > < file > -o < file >  ===> apply chanegs to new file with custom name

# tile multiple pages into 1 page
pdftools tile --factor 2 s1.pdf s2.pdf
pdftools tile --flip-long-side --factor 4 --landscape 
pdftools tile --flip-short-side --factor 2 --landscape

# untile page into multiple pages
pdftools untile --flip-long-side --factor 4 --landscape
pdftools untile --flip-short-side --factor 2 --landscape


with reorder and zip merge all possible permutations are possible:
==================================================================
# merge 2 or more pdfs, default strategy is zip
# for more advanced merging strategies 
pdftools merge --stack < files ... > -o ./merged.pdf

pdftools reorder 3,2,1 --leftover keep --color 
pdftools config color true
pdftools config reorder.confirmation true/false

>>> reorder pages: [3,2,1],[6,5,4],7,8
>>> confirm (y/n):
(color baded on diff from original)
pdftools reorder 1:6,8,7 -y
>>> reorder pages: [1,2,3,4,5,6,8,7]
pdftools reorder 8:1:2,2:8:2 -y
>>> reorder pages: [1,3,5,7,2,4,6,8]
pdftools reorder 1:8:2 --leftover drop
>>> reorder pages: [1,3,5,7]
>>> deleted: 2,4,6,8
>>> confirm (y/n):
pdftools reorder 1:3 -y
>>> cannot reorder partial pdf
>>> leftover: [4]
>>> use --leftover keep or --leftover dropon: portrait
pdftools reorder 1,1,2,2 --allow-duplicates 
>>> reorder pages: [1,1,2,2],[3,3,4,4]

pdftools resources:
- https://stackoverflow.com/questions/56970605/how-to-merge-two-pages-from-a-pdf-file-as-one-page
"""
import argparse
from sys import argv
from tools import tile, concat, reorder

if len(argv) == 1:
    print(__doc__)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# concat
subparser = subparsers.add_parser("concat")
subparser.add_argument("-i", "--input", nargs="+")
subparser.add_argument("-o", "--output", nargs=1)

def args_handler(args:argparse.Namespace):
    concat(args.input, args.output)

subparser.set_defaults(func=args_handler)

parser_tile = subparsers.add_parser("tile")
parser_untile = subparsers.add_parser("untile")
tile.add_untile_subprogram(parser_tile)


