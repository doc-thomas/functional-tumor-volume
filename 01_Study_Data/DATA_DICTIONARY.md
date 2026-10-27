# Data dictionary

- study_id: anonymous identifier shared across the five final analytical tables.
- subtype: HER2_positive or TNBC.
- center: A, development; B, main external validation; C, additional HER2-positive external validation.
- original_split: retained source train/test/validation assignment. A source train/test subdivisions are combined for development.
- analysis_row_order: frozen row order used for resampling reproduction.
- age: age in years.
- t: clinical T category 1-4; model reference T1.
- n: clinical N category 0-3; model reference N0.
- hr_class: p=HR positive, n=HR negative; used for HER2-positive models.
- ki67_class: h/high=high, l/low=low using the recorded 20% cutoff; used for TNBC models.
- nat: recorded treatment-regimen abbreviation, retained for treatment-sensitivity analyses.
- ajcc_stage: recorded stage, used as ordinal I/II/III in recurrence associations.
- label: 1=pCR, 0=non-pCR; pCR is ypT0/Tis ypN0. This is stored separately in pCR_outcomes.csv.
- v2_a through v441_b: absolute FTV measurements in mL; the exact column set and PE/SER definitions are supplied in FTV_threshold_definitions.csv.
- whole_tumor_volume_ml: complete pretreatment tumor-mask volume, mL, using verified corrected source records.
- recurrence_3y: recorded recurrence within 36 months, 1=yes and 0=no.
- recurrence_month: months from surgery to recorded recurrence where applicable.
- observation_month: recorded postoperative observation duration, months.
- hr_class, stage and recurrence fields remain source values; unrelated source metadata and direct identifiers were excluded.
- original_volume_ml, corrected_volume_ml, factor: anonymous source-record decimal-point correction log. Released whole-tumor volume values are already corrected; do not apply the factor again.

Model terms age, T2/T3/T4, N1/N2/N3, HR_positive and Ki67_high use the encodings above. log1p terms mean natural log(1 + mL). Relative FTV is the fixed selected absolute FTV divided by complete tumor volume; no ratio-specific threshold search is introduced. Numeric file_id in analysis is a newly assigned integer corresponding to study_id, not an original patient identifier.
