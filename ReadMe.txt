1.Use Write_CSV_to_Folder_v3_FY.ipynb to create A csv_folder that will have all .csv from the subjects each .csv file will have the points that define the contour of the cancer cell.(Input is form LUNA dataset)

2.Use Create_jsn.ipynb to create a .json file that takes csv_folder as input.

3.Use Write_PNG_to_Folder_v3_FY.ipynb to create a PNG_folder that will have all the .png from subjects.(Input is form LUNA dataset)

4.Create a folder named "cancer_nodule" then create 2 more folder named "train" and "test" inside "cancer_nodule". Place all png and corresponding .json in "train". Similarly do for test

5.Use Train_maskRCNN.ipynb to train the model.

6.Use inspect_custom_model.ipynb to test.Link to download pre-trained model --https://drive.google.com/open?id=1-R71xDnBKFFXKQ-EYz0D9RCWHsxANwT9
