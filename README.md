# Pretreatment functional tumor volume for pCR prediction

Reproducibility materials for the multicenter study of HER2-positive and triple-negative breast cancer.

## Repository contents

| Folder | Contents |
|---|---|
| 01_Study_Data | Final de-identified clinical data, 880 FTV measurements, separate pCR outcomes, whole-tumor volume, cohort assignments, and data dictionaries |
| 02_Statistical_Analysis | Executable analysis scripts, input matrices, frozen development results, and supplementary analyses |
| 03_Prediction_Models | Full-precision fitted coefficients and frozen probability cutoffs |
| 04_Expected_Results | Patient predictions and model-performance results for verification |
| 05_FTV_Measurement | Reference implementation of the reported PE/SER definition |
| 06_FTV_Reliability | ROI-derived ICC estimates, supporting measurements, and Table S20/Figure S5 |
| 07_Segmentation_Model | Five trained segmentation checkpoints, configurations, trainer, and inference interfaces |
| 08_Verification | Numerical reproduction results |

FILE_INDEX.csv describes every file. MANUSCRIPT_RESULTS_INDEX.csv maps manuscript sections and tables to the relevant numerical files. SHA256SUMS.csv records file sizes and hashes.

## Data and identifiers

The analytical cohort contains 849 patients: 587 HER2-positive and 262 triple-negative cases. Join the five final tables in 01_Study_Data by study_id. The outcome is 1 for pCR (ypT0/Tis ypN0) and 0 for non-pCR. Volume is in mL. study_id and numeric file_id are newly assigned study identifiers; original names and patient identifiers are excluded. Scientific measurements, fitted coefficients, thresholds, and seeds retain numerical precision. Author contact details in this README are intended for public correspondence.

Institutional requirements prohibit public release of original DCE-MRI images and NIfTI masks. They are not included. The released measurements support statistical reproduction; image-to-FTV re-extraction requires the restricted images.

## Quick verification

Install NumPy, then run from this package root:

    python 02_Statistical_Analysis/verify_frozen_models.py
    python 02_Statistical_Analysis/verify_volume_records.py
    python 05_FTV_Measurement/ftv_reference.py

The probability check reproduces frozen external predictions and checks AUC, Brier scores, and classification counts. 08_Verification documents the results. The volume check reads the already corrected finalized records; do not apply the recorded factor again. The FTV reference check uses synthetic arrays, not participant images.

## Full statistical analysis

Use the pinned stack in requirements-statistics.txt. The input order and stage-specific random-seed formulas are retained. Run the scripts in the following order:

    python 02_Statistical_Analysis/scripts/run_clinical_benchmark.py
    python 02_Statistical_Analysis/scripts/run_ftv_optimization.py
    python 02_Statistical_Analysis/scripts/run_combined_models.py
    python 02_Statistical_Analysis/scripts/run_recurrence_secondary.py
    python 02_Statistical_Analysis/scripts/complete_ftv_metrics.py
    python 02_Statistical_Analysis/scripts/formal_statistics.py
    python 02_Statistical_Analysis/scripts/treatment_sensitivity.py
    python 02_Statistical_Analysis/scripts/run_supplementary_ftv_analyses.py --stage all
    python 02_Statistical_Analysis/scripts/hr_stratified_analysis.py --stage all
    python 02_Statistical_Analysis/scripts/volume_extension_analysis.py --stage develop
    python 02_Statistical_Analysis/scripts/volume_extension_analysis.py --stage relative
    python 02_Statistical_Analysis/scripts/volume_extension_analysis.py --stage evaluate --include-relative
    python 06_FTV_Reliability/summarize_icc.py

Expected predictions and performance results are provided for numerical verification. The threshold-stability analysis uses 200 resamples; most performance intervals use 2,000 resamples. Calibration intervals use ordinary patient bootstraps. The main seed is 20260924.

## Segmentation inference

07_Segmentation_Model/model contains fold_0 through fold_4, checkpoint_best.pth, plans.json, and dataset.json. The model uses 3d_fullres and nnUNetTrainer_500epochs. Install the supplied trainer class in the matching nnU-Net v2 trainer-variants location. The recorded environment includes PyTorch 2.10.0+cu128 and cuDNN 91002; the exact nnU-Net package version was not retained.

    python 07_Segmentation_Model/predict_local_images.py --input LOCAL_IMAGES --output LOCAL_MASKS --tta enabled

The portable entry uses explicit TTA selection. The dataset-based command did not include a TTA-disabling argument; its CLI default applies. Standard nnU-Net filenames are preserved for compatibility.

## GitHub upload

The code and tabular data can be committed normally. Each checkpoint is approximately 247 MB and requires Git LFS or separate GitHub Release assets; it cannot be uploaded through the ordinary browser file interface. The supplied .gitattributes configures *.pth for Git LFS. When copying this package into an existing repository, merge that rule with any existing attributes. Do not overwrite unrelated repository contents.

Use a versioned release and record its commit or permanent data-record link in the manuscript and response after upload. This local package does not itself create an online release. Author repository: https://github.com/doc-thomas/Cancer-Research . Corresponding author: Song Peng, cqfyfsk@126.com.
