# Módulo Personalizado Odoo: Gestión de Biblioteca

Este módulo personalizado permite gestionar libros, préstamos y socios. A continuación se describen los pasos para levantar el entorno con `virtualenv` e instalar o actualizar el módulo.

---

## Requisitos

- Python 3.8 o superior
- PostgreSQL instalado y corriendo
- Odoo 18 (o la versión correspondiente al módulo)
- Git
- Indicaciones sugeridas para entornos Windows

---

## Levantar el entorno con `virtualenv`

1. **Clonar el repositorio del módulo en la carpeta `addons` del proyecto Odoo**

```bash
git clone https://github.com/ArturDuar/Oddo_Library_Management.git
```

2. **En la carpeta raiz del proyecto Odoo, crea el entorno virtual**

```bash
python -m venv venv
venv\Scripts\activate
```
3. **Instala las dependencias de Odoo en este entorno virtual**

```bash
pip install wheel
pip install -r requirements.txt
```


4. **Levanta el servidor Odoo**

```bash
python odoo-bin -r <tu_nombre_usuario> -w <tu_contraseña_usuario> --addons-path=addons -d <base_de_datos_odoo>
```


Listo, el proyecto esta corriendo en `localhost:8069`
Dentro de Apps, puedes buscar el proyecto `Library Management` e instalarlo.
