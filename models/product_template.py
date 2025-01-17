from odoo import models, api
from odoo.exceptions import ValidationError

class ProductProduct(models.Model):
    _inherit = 'product.template'

    @api.constrains('list_price')
    def _check_non_negative_value(self):
        for record in self:
            if record.list_price < 0:
                raise ValidationError("El campo \"Precio de Venta\" no puede ser negativo")