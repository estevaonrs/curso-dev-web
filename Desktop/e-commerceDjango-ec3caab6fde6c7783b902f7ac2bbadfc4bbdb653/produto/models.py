from django.db.models.signals import post_save, pre_delete

from django.dispatch import receiver
from django.utils import timezone
import os
import random
import re
import string

from django.conf import settings
from django.db import models
from django.utils.text import slugify
from PIL import Image
from utils import utils


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
            while Categoria.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.nome)}-{random.randint(1, 1000)}"
        super().save(*args, **kwargs)


class Tipo(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
            while Tipo.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.nome)}-{random.randint(1, 1000)}"
        super().save(*args, **kwargs)


class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        default='SP',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'


class ContasPagar(models.Model):
    data = models.DateField(verbose_name="Data do pagamento")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT,
                                   default=None, blank=True, null=True, verbose_name="Fornecedor")
    valor = models.FloatField(verbose_name="Valor da dívida")
    pagamento = models.CharField(
        max_length=100, verbose_name="Tipo de pagamento")
    status = models.CharField(
        default="D",
        max_length=1,
        choices=(
            ('D', 'Devendo'),
            ('P', 'Pago'),
        )
    )

    class Meta:
        verbose_name = 'Contas a pagar'
        verbose_name_plural = 'Contas a pagar'


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    cor = models.CharField(max_length=255, blank=True, null=True)
    modalidade = models.CharField(
        default="A",
        max_length=1,
        choices=(
            ('A', 'Atacado'),
            ('V', 'Varejo'),
        )
    )
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField(verbose_name='Preço')
    preco_marketing_promocional = models.FloatField(
        default=0, verbose_name='Preço Promo.')
    tipo = models.ForeignKey(
        Tipo, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.PROTECT, default=None, blank=True, null=True)

    is_primary = models.BooleanField(
        default=False, verbose_name="Mostrar no template?")

    def get_preco_formatado(self):
        return utils.formata_preco(self.preco_marketing)
    get_preco_formatado.short_description = 'Preço'

    def get_preco_promocional_formatado(self):
        return utils.formata_preco(self.preco_marketing_promocional)
    get_preco_promocional_formatado.short_description = 'Preço Promo.'

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(img_full_path, optimize=True, quality=50)

    def save(self, *args, **kwargs):
        if not self.id:
            existing_products = Produto.objects.filter(nome=self.nome)
            if not existing_products.exists():
                self.is_primary = True
        if not self.slug:
            # Gerar 6 caracteres numéricos aleatórios
            random_chars = ''.join(random.choices(string.digits, k=6))
            # Adicionar os caracteres aleatórios ao slug
            slug = f'{slugify(self.nome)}-{random_chars}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome


class ImagemProduto(models.Model):
    produto = models.ForeignKey(
        Produto, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m/', blank=True, null=True)

    def __str__(self):
        return self.produto.nome


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True,
                            null=True, verbose_name='Nome da variação')
    preco = models.FloatField(verbose_name='Preço da variação')
    preco_promocional = models.FloatField(
        default=0, verbose_name='Preço promo da variação')
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'


class Influenciadores(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField(default=timezone.now,
                            verbose_name='Data do envio')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome or self.nome

    class Meta:
        verbose_name_plural = 'Influenciadores'
