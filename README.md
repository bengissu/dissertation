# Super-Resolution in MRI: Reducing Artifacts and Enhancing Efficiency

This repository contains the codebase and experiments for my MSc Data Science dissertation titled **"Super-Resolution in MRI: Reducing Artifacts and Enhancing Efficiency"**, completed at the University of Sussex under the supervision of Dr. Ivor Simpson.

You can read the full dissertation [here](https://drive.google.com/drive/folders/1XCWqYjvUyAiDpuXU-2NXA10gUmGJfiwh?usp=sharing). This project showcases the application of **Super-Resolution (SR) techniques** to improve MRI images, specifically for **speech production studies**, addressing key challenges in MRI such as artifacts and resolution trade-offs.

## Abstract

### Objective and Methodology
This dissertation explores the use of SR methods to enhance **Magnetic Resonance Imaging (MRI)**, focusing on improving image quality while reducing common MRI artifacts (such as **motion blur** and **susceptibility artifacts**). The research simulates different MRI artifacts on low-resolution images and evaluates the performance of state-of-the-art SR models to mitigate these distortions.

### SR Models Evaluated
Three leading SR models were implemented and compared:
- **SwinIR**: Combines convolution and transformer mechanisms for local and global image feature extraction.
- **MSRResNet**: Focuses on multi-scale residual learning for detail reconstruction.
- **DnCNN**: Denoising convolutional neural network optimized for image enhancement.

### Results
Quantitative metrics (PSNR, SSIM) and qualitative assessments showed that **MSRResNet** delivered the most significant improvements in artifact reduction and overall image quality. However, **SwinIR** excelled in preserving organ structures in specific scenarios, and **DnCNN** performed efficiently in denoising tasks. The study identified areas for improvement in SR evaluation metrics, particularly to better align with **human visual perception**.

### Conclusion
This research contributes to advancing MRI quality for speech production studies, with potential applications in **medical imaging**, **linguistics**, and **speech therapy**. Future directions include refining SR models for better visual fidelity and extending their use to other medical imaging contexts.

## Repository Structure

```
├── config               # Configuration files for model training and testing
├── data-info-table.xlsx # Dataset information (from 'Watch Your Welsh' project)
├── results.ipynb        # Jupyter notebook with final results and comparisons
├── results.py           # Script to generate and compare model results
├── scripts              # Core model scripts (SwinIR, MSRResNet, DnCNN)
├── test-logs            # Logs from test runs on different datasets
├── valid-logs           # Validation logs
└── README.md            # Project overview (this file)
```

## Models and Implementation

The models trained and used for this dissertation can be accessed [here](https://drive.google.com/drive/folders/1gUBpM_3DDjS40OvAz-nl4hW0MTwU-JtT?usp=drive_link).

### Training Details
The following SR models were implemented:
- **SwinIR**: Uses transformer-based architecture for image restoration.
- **MSRResNet**: Leverages multi-scale learning with residual blocks.
- **DnCNN**: Specializes in denoising and general image restoration tasks.

Each model was trained and tested using **simulated low-resolution MRI images**. Artifacts such as **motion blur**, **ghosting**, **susceptibility artifacts**, and **low SNR** were artificially applied to evaluate model performance.

### Metrics
- **PSNR (Peak Signal-to-Noise Ratio)**: Evaluates image quality based on pixel-level similarity.
- **SSIM (Structural Similarity Index Measure)**: Assesses perceptual similarity focusing on structural details.

## Results Summary
The models were compared across different artifact scenarios, showing that **MSRResNet** achieved the highest **PSNR** and **SSIM** scores overall, especially in handling **motion artifacts** and **susceptibility artifacts**.

| Model     | Avg PSNR (dB) | Avg SSIM |
|-----------|---------------|----------|
| SwinIR    | 31.07         | 0.94     |
| MSRResNet | 37.57         | 0.97     |
| DnCNN     | 27.38         | 0.82     |

For detailed results, see the Jupyter notebook in `results.ipynb`.

## How to Use
1. Clone the repository:  
   ```
   git clone https://github.com/bengissu/super-resolution-mri.git
   ```
2. Install the necessary dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the models:
   ```
   python scripts/train_model.py --config config/swinir_config.yaml
   ```

## Acknowledgements
I would like to thank my supervisor, **Dr. Ivor Simpson**, for his guidance, and my friends and family for their support. The code is based on adaptations from [KAIR](https://github.com/cszn/KAIR) and is implemented on the **Watch Your Welsh** MRI dataset.
