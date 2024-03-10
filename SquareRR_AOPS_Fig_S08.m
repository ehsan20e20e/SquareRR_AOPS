%The code for the research presented in the paper titled "Spectrum prediction and inverse design of all-optical nonlinear plasmonic square ring resonator switches using deep learning

%This code corresponds to the complex refractive index for silver obtained from Johnson and Cristy.
%This code regenerates the Fig. S8 of the paper's Supplementary Information.
%Please cite the paper in any publication using this code.
%% =======================================================================
clc
close all
clear
%%% load dirty data (predicted)
load Johnsonsilver.mat
figure(1)
yyaxis left
plot(Johnsonsilver(1:48,1),Johnsonsilver(1:48,2),'linewidth',2) % plot the transmission spectrum
hold on
ylabel('Real part (blue solid)')
yyaxis right
plot(Johnsonsilver(1:48,1),Johnsonsilver(1:48,3),'linewidth',2, LineStyle='--') % plot the transmission spectrum
ylabel('Imaginary part (red dashed)')
xlabel('Wavelength(nm)')
get(gca,'fontname')  
set(gca,'fontname','times','fontweight','normal') 
set(gca,'fontsize',18)
set(gca,'linewidth',0.85)
title('complex refractive index','fontweight','normal')
grid off
