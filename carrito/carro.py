


class Carro:

  def __init__(self, request):
    self.request = request
    self.session = request.session
    self.carro = self.session.get("carro", -1)
    if self.carro == -1:
      self.carro = self.session["carro"] = {}

  def guardar(self):
    self.session["carro"] = self.carro
    self.session.modified = True

  def agregar(self, producto, cantidad):
    if producto.id not in self.carro.keys():
      self.carro[producto.id] = {
        "id_producto": producto.id,
        "producto": producto.producto,
        "precio": producto.precio,
        "cantidad": cantidad
      }
    else:
      self.carro[producto.id]["cantidad"] += cantidad
    self.guardar()

  def restar(self, producto, cantidad):
    self.carro[producto.id]["cantidad"] -= cantidad
    if self.carro[producto.id]["cantidad"] <= 0:
      self.eliminar(producto)
    self.guardar()

  def eliminar(self, producto):
    del self.carro[producto.id]
    self.guardar()

  def limpiar(self):
    self.carro = {}
    self.guardar()