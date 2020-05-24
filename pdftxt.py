# -*- coding: utf-8 -*-
import subprocess
import os




#pdf1 = r"C:\\Users\\daniyar.abdimomunov\\Desktop\\A-Case-Study-for-Blockchain-in-Manufacturing---FabRec---A-P_2018_Procedia-Ma.pdf"
#txt = r"C:\\Users\\daniyar.abdimomunov\\Desktop\\A-Case-Study-for-Blockchain-in-Manufacturing---FabRec---A-P_2018_Procedia-Ma.txt"
#pdftotext = r"C:\\Users\\daniyar.abdimomunov\\Desktop\\xpdf-tools-win-4.02\\bin64\\pdftotext.exe"
#file = open( txt, "w")

#pdfs = os.listdir(r"C:\Users\daniyar.abdimomunov\Körber Logistics Systems GmbH\Bahke, Andreas Dr. - 02_K.Digital\17_Team\07_Thesis\01_Daniyar\01_Thesis Proposal\big_data_manlog_pdf\pdfs done")

#for pdf in pdfs:
#    print(pdf[:-3])
#cmd = [pdftotext, pdf1, txt]
#response = subprocess.check_output(cmd, 
#                shell=True,
#                stderr=subprocess.STDOUT)
#file.close()


pdftotext = r"C:\Users\daniyar.abdimomunov\xpdf-tools-win-4.02\bin64\pdftotext.exe"
source = r"C:\Users\daniyar.abdimomunov\Desktop\pdfs"
pdfs = os.listdir(source)

for pdf1 in pdfs:
    txt = source + "\\" + pdf1[:-3] + "txt"
    pdf = source + "\\" + pdf1
    txtfile = open(txt, "w")
    cmd = [pdftotext, pdf, txt]
    response = subprocess.check_output(cmd, 
                shell=True,
                stderr=subprocess.STDOUT)
    txtfile.close()
