# Construccion del backend del plugin carrito
class Carro:
    def __init__(self,request):
        # almacenamos la peticion actual para utilizarla mas adelante
        self.request = request
        self.session = request.session
        # igualamos la sesion del usuario con el carro
        cart = self.session.get("cart")
        # si no existe un carro , entonces sera creado
        if not cart:
            cart = self.session["cart"] = {}
        else:
            self.cart=cart

    def agregar(self,producto):
        """

        Funcion encargada de agregar los productos del usuario al Carro


        parametros: self,producto

        retorna:

        """
        if(str(producto.id) not in self.cart.keys()):

            self.cart[producto.id] = {

                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url

            }
