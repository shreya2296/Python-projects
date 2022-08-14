#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:47:22 2022

@author: shreyasanjayshirodkar
"""

# Importing libraries
import PyPDF2
import sys

# initializing argument
input = sys.argv[1:]

# Function to merge pdfs
def pdf_merge(pdf_list):
    # pdf object
    merger = PyPDF2.PdfFileMerger()
    # merging pdf using for loop
    for pdf in pdf_list: 
        print(pdf)
        merger.append(pdf)
    merger.write("merged-pdf.pdf")
    
# calling function   
pdf_merge(input)
    


    
    
