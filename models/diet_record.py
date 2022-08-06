# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DietRecord(models.Model):
    _name = 'diet.record'
    _rec_name = 'category'
    _description = '饮食记录'

    weight_id = fields.Many2one('weight.record', string='体重记录')
    category = fields.Selection([('breakfast', '早餐'),
                                 ('lunch', '午餐'),
                                 ('dinner', '晚餐'),
                                 ('am_extra_meal', '上午加餐'),
                                 ('pm_extra_meal', '下午加餐')], string='类别')
    food = fields.One2many('heat.query', 'diet_id', string='食物')
    total_heat = fields.Integer('总热量')

    # 添加模型属性来创建数据库约束
    _sql_constraints = [
        ('category_uniq', 'unique(category)', '种类已存在！'),
    ]

    def compute_inventory(self):
        pass



