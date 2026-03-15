# website_sale_marketplace_journal

Modulo para Odoo 17 que permite configurar el diario de ventas por defecto para facturas generadas desde pedidos de e-commerce (`website_sale`).

## Objetivo

Evitar que Odoo use automaticamente un diario de ventas no deseado al facturar pedidos web.

Con este modulo se puede definir por compania un diario especifico para marketplace/e-commerce desde Configuracion.

## Funcionalidades

- Agrega el campo `marketplace_sale_journal_id` en `res.company`.
- Expone el campo en `res.config.settings` como ajuste por compania.
- Valida que el diario:
  - pertenezca a la compania activa;
  - sea de tipo ventas (`sale`).
- Al crear factura desde `sale.order`, si el pedido viene de website (`website_id`), fuerza ese `journal_id`.

## Dependencias

- `account`
- `sale_management`
- `website_sale`

## Configuracion

1. Ir a `Ajustes > Contabilidad`.
2. Seleccionar la compania correcta.
3. En `Invoicing Settings`, definir `Marketplace Sale Journal`.

## Comportamiento

- Pedido e-commerce (`website_id`): usa `Marketplace Sale Journal` si esta configurado.
- Pedido no e-commerce: mantiene el comportamiento estandar de Odoo.
- Si no hay diario configurado: mantiene el comportamiento estandar de Odoo.

## Instalacion / actualizacion

```bash
docker-compose run --rm web-dev odoo -d openlab-dev -u website_sale_marketplace_journal --stop-after-init
docker-compose restart web-dev
```

## Licencia

LGPL-3. Ver archivo `LICENSE`.
