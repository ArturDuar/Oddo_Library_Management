
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Prestamo(models.Model):
    _name = 'prestamo'
    _description = 'Prestamos de libros'

    socio = fields.Many2one('socio', string='Socio', required=True, ondelete='cascade')
    libro = fields.Many2one('libro', string='Libro', required=True, domain="[('estado', '=', 'disponible')]", ondelete='cascade')
    fecha = fields.Date(string='Fecha', required=True, default=fields.Date.today, readonly=True)
    estado = fields.Selection([
        ('activo', 'Activo'),
        ('finalizado', 'Finalizado')
    ], string='Estado', required=True, default='activo')


    @api.constrains('socio')
    def _check_prestamos_activos_socio(self):
        for prestamo in self:
            if prestamo.socio:
                prestamos_count = self.search_count([('socio', '=', prestamo.socio.id), ('estado', '=', 'activo')])
                if prestamos_count > 5:
                    raise ValidationError(_('El socio "%s" ya tiene 5 préstamos activos y no puede tener más.') % prestamo.socio.name)

    @api.model
    def create(self, vals):
        libro_id = vals.get('libro')
        estado = vals.get('estado')

        if libro_id and estado == 'activo':
            prestamos_activos = self.search([
                ('libro', '=', libro_id),
                ('estado', '=', 'activo')
            ])
            if prestamos_activos:
                libro = self.env['libro'].browse(libro_id)
                raise ValidationError(f'El libro "{libro.titulo}" ya tiene un préstamo activo.')

        return super().create(vals)

    def write(self, vals):
        if 'estado' in vals or 'libro' in vals:
            for prestamo in self:
                libro_id = vals.get('libro', prestamo.libro.id)
                estado = vals.get('estado', prestamo.estado)

                if libro_id and estado == 'activo':
                    # Buscar otros prestamos activos del mismo libro excluyendo el actual
                    prestamos_activos = self.search([
                        ('libro', '=', libro_id),
                        ('estado', '=', 'activo'),
                        ('id', '!=', prestamo.id)
                    ])
                    if prestamos_activos:
                        libro = self.env['libro'].browse(libro_id)
                        raise ValidationError(f'El libro "{libro.titulo}" ya tiene un préstamo activo.')

        return super().write(vals)

    def unlink(self):
        libros_a_liberar = self.mapped('libro')
        res = super(Prestamo, self).unlink()
        if libros_a_liberar:
            libros_a_liberar.write({'estado': 'disponible'})
        return res
