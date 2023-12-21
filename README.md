## Enhancing MRI Data Resolution for Speech Production Research: A Comparative Study of Super-Resolution Models


This repository is the coding part of the dissertation named "Enhancing MRI Data Resolution for Speech Production Research: A Study of Super-Resolution Models". You can find the dissertation: 


The repository makes possible to reproduce all the outcomes and the codes in the dissertation. Step by step guide can be found after "abstract"

# Abstract:

# Step by Step Guide to Train Super-Resolution Models (Real-ESRGAN,) 

1. Clone the repository in your local:

git clone https://github.com/bengissu/dissertation.git

2. # Creating Image Dataset
  
 
 # to imitate the project as is with the dataset in the project (Data downloaded from watchyourwelsh.org.): 
Download the videos that used in the dissertation, they are shared in watchyourwelsh.org website. BY DOWNLOADING AND/OR USING THE DATA WITHIN THIS WEBSITE YOU AGREE TO THE OBLIGATIONS : https://watchyourwelsh.org/en/data-sharing-agreement.html

Running download-videos.sh will download the videos to /path/dissertation/videos in your local. Change /path/ in download-videos.sh.

make it executable:
chmod +x download-videos.sh
and execute
./download-videos.sh

 # If you have your video dataset:
   
   Copy your data to ./dissertation/videos
   Split data into frames : 
   python3 /path/dissertation/download-videos.sh   #change the /path/ the path you cloned the repository.


