from django.db import models
from django.utils.translation import gettext as _

class Product(models.Model):
    title = models.CharField(_('Title'), help_text=_("Short title of the product."), max_length=50)
    description = models.TextField(_('Description'), help_text=_("Longer description of the product."))
    cost = models.DecimalField(_('Cost'), help_text=_("Cost of the product without taxes and shipping costs."), max_digits=10, decimal_places=2)
    stock = models.IntegerField(_('Stock'), help_text=_("Amount of product units in stock."),default=0)
    date_created = models.DateTimeField(_('Date Created'), help_text=_("Product creation date."), auto_now_add=True)
    date_modified = models.DateTimeField(_('Date Modified'), help_text=_("Product modification date."), auto_now=True)


class ProductImage(models.Model):
    caption = models.CharField(_('Caption'), help_text=_("Caption of the image."),max_length=50)
    product = models.ForeignKey(Product, verbose_name=_("Product"),help_text=_("Product related to image."), on_delete=models.CASCADE, related_name="product_images")
    figure = models.ImageField(_("Figure"),help_text=_("Image figure."), upload_to="figures")
    date_created = models.DateTimeField(_('Date Created'), help_text=_("Image creation date."), auto_now_add=True)
    date_modified = models.DateTimeField(_('Date Modified'),help_text=_("Image modification date."), auto_now=True)


