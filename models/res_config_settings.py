# -*- coding: utf-8 -*-

from odoo import models, fields, api

# -*- coding: utf-8 -*-

# Añade 'urllib' al inicio para construir URLs
import urllib.parse

from odoo import models, fields, api
from odoo.exceptions import UserError  # Para mostrar mensajes de error


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    meli_app_id = fields.Char(
        string="MELI App ID",
        config_parameter="meli.app_id",
        help="App ID proporcionado por Mercado Libre Developers.",
    )

    meli_client_secret = fields.Char(
        string="MELI Client Secret",
        config_parameter="meli.client_secret",
        help="Client Secret proporcionado por Mercado Libre Developers.",
        password=True,
    )

    # --- AÑADE ESTE NUEVO CAMPO ---
    meli_redirect_uri = fields.Char(
        string="MELI Redirect URI",
        config_parameter="meli.redirect_uri",
        help="La URL de Callback registrada en tu aplicación de MELI.",
    )

    # --- AÑADE ESTE NUEVO MÉTODO ---
    def button_meli_authorize(self):
        """
        Este método se llama desde un botón en la vista.
        Redirige al usuario a la página de autorización de MELI.
        """
        # Asegúrate de que los valores estén guardados antes de usarlos
        if not self.meli_app_id or not self.meli_redirect_uri:
            raise UserError(
                "Debes guardar el 'App ID' y la 'Redirect URI' antes de autorizar."
            )

        # URL de autorización de MELI (para Argentina, cambia '.ar' si es otro país)
        auth_url_base = "https://auth.mercadolibre.com.ar/authorization"

        # Parámetros para la URL
        params = {
            "response_type": "code",
            "client_id": self.meli_app_id,
            "redirect_uri": self.meli_redirect_uri,
        }

        # Construimos la URL completa
        query_string = urllib.parse.urlencode(params)
        auth_url = f"{auth_url_base}?{query_string}"

        # Devolvemos una acción de Odoo que redirige el navegador del usuario
        return {
            "type": "ir.actions.act_url",
            "url": auth_url,
            "target": "new",  # Abre en una nueva pestaña
        }
