# -*- coding: utf-8 -*-
# from odoo import http


# class WeightManagement(http.Controller):
#     @http.route('/weight_management/weight_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/weight_management/weight_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('weight_management.listing', {
#             'root': '/weight_management/weight_management',
#             'objects': http.request.env['weight_management.weight_management'].search([]),
#         })

#     @http.route('/weight_management/weight_management/objects/<model("weight_management.weight_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('weight_management.object', {
#             'object': obj
#         })
