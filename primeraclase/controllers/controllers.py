# -*- coding: utf-8 -*-
# from odoo import http


# class Primeraclase(http.Controller):
#     @http.route('/primeraclase/primeraclase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/primeraclase/primeraclase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('primeraclase.listing', {
#             'root': '/primeraclase/primeraclase',
#             'objects': http.request.env['primeraclase.primeraclase'].search([]),
#         })

#     @http.route('/primeraclase/primeraclase/objects/<model("primeraclase.primeraclase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('primeraclase.object', {
#             'object': obj
#         })
