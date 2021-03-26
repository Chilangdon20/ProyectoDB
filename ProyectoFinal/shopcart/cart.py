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

        # en caso de no existir un producto, debe ser agregado con las caracteristicas
        # dentro del bucle.
        if(str(producto.id) not in self.cart.keys()):

            self.cart[producto.id] = {

                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url

            }
        else:
            # recorremos los valors almacenados en el dict y comprobar
            # si la clave corresponde a la del usuario , en ste caso para dicha clave
            # la cantidad se aumenta en Funcion
            for key,value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    break
        self.guardar_carro()

        def guardar_carro(self):
            """
            Funcion encargada de ir actualizando la session
            en caso de que sea agregado un producto o eliminado.

            paramtetros: self

            retorna:


            """

            self.session["carro"]=self.carro

            self.session.modified=True

        def eliminar(self,producto):
            """
             Funcion encargada de eliminar un producto y actualizarlo

             parametros: self, producto
            """
            producto.id=str(producto.id)
            if producto.id in self.carro:
                del self.carro[producto.id]
                self.guardar_carro()

        def restar_producto(self,producto):
            for key,value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break
            self.guardar_carro()

        def limpiar_carro(self):
            self.session["carro"]={}
            self.session.modified=True
