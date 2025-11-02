{
    "name": "GS Odoo Mercado Libre (MELI)",
    "version": "15.0.1.0.0",
    "summary": "Sincroniza Productos, Stock, Precios y Mensajes con Mercado Libre.",
    "description": """
        Módulo de integración con la API de Mercado Libre (MELI) para Odoo 15.
        
        Funcionalidades:
        - Configuración y Autenticación OAuth 2.0
        - Sincronización de Productos (Stock y Precio) de Odoo a MELI.
        - Gestión de Preguntas y Respuestas.
    """,
    "author": "Leonardo Valera / Grupo Systematrix",
    "website": "https://www.gruposystematrix.com",
    "category": "Sales/Integration",
    "license": "AGPL-3",
    "depends": [
        "base",
        "base_setup",
        "sale_management",
        "stock",
        "mail",
    ],
    "data": [
        "views/meli_config_settings_views.xml",
        # 'views/product_template_views.xml',
        # 'views/meli_menu_views.xml',
    ],
    "external_dependencies": {
        "python": ["requests"],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}
