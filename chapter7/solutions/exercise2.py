# Bioinformatics and datas sciences for life sciences - Chapter 7: NGS

from collections import defaultdict
 
import seaborn as sns
import matplotlib.pyplot as plt
 
import vcf
 
def do_window(recs, size, fun):
   start = None
   win_res = []
   for rec in recs:
       if not rec.is_snp or len(rec.ALT) > 1:
           continue
       if start is None:
           start = rec.POS
       my_win = 1 + (rec.POS - start) // size
       while len(win_res) < my_win:
           win_res.append([])
       win_res[my_win - 1].extend(fun(rec))
   return win_res
 
wins = {}
size = 2000
vcf_names = ['centro.vcf.gz', 'standard.vcf.gz']
for vcf_name in vcf_names:
   recs = vcf.Reader(filename=vcf_name)
   wins[name] = do_window(recs, size, lambda x: [1])