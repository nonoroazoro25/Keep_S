# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WeightRecord(models.Model):
    _name = 'weight.record'
    _rec_name = 'weight'
    _order = 'create_date'
    _description = '体重记录'

    user_id = fields.Many2one('res.users', default=lambda self: self.env.user.id, string='用户')
    # digits: 可配置精度的浮点字段
    weight = fields.Float('体重', copy=False, digits="weight record")
    chest_circumference = fields.Float('胸围')
    waistline = fields.Float('腰围')
    thigh_circumference = fields.Float('大腿围')
    calf_circumference = fields.Float('小腿围')
    bmi = fields.Char('BMI')
    # to do: 关系字段中的各种字段属性
    diet_ids = fields.One2many('diet.record', 'weight_id', string='饮食记录')
    photo = fields.Binary(string='每日照片')
    remark = fields.Text('备注')
    state = fields.Selection([('draft', '草稿'),
                                 ('losing', '减脂'),
                                 ('shape', '塑形'),
                                 ('success', '成功')], string='状态', default='draft')

    def confirm(self):
        self.state = 'losing'


