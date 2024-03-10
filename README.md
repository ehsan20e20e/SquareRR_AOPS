# SquareRR_AOPS

![SquareRR_AOPS](https://github.com/ehsan20e20e/SquareRR_AOPS/assets/106914575/89f790e3-0014-4e3d-8859-2e04dee52203)

## Describtion
The provided repository serves as a demonstration of the application of deep learning techniques in the prediction of the spectral response of all-optical plasmonic switches. This repository is based on the extensive research presented in the paper titled "Spectrum_Prediction_and_Inverse_Design_of_All-Optical_Nonlinear_Plasmonic_Square_Ring_Resonator_Switches_Using_Deep_Learning." It has been designed to address inverse design challenges, with a specific focus on the fields of photonics and optics.

#### Table of contents
* [Prerequisites](#Prerequisites)
* [Geting started](#Geting_started)
* * [Forward model](#Forward_model)
  * * *[Figure 4](#Figure_4)
* * [Inverse model](#Inverse_model)
  * * *[Figure 7](#Figure_7) 
* * [Supplementary Information](#Supplementary_Information)
  * * *[Figure S1](#Figure_S1)
  * * *[Figure S2](#Figure_S2)
  * * *[Figure S3](#Figure_S3)
  * * *[Figure S5](#Figure_S5)
  * * *[Figure S6](#Figure_S6) 
#### Instructions
The following guidelines provide detailed instructions for setting up and running a copy of the project on your local machine, thus enabling you to perform testing and development activities. These instructions are tailored to ensure accuracy and completeness in executing the project setup process. Consequently, we recommend that you adhere to them meticulously.
## Prerequisites
In order to execute the MATLAB and Python code, it is imperative to have MATLAB installed on your system. Specifically, for this code, we utilized MATLAB version R2023a, Python version 3.7.13, and Spyder version 5.1.5 within Anaconda version 4.14.0. It must be noted that the project can be completed without these programs, however, without the installation of MATLAB and Python, the ability to compare speed and generate data will be limited.

https://github.com/ehsan20e20e/SquareRR_AOPS/releases/tag/1

https://drive.google.com/drive/folders/12n9jV9eL3ReEAF2YD4dCLRF0pCa51JTy?usp=drive_link

## Geting_started
To utilize the contents of this repository, generating the necessary data for the all-optical switch structure using various FDTD (Finite-Difference Time-Domain) solvers such as Lumerical, RSoft, or MATLAB is crucial. These solvers enable the production and simulation of the optical switch structure, which facilitates the analysis of its performance and characteristics.

The proposed plasmonic switch structure's raw data is available in CSV files. These files have been provided to facilitate the reproduction of the graphs and results presented in this article.

===> Please be advised that there was an error in the input data related to the Drop port. The data was mistakenly entered as negative, which has been rectified in the written code. To ensure the accuracy of the data, we have applied the absolute value function to the input data. We apologize for any inconvenience this may have caused and assure you that we have taken the necessary measures to prevent such errors in the future.

### Forward_model
In order to train the forward model, it is recommended to utilize the Python code provided in the 'SquareRR_AOPS_Forward_model.py' file. To this end, we have generated 147,456 unique examples through FDTD simulations and saved them in the "result_V.csv" file (Please take note of the following information: 18432 out of the total number of examples is sufficient.). As a prerequisite for executing the 'CircularRR_AOPS_Forward_model.py' file, it is essential to obtain the 'result_H.csv' file which constitutes a big data file with a size of 5.7 gigabytes. By following these steps, you can effectively train the forward model and achieve accurate results.

The 'result_V.csv' file can be accessed as a single file through the following link: https://github.com/ehsan20e20e/CircularRR_AOPS/releases/download/untagged-80fe3b94e704169ada0a/result_V.rar

The 'result_V.csv' file (7 parts) can be accessed through the following link: https://drive.google.com/drive/folders/12n9jV9eL3ReEAF2YD4dCLRF0pCa51JTy?usp=drive_link

First part link: https://drive.google.com/file/d/1AcqJO9Qy34U64vmeluImQcEhMb7MNPGP/view?usp=drive_link

second part link: https://drive.google.com/file/d/1IyZfRIT8rBBdbkuAULWjWX0sWpynGatL/view?usp=drive_link

3th part link: https://drive.google.com/file/d/12sdaScipwbH1qMnLSl0erEOm6hB9HGLd/view?usp=drive_link

4th part link: https://drive.google.com/file/d/1R9HOWI5C4JGDUw0pwZd9wpX3vV0L-06k/view?usp=drive_link

5th part link: https://drive.google.com/file/d/1g7PXAXhSXLVsp41bHdyKxCvUy8YYXESo/view?usp=drive_link

6th part link: https://drive.google.com/file/d/1L28Gezy-3qQvxwKAJYG5UH6XhgPf76eH/view?usp=drive_link

7th oart link: https://drive.google.com/file/d/1kWqZg9hmLQG77qri3zCgIPGm32_gE_vK/view?usp=drive_link

#### Figure_4
Upon completion of the training process, Figure 4a will display the loss values. Such values are crucial in determining the efficiency of the training process and assessing the overall performance of the system under evaluation. It is worth noting that Figure 4a provides useful insights into the system's optimization trajectory, which can help inform future improvements.

To obtain Figures 4b and 4c, it is necessary to instruct the trained model to predict the output spectra for unseen geometric parameters, at wavelengths ranging from 1000 to 1800 nm. Essentially, this requires predicting the transmission spectra for 800 different wavelengths to form the complete transmission spectrum. Once this is done, it is necessary to compare the predicted spectrum with the spectrum obtained using the FDTD method. To identify the closest data, it is necessary to search for the nearest data points to the selected geometric parameters in the "result_V.csv" file.

In order to facilitate the replication of Figure 4b,c, we have retained the obtained data for your convenience. As such, the file "SquareRR_AOPS_Fig_04bc.py" may be used to test or apply the forward model. The relevant data for running this file is stored in the files
 "CircularRR_AOPS_Fig_03bc_Lower_sample.csv",
 "SquareRR_AOPS_Fig_04bc_Higher_sample.csv",
 "SquareRR_AOPS_Fig_04bc_FDTD_origin.csv",
 "SquareRR_AOPS_forward_model.json",
 and "SquareRR_AOPS_forward_model_weights.h5", all of which have been included here.

### Inverse_model
To facilitate the training of the inverse model, we recommend utilizing the Python source code provided in the 'SquareRR_AOPS_Inverse_model.py' file. We have meticulously curated 147,456 distinct examples derived from FDTD simulations and have saved them in the "result_H.csv" file, which can be accessed through the following links:

https://github.com/ehsan20e20e/CircularRR_AOPS/releases/download/untagged-80fe3b94e704169ada0a/result_H.rar
https://drive.google.com/file/d/1XW8CZP60sRJwzeInc0dSmcq_Q4VMNfoE/view?usp=drive_link

The aforementioned instances may be employed to train the inverse model, while the provided Python code can be utilized to simplify the process. By capitalizing on these resources, you can significantly improve the efficiency and precision of your model training.

To execute the 'SquareRR_AOPS_Inverse_model.py' file, it is necessary to have the 'result_H.csv' file. This file contains a significant amount of data, with a size of 1.6 gigabytes. Please ensure that you have this file available before proceeding with the execution of the aforementioned file.

#### Figure_7
Upon the completion of the training process, the loss values will culminate in the generation of Figure 7a.
In order to test the inverse model and generate Figure 7b and c, it is necessary to compare the data produced by the FDTD solver based on the geometric parameters derived from the inverse model with the provided geometric parameters. To assess the accuracy of the inverse model and obtain the legend of Figure 7, it is recommended to use the data generated by the FDTD solver as input to the inverse neural network model, specifically for the farthest data point from the training data. This will enable the generation of the output of the neural network model. To minimize the error of the forward network, it is essential to obtain the transmission spectrum of the proposed structure using an FDTD solver.

Figure 7b and c:

Step 1: Geometric Parameter. In order to facilitate the replication of the legend of Figure 7b and c, we have meticulously archived the obtained data. Consequently, for validation or application of the inverse model, the "SquareRR_AOPS_Figure07.py" file can be utilized. The mandatory data files for running this program are "SquareRR_AOPS_Figure06_furthest_data.csv", "CircularRR_AOPS_inverse_model.json", and "SquareRR_AOPS_inverse_model_weights.h5", all of which have been preloaded here.

As part of step 2 (transmission spectra), we have taken measures to facilitate the reproduction of Figure 7b and c. Specifically, we have stored the acquired data, which you can use to regenerate the aforementioned figure. To this end, we recommend utilizing the file "SquareRR_AOPS_Fig_07bc.py." The required data for running this file is stored in the file "SquareRR_AOPS_Fig_07bc_furthest_predicted.csv," which we have already loaded for your convenience.

### Supplementary_Information 
#### Figure_S1
to generate Figure S1, you can utilize the file "CircularRR_AOPS_S1_Fig_S01.m". The required data for running this file is stored in the file "Johnsonsilver.mat", which has been loaded here.

#### Figure_S2
to generate Figure S2, you can utilize the file "CircularRR_AOPS_S2_Fig_S02.py". The required data for running this file is stored in the file "result_V.csv", which has been uploaded in the following link: https://drive.google.com/file/d/1XW8CZP60sRJwzeInc0dSmcq_Q4VMNfoE/view?usp=drive_link.

#### Figure_S3
Figure S3a: To plot a three-dimensional bar chart of The computational cost, you would need to vary the number of layers and the number of neurons each time and record the training time. For the purpose of easily reproducing the plot, we have stored the acquired data. Therefore, to generate Figure S3a, you can utilize the file "CircularRR_AOPS_S3_Fig_S03a.m".

Figure S3b: To obtain Figure S3b, you can keep the number of neurons fixed at 60 and the number of layers fixed at 6 and then you would need to vary the number of epochs. For the purpose of easily reproducing the plot, we have stored the acquired data. Therefore, to generate Figure S3b, you can utilize the file "CircularRR_AOPS_S3_Fig_S03b.m".

#### Figure_S5
To plot Figure S5, you would need to vary the number of layers and the number of neurons each time and record the loss value. For the purpose of easily reproducing the plot, we have stored the acquired data. Therefore, to generate Figure S5, you can utilize the file "CircularRR_AOPS_S4_Fig_S05.py". The required data for running this file is stored in the file "CircularRR_AOPS_S4_Fig_S05.csv", which has been loaded here.

#### Figure_S6
To plot Figure S6, you would need to vary the number of layers each time and after training the network, use it to predict the transmission spectrum of a structure with specific geometric parameters that the network has not seen before. In this paper, for Figure S6, we considered g1=g2=g3=45nm and g4=g5=20nm, and compared the predicted spectrum with the spectrum obtained from the Finite-Difference Time-Domain (FDTD) method.

For the purpose of easily reproducing the plot, we have stored the acquired data. Therefore, to generate Figure S6, you can utilize the file "CircularRR_AOPS_S2_Fig_S06.py". The required data for running this file is stored in the file "CircularRR_AOPS_S2_Fig_S06.csv", which has been loaded here.

#### Figure_S7
To achieve a sharper dip in the through port transmission spectrum, it is advisable to save the spectra extracted from the forward model into a matrix file compatible with MATLAB software, preferably namded as "dataset_T-shape3." Subsequently, the file "CircularRR_AOPS_S5_Fig_S07.m" can be utilized, allowing for the plotting of any desired spectra in the format of Figure S7.

To achieve a sharper dip in the drop port transmission spectrum, the file "CircularRR_AOPS_S5_Fig_S07_drop.m" can be utilized.

===> Please note that the first row of the data matrix is intended to contain NaN values.
===> Please be aware that the initial column in the data matrix must have zero values. The second column should represent wavelength. Columns 3 to 6 are designated for G1 to G5, respectively. Columns 8 and 9 are allocated for T1 and T2, respectively.
