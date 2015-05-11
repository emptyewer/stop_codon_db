from django.db import models

# Create your models here.
class Gene(models.Model):
    unigene_id = models.CharField(max_length=20)
    protein_id = models.CharField(max_length=20)
    gene_id = models.CharField(max_length=20)

    protein_length = models.PositiveIntegerField(default=0)
    gene_length = models.PositiveIntegerField(default=0)

    protein_name = models.CharField(max_length=200)
    gene_name = models.CharField(max_length=200)

    organism = models.CharField(max_length=200)
    gene_type = models.CharField(max_length=20)

    protein_similarity = models.FloatField(max_length=5, default=0)

    gene_start_nucleotide = models.PositiveIntegerField(default=0)
    gene_end_nucleotide = models.PositiveIntegerField(default=0)
    gene_start_codon = models.CharField(max_length=3)
    gene_stop_codon = models.CharField(max_length=3)
    protein_start_aa = models.CharField(max_length=1)
    protein_stop_aa = models.CharField(max_length=1)

    gene_sequence = models.TextField()
    protein_sequence = models.TextField()