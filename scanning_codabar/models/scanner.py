from odoo import models, fields, api
from odoo.exceptions import UserError

class Scanner(models.Model):
    _name = 'scanner.scanner'
    _description = 'Scanner Codabar'

    barcode = fields.Char(string='Codabar', required=False)
    price = fields.Float(string='Price', readonly=True)
    name = fields.Char(string='Name', readonly=True)

    @api.onchange('barcode')
    def _onchange_barcode(self):
        if self.barcode:
            # Cari data berdasarkan generate_code
            generate_code_record = self.env['barcode.generator.line'].search([
                ('generate_code', '=', self.barcode)  # Ganti 'generate_code' dengan nama field yang benar
            ], limit=1)
            
            if generate_code_record:
                self.price = generate_code_record.price
                self.name = generate_code_record.name

                # Buat record baru di model scanner.scanner
                self.env['scanner.scanner'].create({
                    'barcode': self.barcode,
                    'price': self.price,
                    'name': self.name
                })
            else:
                # Jika tidak ditemukan, tampilkan popup dengan pesan
                raise UserError('Data tidak ditemukan untuk barcode: %s' % self.barcode)

            # if generate_code_record:
            #     self.price = generate_code_record.price
            #     self.name = generate_code_record.name
            # else:
            #     self.price = 0.0
            #     self.name = ''
                
            # # Buat record baru di model scanner.scanner
            # self.env['scanner.scanner'].create({
            #     'barcode': self.barcode,
            #     'price': price,
            #     'name': name
            # })
                
            # Kosongkan input barcode setelah proses selesai
            self.barcode = ''
