# coding=utf-8

import zipfile,os


CURRENT_PATH = os.path.dirname(os.path.realpath(__file__)) + '/'





if __name__ == '__main__':
	zipFileFullpath = os.path.join(CURRENT_PATH,"myZipFile.zip")
	z = zipfile.ZipFile(zipFileFullpath, "r")
	for filename in z.namelist():
		print filename
		# bytes = z.read(filename)
		# print len(bytes)