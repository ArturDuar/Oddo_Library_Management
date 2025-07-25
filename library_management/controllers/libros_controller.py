
from odoo import http
from odoo.http import request, Response
import json

class LibrosController(http.Controller):
    @http.route('/api/libros', type='http', auth='public', methods=['GET'], csrf=False)
    def get_libros(self, **kwargs):
        isbn = kwargs.get('isbn')
        domain = []
        if isbn:
            domain = [('isbn', '=', isbn)]
        
        libros = request.env['libro'].sudo().search(domain)
        
        if not libros:
            data = {'status': 404, 'message': 'Libro no encontrado'}
            return request.make_response(
                json.dumps(data),
                headers=[('Content-Type', 'application/json')],
                status=404
            )

        resultado = [{
            'id': libro.id,
            'titulo': libro.titulo,
            'autor': libro.autor,
            'isbn': libro.isbn,
            'estado': libro.estado,
            'antiguedad': libro.antiguedad,
            'fecha_publicacion': str(libro.fecha_publicacion)
        } for libro in libros]

        data = {
            'status': 200,
            'message': 'Libro encontrado',
            'data': resultado
        }

        return request.make_response(
            json.dumps(data),
            headers=[('Content-Type', 'application/json')],
            status=200
        )