import os
import os.path
import sys

def rename_files(indir, outdir):

	files = os.listdir(indir)
	print(len(files))

	for index, oldname in enumerate(files):
		newname = '{0:06}_1.jpg'.format(index)
		oldpath = indir + '/' + oldname
		newpath = outdir + '/' + newname 

		#cmd = 'mv {0} {1}'.format(oldpath, newpath)
		cmd = 'convert {0} -resize 800x600 {1}'.format(oldpath, newpath)
		print(cmd)
		os.system(cmd)


if __name__ == '__main__':		

	if len(sys.argv) < 3:
		print('python3 rename.py indir outdir')

	indir = sys.argv[1]
	outdir = sys.argv[2]
	rename_files(indir, outdir)

