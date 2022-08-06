# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HeatQuery(models.Model):
    _name = 'heat.query'
    _rec_name = 'name'
    _description = '热量查询'

    category = fields.Char('类别')
    name = fields.Char('食物')
    currency_id = fields.Many2one('res.currency', string='单位', default=lambda self: self.env.company.currency_id.id)
    price = fields.Monetary('价格', currency_field='currency_id')
    gram = fields.Char('克数')
    heat = fields.Char('热量')
    protein = fields.Char('蛋白质')
    carbohydrate = fields.Char('碳水化合物')
    diet_id = fields.Many2one('diet.record', string='食物记录')



