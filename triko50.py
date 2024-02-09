import numpy as np
import matplotlib.pyplot as plt


with plt.xkcd():
	#definice Lissajous obrazce
	n=np.linspace(0,24*np.pi,1000)	
	m=np.linspace(np.pi/7,20*np.pi,1000)
	r=np.pi*3
	x=np.sin(n+r)
	y=np.sin(m)
	# definice textů 
	fig = plt.figure()
	ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
	ax.set_xlabel('moje pocity')
	ax.set_ylabel('babička řikala')
	ax.annotate(
		'Chvíle, kdy\nto snad manža\ntrochu pochopil',
		xy=(0,0.43), arrowprops=dict(arrowstyle='->'), xytext=(0.1, 0.6))

	ax.annotate(
		'Začala jsem \nmu to jasně a \nstručně vysvětlovat',
		xy=(0,0), arrowprops=dict(arrowstyle='->'), xytext=(-0.5, -0.6))


	fig.text(
		0.5, 0.01,
		'JAK VYSVĚTLIT MANŽELOVI RECETPT NA BABIČČINU BRAMBORAČKU',
		ha='center')

	plt.plot(x,y)

plt.show()

