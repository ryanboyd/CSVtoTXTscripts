
#  .o oOOOOOOOo                                            OOOo
#   Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
#   OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
#   OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
#   `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
#   .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
#   OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
#  oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
# oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
#OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
#OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
#   Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
#   :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
#   .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
#                '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
#                     `$"  `OOOO' `O"Y ' `OOOO'  o             .
#   .                  .     OP"          : o     .
#                            :
#-CSV to TXT Files
#-RYAN L. BOYD 
#-UNIVERSITY OF TEXAS AT AUSTIN
#----All input should be in .CSV format


#removes the data if it's already there
remove(DF)


#make sure that your working directory path is the same as the one that your 
#dataset is in -- remember that R needs you to use Forward Slashes (/) instead
#of backslashes (\) in your code for folders
setwd("C:/Directory")

#change the name of the file here to the CSV that you would like to read in
#depending on your region and dataset, you will want to change the "sep" parameter
#to whatever is being used as a delimiter (e.g., a common or semicolon), and you
#may want to remove the "quote" parameter or change it to what is happening in your data
DF <- read.csv("Filename.csv", sep=',', quote='"')


#change these variables to reflect the NAMES of the variables that contain your
#ID variable (this will be your filenames) and you TEXT variable (this will be
#the text that gets put into the corresponding files)
ID_Variable_Name <- "SubjectNumber"
Text_Variable_Name <- "TextResponse"


#this will create a new directory in which your .txt files will be generated
dir.create("Text_Files", showWarnings=F)





#this part of the script loops through your dataset and APPENDS to files using
#whatever you specified for ID_Variable_Name and Text_Variable_Name
#since it APPENDS, you will want to delete the files that it creates and
#start over if there is an issue, otherwise it will keep piling more text
#into the files that already exist

for (i in 1:length(DF[,which(names(DF)==ID_Variable_Name)])){

  #designate the file that we will write to
  FileName = paste("Text_Files/", as.character(DF[i,which(names(DF)==ID_Variable_Name)]), ".txt", sep="")
  
  
  sink(file=FileName, append=T)
  cat(paste(as.character(DF[i,which(names(DF)==Text_Variable_Name)]), "\n", sep=""))
  sink()

  #you can uncomment this next line if you would like to print the progress to the console as it works through the rows in your dataset
  #cat(paste("Wrote to file:", FileName, "\n", sep=" "))
}




