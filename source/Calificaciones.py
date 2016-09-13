class Calificacion:
	def __init__(self, val, user):
		assert(val<6 and 0<val)
		self.estrellas = val
		self.usuario = user

	def darUsuario(self):
		return self.usuario

	def modificarValor(self,val,user):
		assert(val<6 and 0<val)
		assert(self.usuario == user)
		self.estrellas = val

	def darValor(self):
		return self.estrellas

class Categoria:
	def __init__(self, nombre):
		self.nombre = nombre

	def darNombre(self):
		return self.nombre

# Esto deberìa llamarse tal vez "Categoria"
class RegistroDeCalificacionesPorCategoriaYBar:

	def __init__(self,categoria,bar):
		# assert(bar exite y categoria es valida)
		self.Categoria = categoria
		self.Bar = bar
		self.contenedorDeCalificaciones = []

	def agregarCalificacion(self,calificacion):
		self.contenedorDeCalificaciones.append(calificacion)

	def darPromedio(self):
		valores = [unaCalificacion.darValor() for unaCalificacion in self.contenedorDeCalificaciones]
		return float(sum(valores)) / max(len(self.contenedorDeCalificaciones), 1)

		# que solo tome al usuario
	def quitarCalificacion(self,calificacion):
		assert(calificacion in self.contenedorDeCalificaciones)
		self.contenedorDeCalificaciones.remove(calificacion)

		# que solo tome la calificacion nueva
	def modificarCalificacion(self,calificacionNueva):
		assert(calificacion in self.contenedorDeCalificaciones)
		calificacionVieja = self.buscarCalificacionDeUnUsuario(calificacionNueva.darUsuario)
		self.quitarCalificacion(calificacionVieja)
		self.agregarCalificacion(calificacionNueva)

	def buscarCalificacionDeUnUsuario(self,usuario):
		for calificacion in listaDeCalificaciones:
			if calificacion.darUsuario == usuario:
				return calificacion

	def existeCalificacionDeUnUsuario(self,usuario):
		for calificacion in listaDeCalificaciones:
			if calificacion.darUsuario == usuario:
				return True
		return False

	def darNombre(self):
		return self.nombreDeLaCategoria

#class RegistroDeCategorias:
	# def __init__(self):
	# 	self.categorias = []
	#
	# def agregarCategoria(self, categoria):
	# 	self.categorias.append(categoria)

	#def verCalificacionesDeUnaCategoria(self,categoria):
	#	assert(categoria in categorias)
	#	return categorias[categorias.index(categoria)]

	# def agregarCalificacion(self,categoria,bar,calificacion):
	# 	assert(categoria in categorias)
	# 	categorias[categorias.index(categoria)].agregarCalificacion(bar,calificacion)
	#
	# def eliminarCalificacion(self,categoria,bar,calificacion):
	# 	assert(categoria in categorias)
	# 	categorias[categorias.index(categoria)].quitarCalificacion(bar,calificacion)
	#
	# def existeCalificacionDeUnUsuario(self,categoria,bar,usuario):
	# 	assert(categoria in categorias)
	# 	categorias[categorias.index(categoria)].existeCalificacionDeUnUsuario(bar,usuario)
	#
	# def modificarCalificacion(self,categoria,bar,calificacion):
	# 	self.eliminarCalificacion(categoria,bar,calificacion)
	# 	self.agregarCalificacion(categoria,bar,calificacion)
