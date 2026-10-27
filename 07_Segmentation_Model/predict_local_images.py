"""Five-fold inference on independently held local images."""
from pathlib import Path
import argparse,subprocess
p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--tta',choices=['enabled','disabled'],default='enabled');a=p.parse_args()
model=Path(__file__).resolve().parent/'model'
cmd=['nnUNetv2_predict_from_modelfolder','-i',a.input,'-o',a.output,'-m',str(model),'-f','0','1','2','3','4','-chk','checkpoint_best.pth']
if a.tta=='disabled':cmd.append('--disable_tta')
subprocess.run(cmd,check=True)
