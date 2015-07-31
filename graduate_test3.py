from openerp import models, fields

class Graduate(models.Model):
    _name = 'graduate.course'

    name = fields.Char(string='Name', required=True)
    section = fields.Selection([('trainee', 'Training'), ('perm', 'Project')], string='Section', required=True)