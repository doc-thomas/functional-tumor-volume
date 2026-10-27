from pathlib import Path
import csv,collections
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
with (P/'FTV_ICC_estimates.csv').open(encoding='utf-8-sig',newline='') as h:rows=list(csv.DictReader(h))
groups=collections.defaultdict(list)
for r in rows:groups[(r['subtype'],r['original_subset'],r['early_window'])].append(float(r['ICC']))
summary=[]
for (sub,subset,window),values in groups.items():
 a=np.asarray(values);assert len(a)==440
 summary.append({'subtype':sub,'original_subset':subset,'early_window':window,'n_definitions':len(a),'median_ICC':float(np.median(a)),'q1_ICC':float(np.quantile(a,.25)),'q3_ICC':float(np.quantile(a,.75)),'minimum_ICC':float(a.min()),'maximum_ICC':float(a.max()),'fraction_ICC_ge_0_81':float(np.mean(a>=.81))})
with (P/'TableS20_FTV_reliability.csv').open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
fig,axs=plt.subplots(1,2,figsize=(10,4.4),gridspec_kw={'width_ratios':[1.12,1]})
for ax,sub,title in zip(axs,['HER2_positive','TNBC'],['A  HER2-positive','B  Triple-negative']):
 subset_order=list(dict.fromkeys(r['original_subset'] for r in summary if r['subtype']==sub))
 for w,color,dy,label in [('a','#325E7A',-.12,'Early window a'),('b','#00888A',.12,'Early window b')]:
  z=[next(r for r in summary if r['subtype']==sub and r['original_subset']==s and r['early_window']==w) for s in subset_order]
  y=np.arange(len(z))+dy;med=np.array([r['median_ICC'] for r in z]);lo=np.array([r['q1_ICC'] for r in z]);hi=np.array([r['q3_ICC'] for r in z])
  ax.errorbar(med,y,xerr=[med-lo,hi-med],fmt='o',color=color,capsize=3,label=label,markersize=5)
 ax.set_yticks(range(len(subset_order)),subset_order);ax.invert_yaxis();ax.set_xlim(.8,1.0);ax.set_xticks([.8,.85,.9,.95,1.0]);ax.set_xticklabels(['0.800','0.850','0.900','0.950','1.000']);ax.set_xlabel('ICC across candidate FTV definitions');ax.set_title(title,loc='left',fontweight='bold');ax.grid(axis='x',alpha=.18)
axs[0].legend(frameon=False,loc='lower left',fontsize=9)
fig.text(.5,.015,'Points: median ICC; bars: interquartile range across 440 definitions. Subsets are shown separately.',ha='center',fontsize=8.5)
fig.tight_layout(rect=(0,.05,1,1))
fig.savefig(P/'FigureS5_FTV_reliability.png',dpi=330)
fig.savefig(P/'FigureS5_FTV_reliability.pdf')
print('ICC summary rows:',len(summary),'median range:',min(r['median_ICC'] for r in summary),max(r['median_ICC'] for r in summary))
