
from odoo import models, fields, api
from datetime import date

class Libro(models.Model):
    _name = 'libro'
    _description = 'Mis libros'

    isbn = fields.Char(string='ISBN', required=True)
    titulo = fields.Char(string='Título', required=True)
    autor = fields.Char(string='Autor', required=True)
    fecha_publicacion = fields.Date(string='Fecha de publicación', required=True)
    antiguedad = fields.Char(string='Antigüedad', readonly=True, compute='_compute_antiguedad')

    _sql_constraints = [
        ('isbn_unique', 'unique(isbn)', 'El ISBN debe ser único para cada libro.'),
    ]

    @api.depends('fecha_publicacion')
    def _compute_antiguedad(self):
        today = date.today()
        for record in self:
            if record.fecha_publicacion:
                anos = today.year - record.fecha_publicacion.year
                record.antiguedad = f"{anos} años"
            else:
                record.antiguedad = "0 años"