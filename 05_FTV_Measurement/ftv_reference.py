"""Reference quantification of the FTV definition reported in the manuscript."""
import numpy as np
def ftv_ml(pre,early,late,mask,spacing_mm,pe_cutoff,ser_cutoff):
 pre,early,late=np.asarray(pre,float),np.asarray(early,float),np.asarray(late,float)
 mask=np.asarray(mask,bool)
 if not (pre.shape==early.shape==late.shape==mask.shape):raise ValueError('Images and mask must be in the same space and have identical shapes.')
 spacing=np.asarray(spacing_mm,float)
 if spacing.shape!=(3,) or not np.isfinite(spacing).all() or (spacing<=0).any():raise ValueError('Three positive voxel spacings in mm are required.')
 # Explicit reference policy: exclude non-finite input and undefined PE/SER.
 valid=mask&np.isfinite(pre)&np.isfinite(early)&np.isfinite(late)&(pre!=0)&((late-pre)!=0)
 pe=np.full(pre.shape,np.nan);ser=np.full(pre.shape,np.nan)
 np.divide(100*(early-pre),pre,out=pe,where=valid)
 np.divide(early-pre,late-pre,out=ser,where=valid)
 retained=valid&(pe>=pe_cutoff)&(ser>=ser_cutoff)
 return float(retained.sum()*spacing.prod()/1000)
if __name__=='__main__':
 # Hand-checkable boundary case; this does not use any participant image.
 s0=np.array([100.,100.,100.,0.]);se=np.array([170.,169.,190.,50.]);sl=np.array([135.,135.,100.,10.])
 assert abs(ftv_ml(s0,se,sl,[1,1,1,1],[2,2,2],70,2)-0.008)<1e-15
 print('Reference PE/SER boundary and voxel-unit check passed.')
