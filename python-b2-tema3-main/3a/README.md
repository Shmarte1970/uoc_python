## Enunciado

Desarrolla un sistema orientado a objetos en Python que permita gestionar productos de diferentes categorías (Libros,
Electrónicos y Ropa) en un pedido. Cada tipo de producto deberá incluir métodos específicos para describir sus
atributos únicos, así como un mecanismo para ajustar y obtener el precio, asegurando que este no sea negativo. El
diagrama UML de las clases a implementar es:

![ULM Diagram](images/UML_ej3a1.png)

Las clases y métodos a implementar son los siguientes:

- Una clase abstracta `Product` que define la estructura básica de un producto, incluyendo su nombre, precio, y un método abstracto `describe_product()` para obtener una descripción del producto.
- Clases concretas `Book`, `Electronic`, y `Clothing` que heredan de `Product` y sobrescriben el método `describe_product()` para incluir detalles específicos de cada tipo de producto, como autor y ISBN para libros, marca y modelo para electrónicos, y talla y color para ropa.
- Un atributo `price` con su respectivo getter y setter en la clase `Product` para obtener y establecer el precio del producto,
con una validación que impide precios negativos.
- Una clase `Order` que permite agregar productos de cualquier tipo a un pedido y calcular el precio total del pedido.

### Ejemplo

```python
order = Order()
order.add_product(Book("The Little Prince", 20, "Antoine de Saint-Exupéry", "978-3-16-148410-0"))
```

### Salida esperada

- El precio total del pedido.
- Una descripción detallada de cada producto en el pedido, incluyendo su categoría, nombre, detalles específicos (como
autor, marca, talla, etc.), y precio.

