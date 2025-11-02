# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    """
    Heredamos el modelo de ajustes de Odoo (res.config.settings)
    para añadir nuestros campos de configuración de la API de MELI.
    """

    _inherit = "res.config.settings"

    # Definimos los campos que queremos en la vista de Ajustes
    meli_app_id = fields.Char(
        string="MELI App ID",
        config_parameter="meli.app_id",
        help="App ID proporcionado por Mercado Libre Developers.",
    )

    meli_client_secret = fields.Char(
        string="MELI Client Secret",
        config_parameter="meli.client_secret",
        help="Client Secret proporcionado por Mercado Libre Developers.",
        password=True,  # Para ocultar el valor en la interfaz
    )
