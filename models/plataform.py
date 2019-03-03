db = DAL("sqlite://storage.sqlite")

db.define_table('juego',
    Field('nombre', 'string', unique=True),
    Field('url', 'string', unique=True),
    Field('descripcion', 'text'),
    Field('portada', 'upload')
    )

db.define_table('jugador',
    Field('nick', 'string', unique=True),
    Field('correo', 'string')
    )

db.define_table('puntaje',
    Field('jugador_id', 'reference jugador'),
    Field('juego_id', 'reference juego'),
    Field('puntos', 'integer'),
    Field('fecha', 'date')
    )

db.jugador.correo.requires = IS_EMAIL()
db.juego.descripcion.requires = IS_NOT_EMPTY()