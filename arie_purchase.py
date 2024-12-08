from odoo import models, fields, _ 

class arie_purchase(models.Model):
    _name = 'arie.purchase'
    
    name = fields.Char(string="Name")
    tanggal = fields.Date(string="Tgl")
    status = fields.Selection([('draf','Draf'),('approve','Approve'),('done','Done')])
    
    
