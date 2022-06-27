from datetime import datetime, time
from email.policy import default

from dateutil.rrule import rrule, DAILY
from odoo import models, fields, api
from pytz import UTC


class EffortTimesheet(models.Model):
    _name = 'effort.timesheet'
    _description = 'Here effort timesheet information is stored.'

    encrypted = fields.Encrypted()

    duration = fields.Float("Duration", encrypt='encrypted', default=10)
    price_unit = fields.Float(encrypt='encrypted', default=22)
    price_unit2 = fields.Float(encrypt='encrypted', default=1334)
    price_unit3 = fields.Integer(encrypt='encrypted', default=1434543)
    price_unit4 = fields.Float(encrypt='encrypted', default=13334)
    price_unit5 = fields.Boolean(encrypt='encrypted', default=True)
    my_selection = fields.Selection([('option1', 'Label 1'), ('option2', 'Label 2')], string='My Selection Field', encrypt='encrypted')
