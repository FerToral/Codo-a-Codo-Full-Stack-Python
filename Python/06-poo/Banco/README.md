# POO: gestión de clientes de un banco

Actividad opcional de Codo a Codo Full Stack Python: clases abstractas, herencia, polimorfismo, listas y métodos especiales. La [carpeta de material del curso](https://drive.google.com/drive/folders/1Fpgw944KMCjIpe4xY1KBQU8MWZISmCQ-) conserva la consigna **Actividad Opcional POO Banco** y sus ejemplos.

Esta es una **propuesta nueva de resolución de 2026**, basada en esa consigna. No se presenta como entrega histórica ni como proyecto final del curso. Los ejemplos docentes originales se preservan por separado y no se copian como código propio.

```sh
python Python/06-poo/Banco/banco.py
python -m unittest discover -s pruebas -v
```

- `cliente.py`: base abstracta, clientes estándar y Gold, saldo consultable y operaciones.
- `banco.py`: altas y listado polimórfico; extras de búsqueda, cambio de nombre y baja.
- Datos ficticios, sólo en memoria. No se persisten identidades ni se conectan servicios.
- Identificadores locales al banco, crecientes y no reutilizados. Los nombres pueden coincidir.
- Para concretar el descubierto de Gold, el cliente estándar no admite saldo negativo y Gold permite bajar hasta el límite configurado; se explicita esta decisión porque la consigna enumera clases pero no detalla todas las reglas.
- Importes didácticos positivos con hasta dos decimales, tratados con Decimal. Sin intereses, transferencias, concurrencia ni pretensión de software financiero real.

Ocho pruebas cubren abstracción, polimorfismo, operaciones válidas/erróneas, límites, identificadores, búsquedas, bajas, copia de la lista y ejecución de la demostración.
