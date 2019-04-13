# "Write a program that creates backup copies of important files"

from argparse import ArgumentParser
from pathlib import Path
from datetime import datetime
import tarfile

parser = ArgumentParser()
parser.add_argument('src', help='''Source directory. If it is not specified current directory \
	will be used as source.''', nargs='?', default='.')
parser.add_argument('dest', help='''destination directory -\
	 all important files from source directory will be placed here''',
	 nargs='?', default=None)
args = parser.parse_args()

srcPath = Path(args.src)
# get list of important files
files = [x for x in srcPath.glob('**/important*') if not x.is_dir()]
# create archive in the source directory
archiveName = datetime.now().strftime('%Y-%m-%d') + '.tar.gz'
archivePath = str(srcPath.joinpath(archiveName))
tar = tarfile.open(archivePath, 'w:gz')
for file in files:
	tar.add(str(file), file.name, False)
tar.close()
# create destination directory if it doesn't exist already
dest = args.dest
backupDir = Path(dest) if dest else Path.home() / 'backup'
if not backupDir.exists():
	backupDir.mkdir(0o777, parents=True)

destPath = backupDir / archiveName
# move archive to destination directory
archive = Path(archivePath)
archive.rename(destPath)
