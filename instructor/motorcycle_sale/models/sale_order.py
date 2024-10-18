from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    is_new_customer = fields.Boolean('New Customer', compute='_compute_is_new_customer', default=False)

    @api.depends('partner_id')
    def _compute_is_new_customer(self):

        '''
        Only bother computing for draft sale orders.
        '''
        draft_orders = self.filtered(lambda so: so.state in ['draft', 'sent'])
        for order in draft_orders:
            previous_orders = order.partner_id.sale_order_ids.order_line.filtered(lambda sol: sol.order_id.state in ['sale', 'done'])
            previous_motorcycle_orders = previous_orders.filtered(lambda sol: sol.product_template_id.is_motorcycle)
            order.is_new_customer = len(previous_motorcycle_orders) == 0
        for order in self - draft_orders:
            order.is_new_customer = False


    def motorcycle_apply_discount_button(self):
        self.pricelist_id = self.env.ref('motorcycle_sale.new_customer_pricelist')
        super().action_update_prices()