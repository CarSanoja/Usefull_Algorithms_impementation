import os


path =  '/home/carlos/Descargas/GITHUB/Inference_Project/src/data_collection/mango'
filenames = os.listdir(path)

x = 0 
mango_name = 'mango_'
for filename in filenames:
	print(filename)
	new_name = mango_name + str(x) + '.jpeg'
	print('renaiming..', new_name)
	os.rename( filename , new_name)
	x = x + 1