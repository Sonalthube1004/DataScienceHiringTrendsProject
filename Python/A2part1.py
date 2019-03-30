import pandas as pd
import glob
import os


def concatenate(indir=r"C:\Program Files\Docker Toolbox\product\DockerAssignment2", 
                outfile=r"C:\Program Files\Docker Toolbox\product\DockerAssignment2\output1.csv"):
    os.chdir(indir)
    fileList = glob.glob('*.csv')
    dfList = []
    for filename in fileList:
        print(filename)
        df = pd.read_csv(filename, header=None, encoding = "ISO-8859-1", dtype= object)
        

        dfList.append(df)
    concatdf = pd.concat(dfList, axis=0)
    concatdf.to_csv(outfile, index=None)
    
concatenate()

dataset = pd.read_csv(r"C:\Program Files\Docker Toolbox\product\DockerAssignment2\output1.csv", dtype= object)

