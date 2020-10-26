# Bioinformatics and data sciences for life sciences

### Jesús Urtasun Elizari - University of Milan - 2020/21

## Chapter 7

#### Next-generation Secquencing (NGS) datasets
Computational methods to analyze increasingly larger datasets. Python is probably the fastest growing language in the field of data sciences. It includes a rich ecology of software libraries to perform complex data analysis. Another major point in Python is its great community, which is always ready to help and produce great documentation and high-quality reliable software.

Next-generation Sequencing (NGS) is one of the fundamental technological developments of the decade in the field of life sciences. Whole Genome Sequencing (WGS), RAD-Seq, RNA-Seq, Chip-Seq, and several other technologies are routinely used to investigate important biological problems. These are also called high-throughput sequencing technologies with good reason; they generate vast amounts of data that need to be processed. NGS is the main reason why computational biology is becoming a “big data” discipline. More than anything else, this is a field that requires strong bioinformatics techniques. There is very strong demand for professionals with these skillsets.

# Exercise 1 - 

1. Download tabix
*Example:* `sudo apt installa tabix;`

2. Perform partial download of the VCF file for chromosome 22 (up to 17 Mbp) of the 1000 genomes project.

```console
tabix -fh ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20130502/supporting/vcf_with_sample_level_annotation/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5_extra_anno.20130502.genotypes.vcf.gz 22:1-17000000
```

3. Then, compress it with bgzip.
```console
bgzip -c > genotypes.vcf.gz
```

https://hub.packtpub.com/processing-next-generation-sequencing-datasets-using-python/
