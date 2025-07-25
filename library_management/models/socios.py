
from odoo import models, fields, api
import random
import string

class Socio(models.Model):
    _name = 'socio'
    _description = 'Mis socios'

    codigo = fields.Char(string='Código', readonly=True, copy=False)
    name = fields.Char(string='Nombre', required=True)
    fecha_alta = fields.Date(string='Fecha de alta', readonly=True, default=fields.Date.context_today) 

    @api.model
    def create(self, vals):
        # Generar código aleatorio si no está definido
        if 'codigo' not in vals or not vals['codigo']:
            vals['codigo'] = self._generar_codigo_aleatorio()
        return super(Socio, self).create(vals)
    
    def _generar_codigo_aleatorio(self, longitud=8):
        letras_numeros = string.ascii_uppercase + string.digits
        return ''.join(random.choices(letras_numeros, k=longitud))