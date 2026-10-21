# La cocina de Juan · HTML y CSS

Base del sitio que después continúa con Bootstrap, DOM y Vue. Seis páginas principales, una ficha embebida y un formulario de práctica.

| TP  | Actividades                                                                                                        | Código                                            |
| --- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| 01  | Inicio, acerca de, contacto y receta; enlaces y encabezados                                                        | index, nosotros, registro y receta                |
| 02  | Tabla de ingredientes, listas e iconos                                                                             | receta.html y FontAwesome local                   |
| 03  | Iframe, enlaces con destino y formulario con distintos controles                                                   | sucursales.html, ubicaciones.html y registro.html |
| 04  | Hoja externa, selectores, fuentes, espaciado y estados                                                             | cocina.css                                        |
| 05  | Estilo del formulario y galería adaptable de clientes                                                              | clientes.html y registro.html                     |
| 06  | Cinco páginas o más, semántica, formulario, iframe, FontAwesome, fuente local, tres cortes, movimiento y Grid/Flex | Todo el bloque                                    |

## Decisiones de implementación

Los clientes y las sedes son ficticios. El iframe carga una ficha local y los enlaces cambian su destino sin necesitar mapas remotos. La galería usa ilustraciones propias. Lora y FontAwesome se incluyen con sus licencias.

El formulario retoma los controles de la práctica. El resumen usa nodos de texto, omite y limpia la clave, y no envía ni guarda información. Para probarlo, utilizar datos inventados.

Los puntos de corte son 1100, 760 y 420 px. La distribución pasa de tres columnas a dos y una; la galería se adapta y los campos se apilan. El movimiento respeta prefers-reduced-motion.

## Ejecutar

Desde la raíz: `python -m http.server 8000 --bind 127.0.0.1`.

Abrir `http://127.0.0.1:8000/Web/Trabajos-Practicos/Cocina/01-06-HTML-CSS/`.

Pruebas: `npm run test:web`.

Las consignas TP01–05 muestran un sitio de cocina. Este bloque desarrolla sus contenidos con una presentación propia; su autoría y fecha están en los créditos de la cursada. Órbita conserva su nombre histórico TP2, independiente de esta numeración.
