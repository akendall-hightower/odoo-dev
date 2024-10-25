from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_motorcycle = fields.Boolean(string="Motorcycle", default=False)
  
