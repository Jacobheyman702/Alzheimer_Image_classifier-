# Alzheimer_Image_classifier-

**Authors**: Jacob Heyman, Mitchell Krieger


## Overview
Alzheimer Disease (AD) is Neurodegenerative disease which has a distinctly complex and perplexing pathology.  One Major symptom of AD is induced progressive dementia, which is a result of a toxic accumulation of specific protiens in the limbic areas of the brain.  With over 47 million global cases of AD, there is a need for noval techniques for diagnosis and treatment.  A current hallmark biomarker of Alzheimers is the quantification of the accumuilation of amyloid-β and tau proteins in the brain. To quantify these protiens for a diagnosis a Positron emission tomography (PET) is used to asses the AD biomarkers in the cerebrospinal fluid.  While an accurate method for diagnosisng AD, PET Scans are expensive, require expert analysis, and subject the patients to radation. Lumber punctures which are required for the procudre, also present their own risks, such as back pain and bleeding. An alternative biomarker currently used for the diagnosis of AD is MRI imaging of the cerebral atrophy, another key characteristic in AD Neurodegenration.  Signs of cerebral atrophy can be used to diagnose AD earlier and aid in the course of treatment plans for the patients.  However There are issues with MRI detection of AD.  The MRI imagaging for AD atrophy requires expert analysis because it is difficult to visually detect small changes in tissue degeneration. Also atrophy may occur long before observable symptons like dementia occur, and/or the findings may just be the result of natural aging. 
 
With advances in machine learing and DeepLearning, In this study, we address the shortcomings MRI imaging for brain atrophy, and attempt to create an image classifier with convoluted neural networks(CNN).  Using a kaggle obtained collection of images collected from patients with four different levels of AD induced dementia, we trained several neural networks to classify the images into the four catagories.  Our goal was to create a model that could be used as a preliminary diagnosis for new patients with early signs of dimentia.  The aim of our project was to reduce as many false negative predictions as possible, in order to aid in the diagnosis of recently imaged patients.  We created several neural networks classifiers and tuned their parameters to improve the recall of the models, but found ourselves limited by both the data, and the large variance of the non-demented class.  For future studies we would to address the variatability found in our four original classes, and find additional image data to add to our modeling process.  




## Bussiness Problem 
Current methods for diagnosing Alzheimers disease in patients displaying early signs of dementia are expensive, risky and require expert analysis.  Recent studies have shown that using MRI imaging to visualize neurodegeneration can be an alternative method of diagnosis.  While this method decreases expense and risk, MRI imaging for tissue atrophy still requires visual analysis, resulting in potential human error.  Using machine learning algorithms we plan on creating a classifying model that can be used to classify the progression of demensia in AD patients and be used as a primary diagnostic tool for further medical intervention.  In this project we aim to answer the following questions:
    - What are some of the distinct features of the four classes of dementia?
    - Can we create a model that accuratly classifies AD MRI images?
    - What model and method best reduces the number of false positive when classifying images>


## Data
The data was collected from a kaggle database which was a selection of brian MRI images collected from various websites.
[Kaggle data set]('https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images')
The dataset consists of one train and one test folder, each with images labled with four different stages of AD symptom progression:
        - NonDemented    
        - Very Mild Demented
        - Mild Demented
        - Moderate Demented
    - There is a very large class imbalance, particularly in the Moderate and Mild Demented classes.  
![Imbalance]('./images/class_balance.png')
We used data augmentation to address class imbalance
![new_class_distribution]('./images/class_balance_aug.png')


## Data Understanding: Exploratory Data Analysis
To process our images we loaded the images with the keras ImageGenorator.  We visualized class distinctions in the images, by finding the mean and standard deviation image for each class. 
![mean images]('./images/mean.png')
Next we found the difference between the NonDemented and Moderatly demented classes to display the contrast of the two most disparate classes. Additionaly we observed the pixel gradiant between the NonDemented and moderatly demented classes using a histogram of oriented gradient plot.
![HOG]('./images/hog.png')
In the above, we can see differences in the structure of the brain between the four classes.  This is idedtifiable in the mean images through differences between the classes and in the hog in the stark gradients present in the moderate class. This may indicate the increased atrophy of the brain in the Moderatly demented images.   

We attempted to find the primary image componants with eigan images.  One hundred principal componants where identified that accounted for 71% of the class variance of the images. We where unable to identify what key features of the eigan images attributed to that specific class.  However, the high number of principle componants leads us to believe there is high variability in the dataset and concerns the predictive ability of a classification model.  For example, the NonDemented class alone, had 81 principle componants.  



## Methods
Modeling:
For a baseline model we created a simple neural network.  The structure was three dense layers of thirty neurons with bias at each neuron, and a softmax activation layer for classification.  To addresss class imbalance we used image augmentation, adding augmented images to the minority class images.  We then proformed several CNN model:
    1. Basic CNN: 2 conv2d followed by maxpooling with 2 dense layers using softmax as the final layer for classification.
    2. AlexNet: Transferlearning Model
    3. Fronteirs and Neuroscience CNN: Attempted to recreate a classification CNN from an MRI image classifying paper. 
    [Fronteirs]('https://www.frontiersin.org/articles/10.3389/fnins.2018.00777/full#T1')
To evaluate the above models we used accuracy and Recall as our primary metrics, in order to minimize false negatives.  We also used confusion matricies to asses how each model preformed as a classifier.  Additionally, for the CNN models we attempted to visually represent each layer in order to understand how each model makes a prediction for each learn each class, based on the selected features.  
    



## Results

Our best model was our fronteirs CNN which had and accuracy and recall of 66%.  It identified a good percentage of each class, however often misclassified the NonDemented class as alternative classes.  
![Confusion matrix]('./images/confusion_matrix_front.png')



## Conclusions
 The primary goal of this study, was to create a highly accurate image classifier to act as a primary diagnosis tool.  To acheive our goal we trained several nerual networks with our image data set, and attemped to increase the recall by tuning the parameters of each model.  We found that we where unable to improve our models past a 66% recall on our test set.  We suspect that the low accuracy and recall is most likely due to the ambiguity between brain atrophy from (AD) and the actual onset of dementia symptoms. In several papers, it has been noted that the atrophy of the brain may occur at a far earlier time than the symptoms they cause. There is a likely chance that our model was classifying the images by the level of atrophy present, but these images belonged to a different symptom class due to whatever symptom the patient was labled with at the time of imaging. Another factor could be that our imaging classifier was unable to distinguish the difference between the features of dementia patients and the normal degeneration of the brain that comes along with age, and is not synonymous with dementia.  

## Next Steps
Future studies will need to address the issue of variatability in the brains structure and the indierect releationship between atrophy and the severity of dementia.  One avanue would be to find a new dataset with a different set of lables that catagorizes the severity of atrophy and not the associated symptoms.  Another step would be to address the issue of how aging healthy brains may be confused with atrophied brains.  Finally we would also like to explore several other CNN structures, and additional transfer learning models to further improve the classification accuracy and recall.  


 

## For More Information
    - Tiwari, Sneham et al. “Alzheimer's disease: pathogenesis, diagnostics, and therapeutics.” International journal of nanomedicine vol. 14 5541-5554. 19 Jul. 2019, doi:10.2147/IJN.S200490
    - Johnson, Keith A et al. “Brain imaging in Alzheimer disease.” Cold Spring Harbor perspectives in medicine vol. 2,4 (2012): a006213. doi:10.1101/cshperspect.a006213
    - Scheltens, Philip. “Imaging in Alzheimer's disease.” Dialogues in clinical neuroscience vol. 11,2 (2009): 191-9. doi:10.31887/DCNS.2009.11.2/pscheltens






## Repository Structure

```
├──                            <- 
├──           <- 
├──                <- 
├──        <- 
├──              <-        
├─                              <- 
└──                 <- 