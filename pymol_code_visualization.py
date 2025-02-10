#buena practica partir con esto, limpia todo, removiendo estructuras cargadas anteriormente
reinit 

#OBTENER ESTRUCTURA
# async 0 por lo general no es necesario, pero detiene ejecucion de lo otro mientras se carga
fetch 1J95, kchannel, async=0 

#ESTABLECIENDO SELECCIONES (depende de lo que se quiere resaltar)

#creamos seleccion con create y llamamos sfilter a la seleccion
create SFilter, resi 75-80 

#seleccionamos los iones potasio y nombramos la seleccion k
select k, name k

#borrar cuadrados de seleccion 
deselect 

#VISUALIZAR
#elimina ligando que no nos enfocamos
remove resn TBA 

#color de acuerdo a la cadena (color by chain), hay 3 iones en 1 cadena y otro en otra
util.cbc 

#cambiamos la visualizacion a stick, en vez de que quede stick sobre la representacion. por eso se definio sfilter como objeto en vez de una seleccion
#si lo dejamos como seleccion este comando hubiese creado agujeros visibles en la cadena principal
as stick, SFilter 

#coloreamos toda la representacion como blanco, pero no es 1 buena visualizacion
#si quiero ver insteracciones polares, por lo que necesitamos ver los elementos
color white, SFilter 

#colorea por atomo (color by atom), pero carbonos deben ser blancos (w)
util.cbaw SFilter

util.cbaw k

#ORIENTACION

#con get_view vemos la posicion de la molecula que en pymol obtuvimos con action -> orient
set_view (\
     0.362904966,    0.465746939,    0.807081044,\
    -0.000884769,   -0.865955830,    0.500119984,\
     0.931825757,   -0.182210088,   -0.313847572,\
     0.000000000,    0.000000000, -208.887161255,\
    72.113220215,   27.030769348,   19.742210388,\
   178.243988037,  239.530334473,  -20.000000000 )
### cut above here and paste into script ###


#GUARDAR ESCENA
#guardamos la escena con nombre F1, este sera el punto de partida para la proxima escena
scene F1, store

#NUEVA ESCENA, interaccion con 1 solo ion K
hide sticks, SFilter
create kcomplex, resi 77+78+201
as sticks, kcomplex
util.cbaw kcomplex
hide sphere, resi 202-204

scene F2, store

#cambiando color de fondo
bg_color white

