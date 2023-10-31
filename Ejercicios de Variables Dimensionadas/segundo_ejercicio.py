def obtener_domicilios_factura(compras):
    #Uso un conjunto para asegurarme de que cada domicilio aparezca una sola vez.
    domicilios = set()

    for compra in compras:
        cliente, dia, monto, domicilio = compra
        domicilios.add(domicilio)

    #Convierto el conjunto de domicilios de nuevo a una lista
    return list(domicilios)

#Ejemplo para mostrar la funcionalidad de la funcion previamente creada
compras = [('Nuria Costa', 5, 1234.5, 'Calle 1 - 456'), ('Jorge Russo', 7, 3999, 'Calle 2 - 741')]
domicilios_factura = obtener_domicilios_factura(compras)
print(domicilios_factura)
