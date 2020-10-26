# Bioinformatics and datas sciences for life sciences - Chapter 7: NGS

import vcf

# Inspecting the information we can get per record
v = vcf.Reader(filename='genotypes.vcf.gz')
 
print('Variant Level information')
infos = v.infos
for info in infos:
   print(info)
 
print('Sample Level information')
fmts = v.formats
for fmt in fmts:
   print(fmt)

# Explore a single VCF record
v = vcf.Reader(filename="genotypes2.vcf.gz.zip")
rec = next(v)
print(rec.CHROM, rec.POS, rec.ID, rec.REF, rec.ALT, rec.QUAL, rec.FILTER)
print(rec.INFO)
print(rec.FORMAT)
samples = rec.samples
print(len(samples))
sample = samples[0]
print(sample.called, sample.gt_alleles, sample.is_het, sample.phased)
print(int(sample['DP']))

# Check the type of variant and the number of nonbiallelic SNPs in a single pass
from collections import defaultdict
f = vcf.Reader(filename='genotypes.vcf.gz')
 
my_type = defaultdict(int)
num_alts = defaultdict(int)
 
for rec in f:
   my_type[rec.var_type, rec.var_subtype] += 1
   if rec.is_snp:
       num_alts[len(rec.ALT)] += 1
print(num_alts)
print(my_type)