Proyecto final
Alumno: Giraudo Sebastián

Aplicación de gestión de un centro médico multidiciplinario.

Objetivo de la aplicación: permitir la administración y gestión de información de los recursos disponibles.

Usuario administrador: nombre de usuario = admin / contraseña = 12345
Usuario creado en video: nombre de usuario = Sebastian/ contraseña = Seba-12345


Los modelos que presenta esta aplicación son:
- Consultorios
- Especialidades
- Pacientes
- Profesionales

Siempre que se quiera volver a la página inicio, el botón de home (ubicado en la barra superior) lo redireccionará.

Para cerrar sesión, presionar el boton "Cerrar sesión" ubicado en la barra superior.

Registro en aplicación:
- Registro de usuario: http://127.0.0.1:8000/aplicacion/registro/

Login en aplicacion:
- Login: http://127.0.0.1:8000/aplicacion/login/
- Usuario creado: nombre de usuario = admin / contraseña = 12345
- Una vez logueado, se redirige al html del home

Consultar contenido de los modelos (tocar los botones de la página home correspondiente a la categoría a consultar):
- Consultar todos los consultorios:   http://127.0.0.1:8000/aplicacion/consultorios/
- Consultar todas las especialidades: http://127.0.0.1:8000/aplicacion/especialidades/
- Consultar todas los pacientes:      http://127.0.0.1:8000/aplicacion/pacientes/
- Consultar todos los profesionales:  http://127.0.0.1:8000/aplicacion/profesionales/
En cada categoría se muestra el listado de todos los registros ingresados en una tabla.

Agregar contenido en cada uno de los modelos (tocar el boton de agregar correspondiente a cada modelo):
- Agregar consultorios:   http://127.0.0.1:8000/aplicacion/consultorio_create/ 
- Agregar especialidades: http://127.0.0.1:8000/aplicacion/especialidad_create/
- Agregar pacientes:      http://127.0.0.1:8000/aplicacion/paciente_create/
- Agregar profesionales:  http://127.0.0.1:8000/aplicacion/profesional_create/

Editar contenido de las tablas en cada uno de los modelos (tocar el botón azul de edición en la columna acciones de la tabla):

- Edición de contenido en tabla de consultorios: http://127.0.0.1:8000/aplicacion/consultorio_update/1/
- Edición de contenido en tabla de especialidades: http://127.0.0.1:8000/aplicacion/especialidad_update/1/
- Edición de contenido en tabla de pacientes: http://127.0.0.1:8000/aplicacion/paciente_update/1/
- Edición de contenido en tabla de profesionales: http://127.0.0.1:8000/aplicacion/profesional_update/1/

Eliminar contenido de las tablas en cada uno de los modelos (tocar el botón rojo de borrar en la columna acciones de la tabla):
- Eliminar contenido en tabla de consultorios:   http://127.0.0.1:8000/aplicacion/consultorio_delete/1/
- Eliminar contenido en tabla de especialidades: http://127.0.0.1:8000/aplicacion/especialidad_delete/1/
- Eliminar contenido en tabla de pacientes:      http://127.0.0.1:8000/aplicacion/paciente_delete/1/
- Eliminar contenido en tabla de profesionales:  http://127.0.0.1:8000/aplicacion/profesional_delete/1/

Busqueda en los modelos por el patrón nombre (por medio de los botones de busqueda en cada modelo o en el home):
- Busqueda de consultorios:  http://127.0.0.1:8000/aplicacion/buscar/
- Busqueda de especilidades: http://127.0.0.1:8000/aplicacion/buscar/
- Busqueda de pacientes:     http://127.0.0.1:8000/aplicacion/buscar/
- Busqueda de profesionales: http://127.0.0.1:8000/aplicacion/buscar/

Editar perfil de usuario:
- http://127.0.0.1:8000/aplicacion/editar_perfil/

Editar imagen de perfil (presionar sobre la imagen cargada por defecto junto al saludo en la barra superior):
- http://127.0.0.1:8000/aplicacion/agregar_avatar/