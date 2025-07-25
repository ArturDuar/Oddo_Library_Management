
from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

class Libro(models.Model):
    _name = 'libro'
    _description = 'Mis libros'

    isbn = fields.Char(string='ISBN', required=True)
    titulo = fields.Char(string='Título', required=True)
    autor = fields.Char(string='Autor', required=True)
    fecha_publicacion = fields.Date(string='Fecha de publicación', required=True)
    antiguedad = fields.Char(string='Antigüedad', readonly=True, compute='_compute_antiguedad')

    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado')
        ], string='Estado', required=True, default='disponible', readonly=True, compute='_compute_estado_libro')
    
    prestamo_ids = fields.One2many('prestamo', 'libro', string='Préstamos', domain=[('estado', '=', 'activo')])
    prestamo_entregados_ids = fields.One2many('prestamo', 'libro', string='Préstamos entregados', domain=[('estado', '=', 'finalizado')])


    _sql_constraints = [
        ('isbn_unique', 'unique(isbn)', 'El ISBN debe ser único para cada libro.'),
    ]

    @api.depends('prestamo_ids.estado')
    def _compute_estado_libro(self):
        for libro in self:
            prestamos_activos = libro.prestamo_ids.filtered(lambda p: p.estado == 'activo')
            if prestamos_activos:
                libro.estado = 'prestado'
            else:
                libro.estado = 'disponible'

    @api.depends('fecha_publicacion')
    def _compute_antiguedad(self):
        today = date.today()
        for record in self:
            if record.fecha_publicacion:
                anos = today.year - record.fecha_publicacion.year
                record.antiguedad = f"{anos} años"
            else:
                record.antiguedad = "0 años"