# CHEME599_Brain
Repository for CHEME599 Term Project on segmenting and tracking neurons in two-photon calcium imaging datasets.

This workflow has been tested on .tif, .tiff, .jpeg, and .png images

**Project Goals**
1. Filter images to remove extraneous information
2. Segment Neurons
3. Track Neurons in multi-day datasets 

**These goals are represented by three notebooks within this repository**
1. To determine what image filter provides the best preprocessing for your applications, go to the preprocess_testing folder and use the `Filter_Testing.ipynb` notebook to visualize some options I prepared. Once you decide which you like best, integrate the corresponding function (`.py` file) into your workflow. This notebook was built to work on GoogleColab. 
2. To segment neurons, use the `Segmentation_Workflow.ipynb` notebook on the main branch here. This uses the `unsharp_mask` function by default. To use a differnt one, replace that section of the code with the corresponding function for a different preprocessing protocol. This notebook was built to work on GoogleColab. 
3. To track segmented neurons, use `Tracking_Workflow.ipynb` from the main branch. This notebook cannot work on GoogleColab and requires to be run in the desktop version of python/JupyterNotebooks. The envrionment file I used to run this workflow is available as `environment.yml` in the main directory

For more background and a sample implementation, peruse the `Final_Project_Poster.pdf` document on the main branch. 
