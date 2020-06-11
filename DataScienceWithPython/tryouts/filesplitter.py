
import os
import sys

def getfilesize(filename):
   with open(filename,"rb") as fr:
       fr.seek(0,2) # move to end of the file
       size=fr.tell()
       print("getfilesize: size: %s" % size)
       return size

def splitfile(filename, splitsize):
   # Open original file in read only mode
	if not os.path.isfile(filename):
		print("No such file as: \"%s\"" % filename)
		return

	filesize=getfilesize(filename)
   
	with open(filename,"r") as fr:
		orginalfilename = filename.split(".")
		if filesize%splitsize :
			nr_sub = filesize//splitsize + 1
		else:
			nr_sub = filesize//splitsize
		
		print (nr_sub)
	
		for i in range(nr_sub):
			with open(orginalfilename[0]+"_{id}.".format(id=str(i))+orginalfilename[1],"a") as fw:
		
				sizenotreached = 1
		
				while(sizenotreached):
			
					data = fr.readline(100)
					fw.writelines(data)
					print("written 100 lines")
					print(fr.tell())
					if (fr.tell()> splitsize):
						sizenotreached = 0
				

				
				
if __name__ == "__main__":
   if len(sys.argv) < 3: print("Filename or splitsize not provided: Usage:     filesplitter.py filename splitsizeinkb ")
   else:
       filesize = int(sys.argv[2]) * 1000 #make into kb
       filename = sys.argv[1]
       splitfile(filename, filesize)
			
			