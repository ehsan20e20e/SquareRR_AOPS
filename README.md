# SquareRR_AOPS
Animated Abstract (loading ... please wait):
![SquareRR_AOPS2](https://github.com/ehsan20e20e/SquareRR_AOPS/assets/106914575/82b8c75c-9f30-4d6e-8ac6-914e99deb533)

## Describtion
The provided repository serves as a demonstration of the application of deep learning techniques in the prediction of the spectral response of all-optical plasmonic switches. This repository is based on the extensive research presented in the paper titled "Inverse_design_of_plasmon-based_nonlinear_square_resonators_enabled_by_deep_neural_networks." It has been designed to address inverse design challenges, with a specific focus on the fields of photonics and optics.

#### Table of contents
* [Prerequisites](#Prerequisites)
* [Geting started](#Geting_started)
* * [Forward model](#Forward_model)
  * * *[Figure 4](#Figure_4)
* * [Inverse model](#Inverse_model)
  * * *[Figure 7](#Figure_7) 
* * [Supplementary Information](#Supplementary_Information)
  * * *[Figure S4](#Figure_S4)
  * * *[Figure S5](#Figure_S5)
  * * *[Figure S6](#Figure_S6)
  * * *[Figure S8](#Figure_S8)
  * * *[Figure S9](#Figure_S9)
#### Instructions
The following guidelines provide detailed instructions for setting up and running a copy of the project on your local machine, thus enabling you to perform testing and development activities. These instructions are tailored to ensure accuracy and completeness when executing the project setup process. Consequently, we recommend that you adhere to them meticulously.
## Prerequisites
To obtain the results presented in this article, the use of the following software packages is recommended.
1) MATLAB (for optimization)
2) Python (for neural networks and deep learning)
3) Lumerical (for FDTD simulations)
4) COMSOL (for FEM simulations)
5) Qualitek-4 (for Taguchi method)
6) Minitab (for DOE)
   
Specifically, for this code, we utilized MATLAB version R2023a, Python version 3.7.13, and Spyder version 5.1.5 within Anaconda version 4.14.0, Ansys Lumerical version 2023 R1, COMSOL Multiphysics 6.1, Qualitek-4 version 14.2.0 and Minitab version 21.4.2. The project can be completed without these programs; however, the ability to compare speed and generate data will be limited without installing MATLAB and Python.
https://github.com/ehsan20e20e/SquareRR_AOPS/releases

## Geting_started
To utilize the contents of this repository, it is crucial to generate the necessary data for the all-optical switch structure using various FDTD (Finite-Difference Time-Domain) solvers such as Lumerical, RSoft, or MATLAB. These solvers enable the production and simulation of the optical switch structure, which facilitates the analysis of its performance and characteristics.

The file named "SquareRR_AOPS_Structure_file.fsp" is recommended for Lumerical simulations. To create the three-dimensional structure of AOPS, you can use the "Create SquareRR_AOPS_structure_FDTD_solver.lsf" file. For automatic data generation, the "SquareRR_AOPS_auto_FDTD_dataset_generator" script file is available. It is advisable to utilize these tools for efficient and accurate performance in your business or academic setting.

The proposed plasmonic switch structure's raw data is available in CSV files. These files have been provided to facilitate the reproduction of the graphs and results presented in this article.

===> Please be advised that there was an error in the input data related to the Drop port. The data was mistakenly entered as negative, which has been rectified in the written code. To ensure the accuracy of the data, we have applied the absolute value function to the input data. We apologize for any inconvenience this may have caused and assure you that we have taken the necessary measures to prevent such errors in the future.

### Forward_model
To train the forward model, utilizing the Python code provided in the 'SquareRR_AOPS_Forward_model.py' file is recommended. To this end, we have generated 147,456 unique examples through FDTD simulations and saved them in the "result_V.csv" file (Please take note of the following information: 18432 out of the total number of examples is sufficient.). As a prerequisite for executing the 'SquareRR_AOPS_Forward_model.py' file, it is essential to obtain the 'result_H.csv' file which constitutes a big data file with a size of 5.7 gigabytes. By following these steps, you can effectively train the forward model and achieve accurate results.

The 'result_V.csv' file can be accessed as a single file through the following link: 
https://github.com/ehsan20e20e/SquareRR_AOPS/releases/download/untagged-54db6d6bee08573b3623/result_V.rar

#### Figure_4
Upon completing the training process, Figure 4a will display the loss values. Such values are crucial in determining the efficiency of the training process and assessing the system's overall performance under evaluation. It is worth noting that Figure 4a provides useful insights into the system's optimization trajectory, which can help inform future improvements.

To obtain Figures 4b and 4c, it is necessary to instruct the trained model to predict the output spectra for unseen geometric parameters, at wavelengths ranging from 1000 to 1800 nm. This requires predicting the transmission spectra for 800 wavelengths to form the complete spectrum. Once this is done, it is necessary to compare the predicted spectrum with the spectrum obtained using the FDTD method. Searching for the nearest data points to the selected geometric parameters in the "result_V.csv" file is necessary to identify the closest data.

To facilitate the replication of Figure 4b,c, we have retained the obtained data for your convenience. As such, the file "SquareRR_AOPS_Fig_04bc.py" may be used to test or apply the forward model. The relevant data for running this file is stored in the files
 "SquareRR_AOPS_Fig_03bc_Lower_sample.csv",
 "SquareRR_AOPS_Fig_04bc_Higher_sample.csv",
 "SquareRR_AOPS_Fig_04bc_FDTD_origin.csv",
 "SquareRR_AOPS_forward_model.json",
 and "SquareRR_AOPS_forward_model_weights.h5", all of which have been included here.

### Inverse_model
To facilitate the training of the inverse model, we recommend utilizing the Python source code provided in the 'SquareRR_AOPS_Inverse_model.py' file. We have meticulously curated 147,456 distinct examples derived from FDTD simulations and have saved them in the "result_H.csv" file, which can be accessed through the following links:
https://github.com/ehsan20e20e/SquareRR_AOPS/releases/download/untagged-54db6d6bee08573b3623/result_H.rar

The aforementioned instances may be employed to train the inverse model, while the provided Python code can be utilized to simplify the process. By capitalizing on these resources, you can significantly improve the efficiency and precision of your model training.

To execute the 'SquareRR_AOPS_Inverse_model.py' file, you need the 'result_H.csv' file. This file contains a significant amount of data, with a size of 1.6 gigabytes. Please ensure you have this file available before executing the aforementioned file.

#### Figure_7
Upon completing the training process, the loss values will culminate in the generation of Figure 7a.
To test the inverse model and generate Figures 7b and c, it is necessary to compare the data produced by the FDTD solver based on the geometric parameters derived from the inverse model with the provided geometric parameters. To assess the accuracy of the inverse model and obtain the legend of Figure 7, it is recommended to use the data generated by the FDTD solver as input to the inverse neural network model, specifically for the farthest data point from the training data. This will enable the generation of the output of the neural network model. To minimize the forward network error, obtaining the proposed structure's transmission spectrum is essential to use an FDTD solver.

Figure 7b and c:

Step 1: Geometric Parameter. We have meticulously archived the obtained data to facilitate the replication of the legend of Figure 7b and c. Consequently, the "SquareRR_AOPS_Figure07.py" file can validate or apply the inverse model. The mandatory data files for running this program are "SquareRR_AOPS_Figure07_furthest_data.csv," "SquareRR_AOPS_inverse_model.json," and "SquareRR_AOPS_inverse_model_weights.h5," all of which have been preloaded here.

As part of step 2 (transmission spectra), we have taken measures to facilitate the reproduction of Figure 7b and c. Specifically, we have stored the acquired data, which you can use to regenerate the figure. To this end, we recommend utilizing the file "SquareRR_AOPS_Fig_07bc.py." The required data for running this file is stored in "SquareRR_AOPS_Fig_07bc_furthest_predicted.csv," which we have already loaded for your convenience.

### Supplementary_Information 


#### Figure_S4
To generate Figure S4, please refer to the file "SquareRR_AOPS_Fig_S04.py." The necessary data for running this file is stored in the file "result_V.csv," which can be downloaded at the following link:
https://github.com/ehsan20e20e/SquareRR_AOPS/releases.

#### Figure_S5
To generate Figure S5, the number of layers and neurons must be varied each time, and the corresponding loss value must be recorded. To ensure the reproducibility of the plot, we have stored the acquired data, which can be utilized to execute the file "SquareRR_AOPS_Fig_S05.py." The required data for running this file is stored in the "SquareRR_AOPS_Fig_S05.csv," loaded here. Therefore, generating Figure S5 can be achieved without issues by utilizing the aforementioned files.

#### Figure_S6
To generate Figure S6, it is necessary to vary the number of layers during each iteration. Upon completion of the network training phase, the network should be employed to predict the transmission spectrum of a structure with specific geometric parameters that have not been previously observed by the network. In this research, we considered S1=S2=S3=45nm and S4=S5=20nm for Figure S6, and compared the predicted spectrum with the spectrum obtained through the FDTD method.

We have retained the acquired data to facilitate the reproduction of the plot. Therefore, to generate Figure S6, it is recommended to utilize the file "SquareRR_AOPS_S2_Fig_S06.py." The requisite data for executing this file is stored in the "SquareRR_AOPS_Fig_S06.csv," which has been loaded into the system.

#### Figure_S7
To achieve a more distinct trough in the transmission spectrum of the through port, it is recommended that the spectra derived from the forward model be stored in a matrix file compatible with MATLAB software. The file should be named "dataset_T-shape3." Following this, the file "SquareRR_AOPS_Fig_S07.m" can be employed to generate the desired spectra in the format of Figure S7.

To achieve a more pronounced dip in the transmission spectrum of the drop port, it is recommended to utilize the file "SquareRR_AOPS_Fig_S07_drop.m". This file can help create a sharper and more defined dip in the spectrum, which can be valuable in various business or academic settings. By employing this file, you can enhance the quality and accuracy of your work and achieve more precise results. Utilizing this file can be a valuable tool in your research and experimentation, and can help improve your work's overall quality.

===> Please be advised that the initial row of the data matrix is intended to contain NaN (Not a Number) values. This deliberate measure ensures the data is aligned and represented accurately. It is important to note that any modification of the first row may result in errors that could compromise the integrity of the entire data set. Therefore, we strongly recommend that the first row be left untouched and that any analysis be performed on subsequent rows. Thank you for your attention to this matter.
===> Please note that the initial column in the data matrix must contain zero values. The second column should be dedicated to representing the wavelength. Columns 3 to 6 are designated for S1 to S5, respectively. Columns 8 and 9 are allocated for T1 and T2, respectively. Ensure these guidelines are strictly adhered to when working with the data matrix. Any deviation from this standard may result in erroneous conclusions and incorrect data analysis.

#### Figure_S8
The file "SquareRR_AOPS_Fig_S08.m" can be utilized to generate Figure S8. The required data for running this file is stored in the "Johnsonsilver.mat," which has already been loaded.

#### Figure_S9
To plot a three-dimensional bar chart of the computational cost, it is necessary to vary the number of layers and neurons while recording the training time. However, for the sake of ease in reproducing the plot, the acquired data has been stored. As such, to generate Figure S9, please utilize the file "SquareRR_AOPS_Fig_S09.m"
