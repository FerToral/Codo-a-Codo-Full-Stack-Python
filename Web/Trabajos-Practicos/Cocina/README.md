# La cocina de Juan

Una misma temática recorre las prácticas de Bootstrap, JavaScript y Vue. Cada etapa se puede ejecutar por separado y conserva los conceptos de su trabajo práctico.

| Trabajo | Carpeta                                 | Contenido                                                                 |
| ------- | --------------------------------------- | ------------------------------------------------------------------------- |
| TP07    | [07-Bootstrap](07-Bootstrap/index.html) | Navegación colapsable, carrusel y tres columnas adaptables                |
| TP08–09 | [08-09-DOM](08-09-DOM/index.html)       | Cabecera y pie compartidos; productos desde un array de objetos           |
| TP10    | [10-Vue](10-Vue/index.html)             | Datos reactivos, tarjetas Bootstrap y filtros                             |
| TP11    | [11-SPA](11-SPA/index.html)             | Secciones en una sola página, navegación por hash y estado de la interfaz |

## Ejecutar

Desde la raíz del repositorio:

```console
python -m http.server 8000 --bind 127.0.0.1
```

Abrir `http://127.0.0.1:8000/Web/Trabajos-Practicos/Cocina/07-Bootstrap/` y continuar por las etapas. Hace falta servir los archivos por HTTP porque las prácticas usan módulos de JavaScript. Las bibliotecas, los datos y la ilustración están incluidos: no se necesita conexión a Drive ni a un CDN.

Los formularios sólo validan datos en el navegador; no simulan un envío a un servidor inexistente. Los productos son ejemplos didácticos, no una tienda en producción.

Las [consignas](CONSIGNAS.md) describen lo que se trabaja en cada etapa. Las versiones y licencias de las bibliotecas están en [créditos](../../../CREDITOS.md).
