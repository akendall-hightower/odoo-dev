from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    is_motorcycle = fields.Boolean(string="Motorcycle", default=False)
    battery_capacity = fields.Selection(selection=[('xs','Small'),
                                        ('0m','Medium'),
                                        ('0l','Larga'),
                                        ('xl','Extra Large'),],
                                        copy=False
                                       )
    charge_time = fields.Float()
    curb_weight = fields.Float()
    horsepower = fields.Float()
    launch_date = fields.Date()
    make = fields.Char()
    model = fields.Char()
    range = fields.Float()
    top_speed = fields.Float()
    torque = fields.Float()
    year = fields.Integer()

    @api.depends('make','model','year')
    def _compute_display_name(self):
        super()._compute_display_name()
        for product in self.filtered("is_motorcycle"):
            product.display_name = f'{product.year} {product.make} {product.model}'
