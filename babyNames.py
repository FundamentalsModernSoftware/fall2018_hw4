# Identify the 100 most commonly used baby names from 1880 through 2016


# glob.glob() returns a list of files whose name matches a given pattern
# Here, that pattern is: files in the babies subdirectory that end with '.txt'
import glob
filenames = glob.glob('./babies/*.txt')
for filename in filenames:
    print(filename + ' is a file containing some baby name data')



