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

*This script was built for Python 2.7
*This script is standalone, and should not need additional packages
'''

import csv
import os
import codecs

#what file would you like to input?
InputFile = "C:/Dataset.csv"

#in what directory would you like to dump the output
OutputDir = "C:/Output"



if OutputDir.endswith("/") == False:
        OutputDir += "/"
if not os.path.exists(OutputDir):
    os.makedirs(OutputDir)

#depending on your input file, you might need to add an encoding
#such as 'utf-8' after the 'rb'
with codecs.open(InputFile, 'rb') as file_in:
    #change the "delimiter" argument to whatever suits your file
    csvreader = csv.reader(file_in, delimiter=',')


    HeaderRow = csvreader.next()
    for counter in range(0, len(HeaderRow)):
        print(str(counter) + ": " + HeaderRow[counter])

    Filename_Var = int(raw_input("Variable to use as file name (use the corresponding number): "))
    Text_Var = int(raw_input("Variable to use as file text (use the corresponding number): "))

    
    for row in csvreader:
        Filename_Clean = "".join([c for c in row[Filename_Var] if c.isalpha() or c.isdigit() or c==' ']).rstrip()
        print("Writing file: " + Filename_Clean)
        #depending on your input file, you might need to add an encoding
        #such as 'utf-8' after the 'rb'
        with codecs.open(OutputDir + Filename_Clean + ".txt", 'ab+') as OutputFile:
            OutputFile.write(row[Text_Var] + "\n")
