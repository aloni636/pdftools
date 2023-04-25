#!/usr/bin/env python3
"""
Fit multiple pages on the same paper sheet. 
Allow you to cut them afterwords as a scaled down paper (A4 -> A5 etc).
Supports duplex printing.
Dependencies (install with pip): pypdf

Examples:
A4 to A5, double-sided
>>> python Ax-Transform.py input.pdf output.pdf --factor 2 --double-sided --landscape
transforming input.pdf to output.pdf
- factor: 2
- double-sided: True
- orientation: landscape

A4 to A6, single-sided
>>> python Ax-Transform.py input.pdf output.pdf --factor 4 --single-sided --portrait
transforming input.pdf to output.pdf
- factor: 4
- double-sided: False
- orientation: portrait
"""

from pypdf import PdfReader, PdfWriter, Transformation
import argparse

PdfReader.add_form_topname()
# import sys
from sys import argv

if len(argv) == 1 or argv[1] == "--help":
    print(__doc__)

