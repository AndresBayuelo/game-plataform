
def index():
    juegos = db().select(db.juego.ALL, orderby=db.juego.nombre)
    jugadores = db().select(db.jugador.ALL, orderby=db.jugador.nick)
    return dict(data=[juegos, jugadores])

def agregarJuego():
    form = SQLFORM(db.juego)
    if form.process().accepted:
        response.flash = 'Juego registrado'
    return dict(form=form)

def jugadores():
    jugadores = db().select(db.jugador.ALL, orderby=db.jugador.nick)
    return dict(jugadores=jugadores)

def agregarJugador():
    form = SQLFORM(db.jugador)
    if form.accepts(request, formname=None):
        return DIV("Juagador registrado!", _class="alert alert-success")
    elif form.errors:
        return DIV(*[(campo, valor) for campo, valor in form.errors.items()], _class="alert alert-danger")

def seleccionJugador():
    session.jugador = request.vars.jugador
    session.juego = request.vars.juego
    return dict()

def registrarPuntuacion():
    import time
    db.puntaje.insert(jugador_id=session.jugador, juego_id=session.juego, puntos=request.get_vars.puntaje, fecha=time.strftime("%y-%m-%d"))
    return dict()

def puntuaciones():
    registros = db((db.jugador.id == db.puntaje.jugador_id) & (db.juego.id == db.puntaje.juego_id)).select()
    return dict(puntuaciones=registros)

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)