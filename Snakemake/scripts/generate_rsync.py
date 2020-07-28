from ftplib import FTP
import pandas as pd
import os
link = snakemake.params.link
#link = 'http://hgdownload.soe.ucsc.edu/goldenPath/hg38/phyloP30way/hg38.30way.phyloP/'


filter_ = snakemake.params.filter
path = snakemake.output.path
#path = 'input/features/hg38/priPhyloP46way/'
ftp = link.split('/', 1)[0]
directory = '/' + link.split('/', 1)[1]

f = FTP(ftp)
f.login()
rsync = 'rsync -a -P rsync://' + ftp
f.cwd(directory)
files = f.nlst()

files =pd.Series(files)[pd.Series(files).str.contains(filter_)]

rsync = 'rsync -a -P rsync://' + ftp + directory + files +' ' + './' + path + ' ;'
p = os.getcwd()+'/' +path
with open(p, 'w') as f:
    f.write("\n".join(str(item) for item in rsync))
