## Enhancing MRI Data Resolution for Speech Production Research: A Comparative Study of Super-Resolution Models


This repository is the coding part of the dissertation named "Enhancing MRI Data Resolution for Speech Production Research: A Study of Super-Resolution Models". You can find the dissertation: 


The repository makes possible to reproduce all the outcomes and the codes in the dissertation. Step by step guide can be found after "abstract"

# Abstract:


#  Train Super-Resolution Models included in the Dissertation

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

3. ----------
| Method | Original Link |
|---|---|
| DnCNN |[https://github.com/cszn/DnCNN](https://github.com/cszn/DnCNN)|
| FDnCNN |[https://github.com/cszn/DnCNN](https://github.com/cszn/DnCNN)|
| FFDNet | [https://github.com/cszn/FFDNet](https://github.com/cszn/FFDNet)|
| SRMD | [https://github.com/cszn/SRMD](https://github.com/cszn/SRMD)|
| DPSR-SRResNet | [https://github.com/cszn/DPSR](https://github.com/cszn/DPSR)|
| SRResNet | [https://github.com/xinntao/BasicSR](https://github.com/xinntao/BasicSR)|
| ESRGAN | [https://github.com/xinntao/ESRGAN](https://github.com/xinntao/ESRGAN)|
| RRDB | [https://github.com/xinntao/ESRGAN](https://github.com/xinntao/ESRGAN)|
| IMDN | [https://github.com/Zheng222/IMDN](https://github.com/Zheng222/IMDN)|
| USRNet | [https://github.com/cszn/USRNet](https://github.com/cszn/USRNet)|
| DRUNet | [https://github.com/cszn/DPIR](https://github.com/cszn/DPIR)|
| DPIR | [https://github.com/cszn/DPIR](https://github.com/cszn/DPIR)|
| BSRGAN | [https://github.com/cszn/BSRGAN](https://github.com/cszn/BSRGAN)|
| SwinIR | [https://github.com/JingyunLiang/SwinIR](https://github.com/JingyunLiang/SwinIR)|
| VRT | [https://github.com/JingyunLiang/VRT](https://github.com/JingyunLiang/VRT)       |
| DiffPIR | [https://github.com/yuanzhi-zhu/DiffPIR](https://github.com/yuanzhi-zhu/DiffPIR)|

References
----------
```BibTex
@inproceedings{zhu2023denoising, % DiffPIR
title={Denoising Diffusion Models for Plug-and-Play Image Restoration},
author={Yuanzhi Zhu and Kai Zhang and Jingyun Liang and Jiezhang Cao and Bihan Wen and Radu Timofte and Luc Van Gool},
booktitle={IEEE Conference on Computer Vision and Pattern Recognition Workshops},
year={2023}
}
@article{liang2022vrt,
title={VRT: A Video Restoration Transformer},
author={Liang, Jingyun and Cao, Jiezhang and Fan, Yuchen and Zhang, Kai and Ranjan, Rakesh and Li, Yawei and Timofte, Radu and Van Gool, Luc},
journal={arXiv preprint arXiv:2022.00000},
year={2022}
}
@inproceedings{liang2021swinir,
title={SwinIR: Image Restoration Using Swin Transformer},
author={Liang, Jingyun and Cao, Jiezhang and Sun, Guolei and Zhang, Kai and Van Gool, Luc and Timofte, Radu},
booktitle={IEEE International Conference on Computer Vision Workshops},
pages={1833--1844},
year={2021}
}
@inproceedings{zhang2021designing,
title={Designing a Practical Degradation Model for Deep Blind Image Super-Resolution},
author={Zhang, Kai and Liang, Jingyun and Van Gool, Luc and Timofte, Radu},
booktitle={IEEE International Conference on Computer Vision},
pages={4791--4800},
year={2021}
}
@article{zhang2021plug, % DPIR & DRUNet & IRCNN
  title={Plug-and-Play Image Restoration with Deep Denoiser Prior},
  author={Zhang, Kai and Li, Yawei and Zuo, Wangmeng and Zhang, Lei and Van Gool, Luc and Timofte, Radu},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year={2021}
}
@inproceedings{zhang2020aim, % efficientSR_challenge
  title={AIM 2020 Challenge on Efficient Super-Resolution: Methods and Results},
  author={Kai Zhang and Martin Danelljan and Yawei Li and Radu Timofte and others},
  booktitle={European Conference on Computer Vision Workshops},
  year={2020}
}
@inproceedings{zhang2020deep, % USRNet
  title={Deep unfolding network for image super-resolution},
  author={Zhang, Kai and Van Gool, Luc and Timofte, Radu},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
  pages={3217--3226},
  year={2020}
}
@article{zhang2017beyond, % DnCNN
  title={Beyond a gaussian denoiser: Residual learning of deep cnn for image denoising},
  author={Zhang, Kai and Zuo, Wangmeng and Chen, Yunjin and Meng, Deyu and Zhang, Lei},
  journal={IEEE Transactions on Image Processing},
  volume={26},
  number={7},
  pages={3142--3155},
  year={2017}
}
@inproceedings{zhang2017learning, % IRCNN
title={Learning deep CNN denoiser prior for image restoration},
author={Zhang, Kai and Zuo, Wangmeng and Gu, Shuhang and Zhang, Lei},
booktitle={IEEE conference on computer vision and pattern recognition},
pages={3929--3938},
year={2017}
}
@article{zhang2018ffdnet, % FFDNet, FDnCNN
  title={FFDNet: Toward a fast and flexible solution for CNN-based image denoising},
  author={Zhang, Kai and Zuo, Wangmeng and Zhang, Lei},
  journal={IEEE Transactions on Image Processing},
  volume={27},
  number={9},
  pages={4608--4622},
  year={2018}
}
@inproceedings{zhang2018learning, % SRMD
  title={Learning a single convolutional super-resolution network for multiple degradations},
  author={Zhang, Kai and Zuo, Wangmeng and Zhang, Lei},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
  pages={3262--3271},
  year={2018}
}
@inproceedings{zhang2019deep, % DPSR
  title={Deep Plug-and-Play Super-Resolution for Arbitrary Blur Kernels},
  author={Zhang, Kai and Zuo, Wangmeng and Zhang, Lei},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
  pages={1671--1681},
  year={2019}
}
@InProceedings{wang2018esrgan, % ESRGAN, MSRResNet
    author = {Wang, Xintao and Yu, Ke and Wu, Shixiang and Gu, Jinjin and Liu, Yihao and Dong, Chao and Qiao, Yu and Loy, Chen Change},
    title = {ESRGAN: Enhanced super-resolution generative adversarial networks},
    booktitle = {The European Conference on Computer Vision Workshops (ECCVW)},
    month = {September},
    year = {2018}
}
@inproceedings{hui2019lightweight, % IMDN
  title={Lightweight Image Super-Resolution with Information Multi-distillation Network},
  author={Hui, Zheng and Gao, Xinbo and Yang, Yunchu and Wang, Xiumei},
  booktitle={Proceedings of the 27th ACM International Conference on Multimedia (ACM MM)},
  pages={2024--2032},
  year={2019}
}
@inproceedings{zhang2019aim, % IMDN
  title={AIM 2019 Challenge on Constrained Super-Resolution: Methods and Results},
  author={Kai Zhang and Shuhang Gu and Radu Timofte and others},
  booktitle={IEEE International Conference on Computer Vision Workshops},
  year={2019}
}
@inproceedings{yang2021gan,
    title={GAN Prior Embedded Network for Blind Face Restoration in the Wild},
    author={Tao Yang, Peiran Ren, Xuansong Xie, and Lei Zhang},
    booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
    year={2021}
}
```
