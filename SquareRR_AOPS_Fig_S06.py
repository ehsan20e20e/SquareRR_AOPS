"""
The code for the research presented in the paper titled "Spectrum prediction and inverse design of all-optical nonlinear plasmonic square ring resonator switches using deep learning

@authors: Ehsan Adibnia, Majid Ghadrdan and Mohammad Ali Mansouri-Birjandi
Corresponding authors: mansouri@ece.usb.ac.ir and ghadrdan@ece.usb.ac.ir

This code is corresponding to the Forward Deep Neural Network (DNN) section of the article.
This code regenerates the Fig. S6 of the paper.
Please cite the paper in any publication using this code.
"""
import matplotlib.pyplot as plt 
import pandas as pd 
from matplotlib.font_manager import FontProperties

Loss = pd.read_csv("SquareRR_AOPS_Fig_S06.csv")
Loss=Loss.to_numpy()

# fig S6m
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,8], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('[5-10-20-40-80-160-320-160-80-40-20-10-5] FC NN', fontname='Helvetica', fontsize=13, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='Helvetica', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("P2_FigureS6m.png", format="png", dpi=600, bbox_inches="tight")
plt.show()

# fig S6k
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,10], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('[5-10-20-40-80-160-80-40-20-10-5] FC NN', fontname='Helvetica', fontsize=14, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='Helvetica', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("P2_FigureS6k.png", format="png", dpi=600, bbox_inches="tight")
plt.show()

# fig S6i
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,12], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('[5-10-20-40-80-40-20-10-5] FC NN', fontname='Helvetica', fontsize=14, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='Helvetica', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("P2_FigureS6i.png", format="png", dpi=600, bbox_inches="tight")
plt.show()

# fig S6g
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,14], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('[5-10-20-40-20-10-5] FC NN', fontname='Helvetica', fontsize=14, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("P2_FigureS6g.png", format="png", dpi=600, bbox_inches="tight")
plt.show()

# fig S6e
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,16], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('[5-10-20-10-5] FC NN', fontname='Helvetica', fontsize=14, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='Helvetica', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("P2_FigureS6e.png", format="png", dpi=600, bbox_inches="tight")
plt.show()

# fig S6c
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,18], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('[5-10-5] FC NN', fontname='Helvetica', fontsize=14, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='Helvetica', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("P2_FigureS6c.png", format="png", dpi=600, bbox_inches="tight")
plt.show()

# fig S6a
plt.plot(Loss[:,0],Loss[:,6], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,20], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 1 hidden layer', fontname='Helvetica', fontsize=14, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='Helvetica', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("P2_FigureS6a.png", format="png", dpi=600, bbox_inches="tight")
plt.show()

# fig S6n
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,9], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('[5-10-20-40-80-160-320-160-80-40-20-10-5] FC NN', fontname='Helvetica', fontsize=13, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='Helvetica', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("P2_FigureS6n.png", format="png", dpi=600, bbox_inches="tight")
plt.show()

# fig S6l
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,11], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('[5-10-20-40-80-160-80-40-20-10-5] FC NN', fontname='Helvetica', fontsize=14, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='Helvetica', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("P2_FigureS6l.png", format="png", dpi=600, bbox_inches="tight")
plt.show()

# fig S6j
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,13], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('[5-10-20-40-80-40-20-10-5] FC NN', fontname='Helvetica', fontsize=14, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='Helvetica', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("P2_FigureS6j.png", format="png", dpi=600, bbox_inches="tight")
plt.show()

# fig Sh
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,15], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('[5-10-20-40-20-10-5] FC NN', fontname='Helvetica', fontsize=14, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='Helvetica', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("P2_FigureS6h.png", format="png", dpi=600, bbox_inches="tight")
plt.show()

# fig S6f
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,17], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('[5-10-20-10-5] FC NN', fontname='Helvetica', fontsize=14, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='Helvetica', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("P2_FigureS6f.png", format="png", dpi=600, bbox_inches="tight")
plt.show()

# fig S6d
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,19], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('[5-10-5] FC NN', fontname='Helvetica', fontsize=14, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='Helvetica', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("P2_FigureS6d.png", format="png", dpi=600, bbox_inches="tight")
plt.show()

# fig S6b
plt.plot(Loss[:,0],Loss[:,7], linewidth=2, color=((255/255, 127/255, 14/255))) 
plt.plot(Loss[:,0],Loss[:,21], linewidth=2, color=((0/255, 114/255, 189/255)), linestyle='--') 
plt.title('NN with 1 hidden layer', fontname='Helvetica', fontsize=14, loc='center')
plt.xlabel('Wavelength(nm)', fontname='Helvetica', fontsize=14)
plt.ylabel('Transmission', fontname='THelvetica', fontsize=14)
plt.xticks(fontfamily='Helvetica', fontsize=12)
plt.yticks(fontfamily='Helvetica', fontsize=12)
font_prop = FontProperties(family="Helvetica", size=14)
plt.legend(['FDTD', 'DL'], prop=font_prop)
plt.savefig("EP2_FigureS6b.png", format="png", dpi=600, bbox_inches="tight")
plt.show()
