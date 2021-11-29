import glob
import re
import numpy as np

files = glob.glob('*.stl')

for filei in files:
    if '_splitted' in filei:
        continue
    with open(filei, 'r+') as filein, open(filei[:-4] + '_splitted.stl', 'w') as fileout:
        normal_previous = ''
        i = 0
        for num, line in enumerate(filein):
            if line[:5] == 'solid':
                line = line.replace('solid', 'solid Gmsh Surface 1')
            if line[:8] == 'endsolid':
                line = line.replace('endsolid', 'endsolid Gmsh Surface 6')
            if 'facet normal' in line:
                normal = line[13:]
                if line[13:].replace('-0', '0') != normal_previous:
                    print(normal)
                    normal_previous = normal
                    if i != 0:
                        fileout.write('endsolid Gmsh Surface ' + str(i) + "\n" + 'solid Gmsh Surface ' + str(i+1) + "\n")
                    i += 1
            fileout.write(line)
