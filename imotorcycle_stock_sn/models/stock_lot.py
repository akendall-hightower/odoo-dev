from odoo import api, fields, models


class StockLot(models.Model):
    _inherit = "stock.lot"

    @api.depends('product_id')
    def _compute_display_name(self):
        super()._compute_display_name()
        for lot in self:
            tmpl = lot.product_id.product_tmpl_id
            if tmpl.is_motorcycle and lot.product_id.is_storable:
                make = tmpl.make[:2].upper() if tmpl.make else 'XX'
                model = tmpl.model[:2].upper() if tmpl.model else 'XX'
                year = str(tmpl.year)[-2:] if tmpl.year else '00'
                battery_capacity = tmpl.battery_capacity[:2].upper() if tmpl.battery_capacity else 'XX'
                serial_number = self.env["ir.sequence"].next_by_code("kawiil.serial")

                lot.display_name = f"{make}{model}{year:02}{battery_capacity}{serial_number}"

                