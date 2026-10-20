# POO · Gestión de clientes de un banco

Actividad de clases abstractas, herencia y polimorfismo. El programa administra una lista de clientes y permite operar con dos tipos de cuenta.

## Consigna

Definir una clase base de cliente y especializarla en clientes estándar y Gold. Representar nombre, identificador y saldo; implementar depósitos, extracciones y una presentación de cada cliente. El banco debe permitir altas y un listado que utilice el comportamiento de cada clase.

La práctica agrega búsqueda, cambio de nombre y baja para recorrer el ciclo de gestión de la lista.

## Ejecutar

Desde la raíz del repositorio:

```console
python Python/06-poo/Banco/banco.py
python -m unittest discover -s pruebas -v
```

## Diseño

- `cliente.py`: base abstracta y especializaciones estándar y Gold.
- `banco.py`: colección de clientes y demostración de operaciones.
- Los identificadores son locales, crecientes y no se reutilizan después de una baja.
- El cliente estándar no puede quedar con saldo negativo; Gold permite descubierto hasta su límite configurado.
- Los importes usan Decimal con hasta dos decimales. Los depósitos y extracciones deben ser positivos.
- Los datos son ficticios y viven en memoria. La práctica no implementa transferencias, intereses ni persistencia.

Las pruebas cubren operaciones válidas e inválidas, límites, polimorfismo, identificadores y gestión de la lista.
