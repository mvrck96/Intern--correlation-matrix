def linecounter(file):
    fileHandler = open(file, 'r')
    num_lines = sum(1 for line in fileHandler) # counting lines in file
    fileHandler.close()
    return num_lines



def niceheader(file = None, num_lines = None, moment = None):
        print('='*80 + '\n{:<40}'.format(str(file)) +
         '{:^25}'.format('Lines: ' + str(num_lines)) +
         '{:>15}\n'.format('Slice No.:' + str(moment).strip())+ '='*80) # printitng header
