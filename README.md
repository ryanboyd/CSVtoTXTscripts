# CSVtoTXTscripts
Get text out of CSV files and into TXT files

## Use
This is a pretty basic collection of scripts that will dump texts out of CSV files and into TXT files. If you're looking for a GUI-driven program to do the same, you might want to check out EZPZTXT: https://www.ryanboyd.io/software/ezpztxt

### Python Scripts

#### CSV to Text.py
This script will prompt you for the columns to be used as filenames (usually some kind of subject/participant identifier),
as well as which column contains your text samples.

#### CSV to Text - 20000 Files in Subfolders.py
This script does the same as the one above it, but puts all .txt files into subfolders with a maximum number 
of files in any given folder set to 20,000. Use this for extremely large datasets so that you don't get folder bloat.

#### Python 3.x Scripts
Both of the scripts above have python 3.x versions (noted with - py3 in the filenames). The python 3.x versions are recommended, as they are much better at handling text encodings.

### R Scripts

#### CSV to Text Files.R
The "R" equivalent to the python script above.
