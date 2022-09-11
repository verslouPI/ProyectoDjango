


class Carro:

  def __init__(self, request):
    self.session = request.session
    self.carro = self.session.get("carro", -1)
    if self.carro == -1:
      self.carro = self.session["carro"] = {}

  def guardar(self):
    #for _, value in self.carro.items():
    #  value["imagen"] = str(value["imagen"])
    #  value["precio"] = float(value["precio"])
    #  value["monto"] = float(value["monto"])

    self.session["carro"] = self.carro
    self.session.modified = True

  def agregar(self, producto, cantidad):
    producto.id= str(producto.id)
    if cantidad > 0:
      if producto.id not in self.carro.keys():
        self.carro[producto.id] = {
          "id": producto.id,
          "producto": producto.producto,
          "categoria":str(producto.categoria),
          "precio": float(producto.precio),
          "imagen": f"/media/{str(producto.imagen)}",
          "cantidad": cantidad
        }
      else:
        self.carro[producto.id]["cantidad"] += cantidad
      self.carro[producto.id]["monto"] = self.carro[producto.id]["precio"] * self.carro[producto.id]["cantidad"]
      self.guardar()

  def sumar(self, producto):
    producto.id= str(producto.id)
    self.carro[producto.id]["cantidad"] += 1
    self.carro[producto.id]["monto"] = self.carro[producto.id]["precio"] * self.carro[producto.id]["cantidad"]
    self.guardar()

  def restar(self, producto):
    producto.id= str(producto.id)
    self.carro[producto.id]["cantidad"] -= 1
    if self.carro[producto.id]["cantidad"] <= 0:
      self.eliminar(producto)
    else:
      self.carro[producto.id]["monto"] = self.carro[producto.id]["precio"] * self.carro[producto.id]["cantidad"]
    self.guardar()

  def eliminar(self, producto):
    del self.carro[str(producto.id)]
    self.guardar()

  def limpiar(self):
    self.carro = {}
    self.guardar()