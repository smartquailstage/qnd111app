from django.templatetags.static import static
from django.urls import reverse, path
from django.utils.html import format_html
from wagtail import hooks
from wagtail.admin.menu import MenuItem

# Elimina imports innecesarios o duplicados
# from wagtail_modeladmin.menus import SubMenu  # ❌ No se usa
# from django.urls import reverse, include  # ❌ ya está importado
# from django.template.loader import render_to_string  # ❌ No usado
# from shop.admin import CategoryAdmin  # ❌ No usado
# Asegúrate de tener definido el view `index` que usas más abajo

# 1. Añadir URL personalizada (si tienes definida la vista `index`)
@hooks.register('register_category_url')  # ⚠️ Este hook no es válido en Wagtail; probablemente querías 'register_admin_urls'
def register_category_url():
    return [
        path('ecommerce/', index, name='ecommerce'),
    ]

# ✅ Correcto: añadir CSS personalizado al admin
@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static("css/custom.css"))

# ✅ Añadir un nuevo item al menú del admin de Wagtail
@hooks.register('register_admin_menu_item')
def register_custom_menu_item():
    url = reverse('wagtailadmin_home')
    return MenuItem(
        'Dashboard',
        url,
        classname='icon icon-tasks',  # ✅ corregido: debe ser "classname", no "classnames"
        order=100
    )
