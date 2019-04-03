import additional as addit
import numpy as np

files = ['1d(4)_smp_07.tsf', '1d(4)_smp_06.tsf']
slice = ' 265 '
samples = [[] for i in range(len(files))]

print(samples)
#while True:
#    newFile = input()
#newFile = '1d(4)_smp_07.tsf'
#    if newFile == 'stop':
#        break
#files.append(newFile)

for file in files:
    num_lines = addit.linecounter(file) #counting number of lines
    fileHandler = open(file, 'r') #open file
    addit.niceheader(file, num_lines, slice)

    for index in range(0, num_lines):
        currentLine = fileHandler.readline()
        if slice in currentLine:
#            print(currentLine[15:])
            samples[files.index(file)].append(float(currentLine[15:]))
np.set_printoptions(precision=3)
print('='*80)
#print(samples)
#print('='*80)
np_array = np.array([np.array(xi) for xi in samples])
#print(np_array)
#print('='*80)
print(np_array.transpose())

#print(np.corrcoef(np_array.transpose()))
