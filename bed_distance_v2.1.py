#!/usr/bin/python
from sys import argv
import os,sys
"""
  This program will compute the distance between bed annotations in a file.
  The distance is calculated using end2 - start1 after sorting.
  The output include 
    chr
    bed_start
    bed_end
    distance to the left annotation
    distance to the right annotation
"""

if len(sys.argv) < 1:
  print "python "+argv[0]+" <bed file>"
  sys.exit()
  
bed_file = argv[1]

count = len(open(bed_file,'r').readlines())

f = open(bed_file,'r')

pre_2 = ""
pre_1 = ""
#pre_2
#pre_1
#current
n = 0

for line in f:
    n += 1
    line.strip()
    ln = line.split()
      
    if n == 1:
      pass
    
    elif n == 2:
      if ln[0] != pre_1[0]:
        dist1 = "NA"
        dist2 = "NA"
        print "%s\t%s\t%s\t%s\t%s" % (pre_1[0],pre_1[1],pre_1[2],str(dist1),str(dist2))
        
    elif n == 3 and ln[0] != pre_1[0]:
        if pre_1[0] == pre_2[0]:
          dist1 = "NA"
          dist2 = int(pre_1[1])-int(pre_2[2])
          print "%s\t%s\t%s\t%s\t%s" % (pre_1[0],pre_1[1],pre_1[2],str(dist1),str(dist2))
          
          dist1 = int(pre_1[1])-int(pre_2[2])
          dist2 = "NA"
          print "%s\t%s\t%s\t%s\t%s" % (pre_1[0],pre_1[1],pre_1[2],str(dist1),str(dist2))
        else:  
          dist1 = "NA"
          dist2 = "NA"
          print "%s\t%s\t%s\t%s\t%s" % (pre_1[0],pre_1[1],pre_1[2],str(dist1),str(dist2))
      
    elif ln[0] == pre_1[0] and ln[0] == pre_2[0]:
      if n == 3:
        dist1 = "NA"
        dist2 = int(pre_1[1]) - int(pre_2[2])
        print "%s\t%s\t%s\t%s\t%s" % (pre_2[0],pre_2[1],pre_2[2],str(dist1),str(dist2))
     
      dist1 = int(pre_1[1])-int(pre_2[2])
      dist2 = int(ln[1])- int(pre_1[2])
      print "%s\t%s\t%s\t%s\t%s" % (pre_1[0],pre_1[1],pre_1[2],str(dist1),str(dist2))
      
    elif ln[0] == pre_1[0] and ln[0] != pre_2[0]:
      dist1 = "NA"
      dist2 = int(ln[1])- int(pre_1[2])
      print "%s\t%s\t%s\t%s\t%s" % (pre_1[0],pre_1[1],pre_1[2],str(dist1),str(dist2))
      
    elif ln[0] != pre_1[0]:
      if pre_1[0] == pre_2[0]:
        dist1 = int(pre_1[1])-int(pre_2[2])
      else:
        dist1 = "NA"
        
      dist2 = "NA"
      print "%s\t%s\t%s\t%s\t%s" % (pre_1[0],pre_1[1],pre_1[2],str(dist1),str(dist2))
  
      
    if n == count:
      if ln[0] == pre_1[0]:
        dist1 = int(ln[1])-int(pre_1[2])
      else:
        dist1 = "NA"
        
      dist2 = "NA"
      print "%s\t%s\t%s\t%s\t%s" % (ln[0],ln[1],ln[2],str(dist1),str(dist2))

    pre_2=pre_1
    pre_1=ln
    
