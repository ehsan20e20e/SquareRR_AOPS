"""
The code for the research presented in the paper titled "Spectrum prediction and inverse design of all-optical nonlinear plasmonic square ring resonator switches using deep learning

This code corresponds to the article's inverse Deep Neural Network (DNN) section.
This code regenerates the Fig. 7b and c of the paper.
Please cite the paper in any publication using this code.
"""
import matplotlib.pyplot as plt 
import pandas as pd 
from matplotlib.font_manager import FontProperties

lum = pd.read_csv("SquareRR_AOPS_Fig_07bc_furthest_predicted.csv", header=None)
g = "\u00D7"

lum=lum.to_numpy()

# plot of transmission of furthest data and predicted data from inverse model using FDTD solver
plt.plot(lum[1:800,0],lum[1:800,6], linewidth=2, color='#ff7f0e')
plt.plot(lum[1:800,0],lum[1:800,13], linewidth=2, linestyle='--', color='#1f77b4')
plt.title('Results of inverse design for through port', fontname='Times New Roman', fontsize=18, loc='center')
plt.xlabel('Wavelength (nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=14)
plt.yticks(fontfamily='Times New Roman', fontsize=14)
font_prop = FontProperties(family="Times New Roman", size=14)
plt.legend(['Desierd (55,55,55,24,24)', 'DL (54.2,55.1,55.7,23.9,24.4)'], prop=font_prop)
plt.show()

plt.plot(lum[1:800,0],lum[1:800,7], linewidth=2, color='#ff7f0e')
plt.plot(lum[1:800,0],lum[1:800,14], linewidth=2, linestyle='--', color='#1f77b4')
plt.title('Results of inverse design for drop port', fontname='Times New Roman', fontsize=18, loc='center')
plt.xlabel('Wavelength (nm)', fontname='Times New Roman', fontsize=18)
plt.ylabel('Transmission', fontname='Times New Roman', fontsize=18)
plt.xticks(fontfamily='Times New Roman', fontsize=14)
plt.yticks(fontfamily='Times New Roman', fontsize=14)
font_prop = FontProperties(family="Times New Roman", size=14)
plt.legend(['Desierd (55,55,55,24,24)', 'DL (54.2,55.1,55.7,23.9,24.4)'], prop=font_prop)
plt.show()
