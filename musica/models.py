from django.db import models

class Musica(models.Model):
    nome = models.CharField(max_length=255, verbose_name = "Nome da Canção:",)
    cantor = models.CharField(max_length=255,null=False, verbose_name = "Nome do Cantor:",)
    compositor = models.CharField(max_length=255,null=True, verbose_name = "Nome do Compositor:",)
    data_lancamento = models.DateField(verbose_name = "Data de Lançamento:", auto_now=False, blank=True, null=True,)
    album = models.CharField(max_length=255,null=False, verbose_name = "Nome do Album:",)
    link = models.URLField(verbose_name = "Link da Música no Youtube:",)
    imagem = models.ImageField(upload_to = "images", null = False,verbose_name = "Imagem da Música:",)

    class Meta:
        verbose_name = "Música"
        verbose_name_plural = "Músicas"
        db_table = "musica"

    def __str__(self):
        return self.nome