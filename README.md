# Repo DIF

Aplicación web desarrollada con Django y Tailwind CSS. El proyecto utiliza una arquitectura modular basada en aplicaciones Django y una estructura independiente para la gestión de estilos y recursos estáticos.

## Tecnologías

| Tecnología       | Versión |
| ---------------- | ------- |
| Python           | 3.14.7  |
| Django           | 6.1     |
| Node.js          | 24.20.0 |
| Tailwind CSS     | 4.3.3   |
| Tailwind CSS CLI | 4.3.3   |
| Base de datos    | SQLite  |

## Requisitos

Antes de iniciar el proyecto, es necesario contar con:

* Python 3.14 o superior
* Node.js y npm
* Git
* Entorno virtual de Python

## Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd repo_dif
```

### 2. Crear el entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

En Git Bash:

```bash
source venv/Scripts/activate
```

### 4. Instalar las dependencias de Python

```bash
pip install -r requirements.txt
```

Si el archivo `requirements.txt` todavía no existe:

```bash
pip freeze > requirements.txt
```

## Configuración de Django

El proyecto utiliza `config` como módulo principal de configuración y `core` como aplicación principal.

La estructura de las URLs se encuentra en:

```text
config/urls.py
```

La vista principal está definida en:

```text
core/views.py
```

La plantilla principal se encuentra en:

```text
templates/home.html
```

La aplicación `core` debe estar incluida en `INSTALLED_APPS`.

## Configuración de archivos estáticos

En `config/settings.py` se utiliza la siguiente configuración:

```python
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

La estructura de archivos estáticos es:

```text
static/
├── css/
│   └── output.css
└── src/
    └── input.css
```

## Tailwind CSS

El proyecto utiliza Tailwind CSS 4 mediante `@tailwindcss/cli`.

El archivo de entrada es:

```text
static/src/input.css
```

Contenido:

```css
@import "tailwindcss";

@source "../../templates";
@source "../../core";
```

El archivo generado por Tailwind es:

```text
static/css/output.css
```

### Instalación de Tailwind

Las dependencias de Node se instalan mediante:

```bash
npm install
```

### Compilación durante el desarrollo

Para mantener Tailwind observando los cambios:

```bash
npm run dev
```

Este comando recompila automáticamente `output.css` cuando se modifican archivos dentro de las rutas configuradas.

### Compilación para producción

Para generar el CSS sin modo `watch`:

```bash
npx @tailwindcss/cli -i ./static/src/input.css -o ./static/css/output.css
```

## Integración con las plantillas

Las plantillas Django deben cargar los archivos estáticos mediante:

```django
{% load static %}
```

Y posteriormente importar el CSS generado:

```html
<link rel="stylesheet" href="{% static 'css/output.css' %}">
```

## Ejecución del proyecto

Durante el desarrollo se recomienda utilizar dos terminales.

### Terminal 1: Tailwind

Con el entorno de Node configurado:

```bash
npm run dev
```

### Terminal 2: Django

Con el entorno virtual activado:

```bash
python manage.py runserver
```

El servidor estará disponible normalmente en:

```text
http://127.0.0.1:8000/
```

## Estructura del proyecto

```text
repo_dif/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── core/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── static/
│   ├── css/
│   │   └── output.css
│   └── src/
│       └── input.css
│
├── templates/
│   └── home.html
│
├── venv/
│
├── manage.py
├── package.json
├── package-lock.json
├── requirements.txt
└── README.md
```

## Comandos principales

### Django

Verificar la configuración del proyecto:

```bash
python manage.py check
```

Ejecutar el servidor:

```bash
python manage.py runserver
```

Crear migraciones:

```bash
python manage.py makemigrations
```

Aplicar migraciones:

```bash
python manage.py migrate
```

Crear un superusuario:

```bash
python manage.py createsuperuser
```

### Node.js

Instalar dependencias:

```bash
npm install
```

Ejecutar Tailwind en modo desarrollo:

```bash
npm run dev
```

## Control de versiones

Los siguientes elementos no deben incluirse en el repositorio:

```text
venv/
node_modules/
__pycache__/
*.pyc
.env
```

El archivo `output.css` puede generarse automáticamente mediante Tailwind, por lo que su inclusión en Git debe definirse según la estrategia de despliegue del proyecto.

## Variables de entorno

Las credenciales y configuraciones sensibles deben mantenerse fuera del código fuente.

Se recomienda utilizar un archivo:

```text
.env
```

Ejemplo:

```env
DEBUG=True
SECRET_KEY=your-secret-key
```

El archivo `.env` debe incluirse en `.gitignore`.

## Estado actual

El proyecto cuenta actualmente con:

* Django configurado y operativo.
* Aplicación `core` integrada.
* Sistema de templates configurado.
* Archivos estáticos configurados.
* Tailwind CSS 4 integrado.
* Compilación automática de Tailwind mediante `npm run dev`.
* Vista principal disponible desde la ruta `/`.
* Configuración preparada para continuar con el desarrollo de la aplicación.

## Desarrollo

Para iniciar el entorno de desarrollo:

```bash
# Terminal 1
npm run dev

# Terminal 2
python manage.py runserver
```

A partir de esta configuración, el desarrollo de las vistas puede realizarse mediante Django Templates y Tailwind CSS, manteniendo separadas la lógica de aplicación y la presentación.
