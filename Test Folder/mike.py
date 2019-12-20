import numpy as np 

for i in range(100, 1000, 1):
	print(i)
	i = i*i*i
	for x in range(0, 1000,1):
		x = x*x*x
		for z in range(0, 1000, 1):
			#print(z)
			z= z*z*z
			if i > 0:
				if z > 0:
					if x >0:
						if i == (z + x):
							print(x, z, i)


