# What you have to know 
All the code available below is the corrected version of the Mage stream. 

## 1. Configure your Mage Pipeline 
Files in this repository are ready to be used for the project. However, you should be aware that even if it is not mentioned in the video you have to change your service account key inside your YAML file (config file). Just replace * with your key in it. 

## 2. Occurring Errors 

Some issues can occur as they have not been covered in the video 

1. **Project Not FOUND in Location US**
   You might not be able to run your data exporter after executing the flow. This is happening because you did not copy-paste the right project name for all your variables containing projects such as table_id or project_id. 

2. **Google Cloud is not installed**
   When running your data exporter it might crash as you did not install Google Cloud modules on your VM. Open VM instructions file in the repository for installing all the modules

## For unknown occurring errors 
Please refer to this tutorial on mage I used for building the pipeline : **Uber Data Analytics | End-To-End Data Engineering Project**  

## 3. Additional SQL Queries 
I added additional SQL Queries for helping you to check duplicated and missing elements in your BigQuery Tables. Feel free to change and update them. 
