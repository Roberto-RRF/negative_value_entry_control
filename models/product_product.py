from odoo import models, api
from odoo.exceptions import ValidationError

class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.constrains('lst_price')
    def _check_non_negative_value(self):
        for record in self:
            if record.lst_price < 0:
                raise ValidationError("El campo \"Precio de Venta\" no puede ser negativo")