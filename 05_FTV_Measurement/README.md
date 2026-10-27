# FTV measurement definition

ftv_reference.py implements the manuscript equations PE = 100 Ã— (Se âˆ’ S0)/S0 and SER = (Se âˆ’ S0)/(Sl âˆ’ S0), with PE and SER lower thresholds. It specifies the FTV definition reported in the manuscript. Undefined ratios and non-finite image values are excluded explicitly. The finalized FTV measurements are the input for reproducing the statistical results. Original DCE-MRI and NIfTI masks are restricted by institutional policy.
