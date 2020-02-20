# -*- coding: utf-8 -*-

from odoo import models, fields


class primeraclase(models.Model):
    _name = 'primeraclase.primeraclase'
    _description = 'Primera clase Todoo'

    nombre = fields.Char()
    edad = fields.Integer()
#    value2 = fields.Float(compute="_value_pc", store=True)
#    description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
