'''

  .o oOOOOOOOo                                            OOOo
   Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
   OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
   OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
   `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
   .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
   OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
  oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
 oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
   Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
   :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
   .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                     `$"  `OOOO' `O"Y ' `OOOO'  o             .
   .                  .     OP"          : o     .
                            :

        CSV to Text Files Script
        Coded by Ryan L. Boyd
        The University of Texas at Austin

*This script was built for Python 3.x
*This script is standalone, and should not need additional packages
'''

import csv
import os
import sys

maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True


#what file would you like to input?
InputFile = "c:/writing/gutenberg/gutenberg2010-text_filtered.csv"

#in what directory would you like to dump the output
OutputDir = "c:/writing/gutenberg/text/"



if OutputDir.endswith("/") == False:
        OutputDir += "/"
if not os.path.exists(OutputDir):
    os.makedirs(OutputDir)

#depending on your input file, you might need to add an encoding
#such as 'utf-8' after the 'rb'
with open(InputFile, 'r', encoding = 'utf8') as file_in:
    #change the "delimiter" argument to whatever suits your file
    csvreader = csv.reader(file_in, delimiter=',')


    HeaderRow = csvreader.__next__()
    for counter in range(0, len(HeaderRow)):
        print(str(counter) + ": " + HeaderRow[counter])

    Filename_Var = int(input("Variable to use as file name (use the corresponding number): "))
    Text_Var = int(input("Variable to use as file text (use the corresponding number): "))

    
    for row in csvreader:
        Filename_Clean = row[Filename_Var]
        print("Writing file: " + Filename_Clean)
        #depending on your input file, you might need to add an encoding
        #such as 'utf-8' after the 'rb'
        with open(OutputDir + Filename_Clean + ".txt", 'a', encoding='utf8') as OutputFile:
            OutputFile.write(row[Text_Var] + "\r\n")
