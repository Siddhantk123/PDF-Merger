# package used : PYPDF2 , os

# some questions that this video may answer 

# python pdfminer
# python pdf merge
# python pdf to text
# python pdf reader
# python pdf data extraction
# pdf python tutorial
# pdf python extract
# pdf python extract text
# how to read pdf file using python
# how to create pdf using python
# python pdf creation
# python projects
# python creative projects

from PyPDF2 import PdfFileMerger
import os

#object creation
merger=PdfFileMerger()

#run a loop to take all the pdf file from the file
dir=os.listdir() #this is returning a list

#print(dir) 


for items in dir: #if we donot specify the path, it will cosider the current directory
    
    if items.endswith('.pdf'):

        merger.append(items)    

merger.write("MaC.pdf") 
merger.close()

