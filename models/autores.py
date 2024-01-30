# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BaseArchive(models.AbstractModel):
    _name = 'base.archive'
    _description = 'Fichero abstracto'

    activo = fields.Boolean(default=True)

    def archivar(self):
        for record in self:
            record.activo = not record.activo

class LibroAutor(models.Model):
    _name = 'libro.autor'
    _inherit = ['base.archive']
    _description = 'Autores'
    _order = 'fecha_publicacion desc, nombre'

    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required=True, index=True)
    
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)

    portada = fields.Binary('Portada Libro')

    fecha_nacimiento = fields.Date('Fecha nacimiento')

    libro_ids = fields.Many2many('libro')
    saga_ids = fields.Many2many('libro.saga')

    @api.model
    def _referencable_models(self):
        models = self.env['ir.model'].search([('field_id.name', '=', 'message_ids')])
        return [(x.model, x.name) for x in models]

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.nombre, record.fecha_publicacion)
            result.append((record.id, rec_name))
        return result