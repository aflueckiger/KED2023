#!/bin/bash

##################################################
### Assignment 1
### Seminar: The ABC of Computational Text Analysis
### University of Lucerne
##################################################


### Task 1: Organize your project

# create directory with the required name 
mkdir KED2023_exercise_1

# change into the created directory
cd KED2023_exercise_1

# print path to current directory (e.g., ~/KED2023/KED2023_exercise_1)
pwd

# create all the subfolders at once. The argument -p allows to create subfolders before the top-level folder exists.
mkdir -p reports src data/raw data/interim

# use the given commands to create various empty files
# hint: you need to be in the folder "KED2023_exercise_1", in which "data" and its subfolder "raw" exists already
touch data/raw/speeches_{2019..2023}_{a..z}.txt 
touch data/raw/text_{2019..2023}_{1..12}_{1..30}.txt

# change into the interim directory
cd data/interim

# Use expansion to create all the directories with the name of the year at once.
# Hint: run echo {2019..2023} to see to what the expression expands
mkdir {2019..2023}

# change into the folder raw (one folder up into the main directory and then into the folder raw)
cd ../raw

# Copy the newly created files into the corresponding folders using wildcards.
# Hint: you can use multiple wildcards at once. Each wildcard matches any sequence of characters. 
# Thus, all files with a particular year in its name go into the folder of the corresponding year.
cp *2019*.txt ../interim/2019
cp *2020*.txt ../interim/2020
cp *2021*.txt ../interim/2021
cp *2023*.txt ../interim/2023

# change back to main folder (~ is a shortcut for your home directory, e.g. /home/alex)
cd ~/KED2023/KED2023_exercise_1

# show the folder structure (incl. all files) of the current directory indicated by a period
tree .

### Task 2: Report on file collection

## Task 2.1
# Navigate to the respective directory using `cd` and print the absolute path of this directory using `pwd`.
# Windows cd /mnt/c/Users/YOUR_USERNAME 
# macOS cd /home/YOUR_USERNAME
cd /home/alex/Documents
pwd

## Task 2.2
# List all the PDF files of the current directory and its subfolders using `ls``. 
# Pass the output of the previous command to the `>` operator to write the output directly into a new file.
# While the use of `**` instructs `ls` to match files in any subdirectory, the single `*` is a wildcard that matches an arbitrary filename or directory.
# Check again the post for more information: 
# https://stackoverflow.com/questions/28176590/what-do-double-asterisk-wildcards-mean
ls **/*.pdf > list_of_pdfs.txt 

## Task 2.2
# `ls` lists any pdf files using the same wildcard as above. The argument -t changes the alphabetic order to a chronological order, from new to old.
# After piping, `tail -n 1` retains only the very last line.
# This final output is then written into a file using again the `>` operator
ls -lt **/*.pdf | tail -n 1 > oldest_pdf_file.txt


### Your feedback
