from odoo import models, fields

class MotorcycleRegistry(models.Model):

    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _rec_name = 'registry_number'

    certificate_title = fields.Binary(string='Certificate of Title')
    current_mileage = fields.Float(string='Current Mileage')
    date_registry = fields.Date(string='Date Registry')
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string='Last Name', required=True)
    license_plate = fields.Char(string='License Plate')

    registry_number = fields.Char(string='Registry Number', required=True)

    vin = fields.Char(string='VIN', required=True)
    
    
    # certificate_title = fields.Binary(string='Certificate of Title')