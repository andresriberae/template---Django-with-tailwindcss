from django.db import models


class Company(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True,
    )

    code = models.CharField(
        max_length=50,
        unique=True,
    )

    nit = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    logo = models.ImageField(
        upload_to="companies/logos/",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Campaign(models.Model):

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="campaigns",
    )

    name = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Campaña"
        verbose_name_plural = "Campañas"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.company.name} - {self.name}"


class Diffusion(models.Model):

    class Classification(models.TextChoices):
        MARKETING = "MARKETING", "Marketing"
        UTILITY = "UTILITY", "Utility"
        AUTHENTICATION = "AUTHENTICATION", "Authentication"

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        related_name="diffusions",
    )

    name = models.CharField(
        max_length=200,
    )

    classification = models.CharField(
        max_length=30,
        choices=Classification.choices,
    )

    diffusion_date = models.DateField()

    total_sent = models.PositiveIntegerField(
        default=0,
    )

    total_delivered = models.PositiveIntegerField(
        default=0,
    )

    total_read = models.PositiveIntegerField(
        default=0,
    )

    total_responded = models.PositiveIntegerField(
        default=0,
    )

    total_failed = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Difusión"
        verbose_name_plural = "Difusiones"
        ordering = ["-diffusion_date"]

    def __str__(self):
        return self.name

    @property
    def delivery_rate(self):
        if self.total_sent == 0:
            return 0

        return round(
            (self.total_delivered / self.total_sent) * 100,
            2,
        )

    @property
    def read_rate(self):
        if self.total_sent == 0:
            return 0

        return round(
            (self.total_read / self.total_sent) * 100,
            2,
        )

    @property
    def response_rate(self):
        if self.total_sent == 0:
            return 0

        return round(
            (self.total_responded / self.total_sent) * 100,
            2,
        )


class DiffusionDailyMetric(models.Model):

    diffusion = models.ForeignKey(
        Diffusion,
        on_delete=models.CASCADE,
        related_name="daily_metrics",
    )

    date = models.DateField()

    sent = models.PositiveIntegerField(
        default=0,
    )

    delivered = models.PositiveIntegerField(
        default=0,
    )

    read = models.PositiveIntegerField(
        default=0,
    )

    failed = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        verbose_name = "Métrica diaria"
        verbose_name_plural = "Métricas diarias"

        constraints = [
            models.UniqueConstraint(
                fields=["diffusion", "date"],
                name="unique_diffusion_daily_metric",
            )
        ]

        ordering = ["-date"]

    def __str__(self):
        return f"{self.diffusion.name} - {self.date}"