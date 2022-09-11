

def importe_carro(request):
  total = 0
  cantidadTotal = 0
  carrito = {}
  if request.user.is_authenticated:#Si esta autenticado
    carrito = request.session.get("carro", {})
    for _, value in carrito.items():
      cantidadTotal += value["cantidad"]
      total += value["monto"]
  else: #Si no esta autenticado crea un session anonima
    carrito = request.session.get("carro", {})
    for _, value in carrito.items():
      cantidadTotal += value["cantidad"]
      total += value["monto"]
  costo_envio = round(total * 0.03, 2)
  return {"subtotal": total,"cantidad_total_productos": cantidadTotal, "costo_envio": costo_envio, "total": round(total + costo_envio, 2),"data_producto": carrito}