import pandas as pd
import glob
import os


def concatenate(indir=r"C:\Program Files\Docker Toolbox\product\DockerAssignment2",
                outfile=r"C:\Program Files\Docker Toolbox\product\DockerAssignment2\concatenated.csv"):
    os.chdir(indir)
    fileList = glob.glob('*.csv')
    dfList = []
    for filename in fileList:
        print(filename)
        df = pd.read_csv(filename, header=None)
        dfList.append(df)
    concatdf = pd.concat(dfList, axis=0)
    concatdf.to_csv(outfile, index=None)

concatenate()

words = pd.read_csv(r"C:\Program Files\Docker Toolbox\product\DockerAssignment2\concatenated.csv")

words.duplicated()

keywords = words.drop_duplicates(keep = 'first')

wordsfinal = pd.read_csv(r"C:\Program Files\Docker Toolbox\product\DockerAssignment2\FinalWordlist.csv")
wordsfinal.head()