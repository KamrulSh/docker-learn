import base64

from odoo import models, fields, api


class EffortTimesheet(models.Model):
    _name = 'effort.timesheet'
    _description = 'Here effort timesheet information is stored.'

    employee_id = fields.Many2one('hr.employee', string="Employee")

    # salary = fields.Char("Salary", editable=True, compute='_compute_salary')
    # provident_fund = fields.Char("Provident fund", editable=True, compute='_compute_pf')

    salary = fields.Char("Salary", store=True, compute='_compute_salary', inverse='_decrypt_salary')
    provident_fund = fields.Char("Provident fund", store=True, compute='_compute_pf', inverse='_decrypt_pf')

    def encrypt(self, message):
        print(f"Encrypting: {message}")
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        # base64_message = str(message) + "0000000000000000"
        print(f"Encrypted: {base64_message}")
        return base64_message

    def decrypt(self, base64_message):
        print(f"Decrypting: {base64_message}")
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        # message = base64_message[::-1]
        print(f"Decrypted: {message}")
        return message

    @api.depends('salary')
    def _compute_salary(self):
        print("----- entered_salary")
        # base64_sa = self.decrypt(self.salary)
        # print(f"Enc Salary string: {base64_sa}")
        # self.salary = str(base64_sa)
        # self.write({'salary': base64_sa})

        for rec in self:
            base64_sa = self.decrypt(rec.salary) if rec.salary else None
            print(f"Enc Salary string: {base64_sa}")
            rec.salary = str(base64_sa)

    @api.depends('provident_fund')
    def _compute_pf(self):
        print("----- entered_prov_fund")
        # base64_pf = self.decrypt(self.provident_fund)
        # print(f"Enc PF string: {base64_pf}")
        # self.provident_fund = str(base64_pf)
        # self.write({'provident_fund': base64_pf})

        for rec in self:
            base64_pf = self.decrypt(rec.provident_fund) if rec.provident_fund else None
            print(f"Enc PF string: {base64_pf}")
            rec.provident_fund = str(base64_pf)

    def _decrypt_salary(self):
        print("+++++ entered_salary 1")
        # pass
        for rec in self:
            salary_string = self.encrypt(rec.salary) if rec.salary else None
            print(f"Dec salary string: {salary_string}")
            rec.salary = salary_string

            base64_sa = self.decrypt(rec.salary) if rec.salary else None
            print(f"Enc Salary string: {base64_sa}")
            rec.salary = str(base64_sa)

    def _decrypt_pf(self):
        print("+++++ entered_prov_fund 1")
        # pass
        for rec in self:
            pf_string = self.encrypt(rec.provident_fund) if rec.provident_fund else None
            print(f"Dec PF string: {pf_string}")
            rec.provident_fund = pf_string
