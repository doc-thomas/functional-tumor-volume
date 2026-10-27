"""Recorded five-fold inference command with user-supplied local directories."""
import argparse,subprocess
p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args()
subprocess.run(['nnUNetv2_predict','-i',a.input,'-o',a.output,'-d','701','-c','3d_fullres','-f','0','1','2','3','4','-tr','nnUNetTrainer_500epochs','-chk','checkpoint_best.pth'],check=True)
