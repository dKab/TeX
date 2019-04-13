# "Write a program that creates backup copies of important files"

from argparse import ArgumentParser
from datetime import datetime
import tarfile
import os
from glob import glob

parser = ArgumentParser()
parser.add_argument('src', help='''Source directory. If it is not specified current directory \
	will be used as source.''', nargs='?', default=os.getcwd())
parser.add_argument('dest', help='''destination directory -\
	 all important files from source directory will be placed here''',
	 nargs='?', default=None)
args = parser.parse_args()

srcPath = args.src
# get list of important files
files = glob(srcPath + '/**/important*', recursive=True)
files = filter(lambda file: os.path.isfile(file), files)
# create archive in the source directory
archiveName = datetime.now().strftime('%Y-%m-%d') + '.tar.gz'
archivePath = str(os.path.join(archiveName))
tar = tarfile.open(archivePath, 'w:gz')
for file in files:
	tar.add(file, os.path.basename(file), False)
tar.close()
# create destination directory if it doesn't exist already
dest = args.dest
backupDir = dest if dest else os.path.join(os.path.expanduser('~'), 'backup')
if not os.path.exists(backupDir):
	os.makedirs(backupDir)

destPath = os.path.join(backupDir, archiveName)
# move archive to destination directory
os.rename(archivePath, destPath)
