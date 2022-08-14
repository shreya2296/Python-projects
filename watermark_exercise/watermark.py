#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:47:22 2022

@author: shreyasanjayshirodkar
"""
# Importing libraries
import PyPDF2

# reading merged pdf in binary mode
template = PyPDF2.PdfFileReader(open('merged-pdf.pdf', 'rb'))
# reading watermark pdf in binary mode
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb')) 

# output with PdfFileWriter
output = PyPDF2.PdfFileWriter()

# using for loop to set range of pdf pages
for i in range(template.getNumPages()):
    # get each page
    page = template.getPage(i)
    # watermark pages
    page.mergePage(watermark.getPage(0))
    # add pages to output
    output.addPage(page)
    
# write output file
with open('watermarked.pdf', 'wb') as file:
    output.write(file)


    
    
