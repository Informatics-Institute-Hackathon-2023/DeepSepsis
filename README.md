# PhLORENS: Physiological Learned Objective Response Emergency Notification System

## Background
Sepsis is a host response to an infecting pathogen, and early detection is critical in the ICU. Risk factors include AIDS, COPD, immunosuppressives, advanced cancer, and advanced age. In the United States., 1.7 million people develop sepsis annually, and 270,000 die from sepsis-related complications every year. Currently, sepsis costs the U.S. healthcare system about $24 billion annually, accounting for 13% of total healthcare system costs (Reyna, et al. 2019). A safeguard warning system could be effective in delaying the onset of sepsis, which can lead to a 3.6 to 9.9% increase in patient mortality for each hour of the infection (Kumar et al, 2006).

## Data

Here we have trained a deep neural network on the PhysioNet sepsis dataset (N = 1.5M). Dataset includes 1.8% positive cases and at least 40 features such as vital signs, laboratory values, and demographic information.

## Usage

We developed an application for research use, called PhLORENS (Physiological Learned Objective Response Emergency Notification System) that can be used to provide reporting to predict the development of ICU emergencies (i.e., code blue events). In addition to sepsis prediction, we could potentially refine our model and create a safeguard warning system for nursing and medical staff to monitor the development of additional clinical objectives. The link to the application is available here: [PhLORENS](https://phlorens.streamlit.app)

## Results

Our model was trained in Python using the Keras framework, and uses three feedforward, fully connected layers of 512 nodes, as well as LeakyReLU activation functions (to propagate non-zero gradients) and L1 regularization. After pre-processing the data with patient timeseries censoring, outlier removal, and median value imputation, we trained the model using majority class undersampling (0.1% of nonsepsis data to obtain a 1.1 : 1 class balance) and 80:20 training/validation split. After testing on 778,000 test samples, we achieved a macro average F1 score of 73%. The most important feature correlated with the development of sepsis in the ICU was the troponin biomarker, an indicator of (cardiovascular) muscle damage.

## Team Members

|Name | Email | Role |
----|--|--|
| Kevin Song | kmsong@uab.edu | Team Leader  
| Zhandos Sembay | zsembay8@uab.edu | Team Member
| Radomir Slominski | rslom@uab.edu | Team Member
| Melissa Hall | hallma0@uab.edu | Team Member

AI.MED Laboratory
University of Alabama at Birmingham