# Whole Foods Shopping List

This integration allows you to manage a shopping list specifically for Whole Foods.

## Features

- Add items with product names, product numbers, images, and labels.
- Remove items from the catalog.
- Display catalog items in a Lovelace card.
- Filter items by labels.

## Installation

1. Add this repository to HACS as a custom repository.
2. Install the integration via HACS.
3. Add the custom card to Lovelace.

## Configuration

- **Services**: Use the provided services to add or remove items from the catalog.
- **Lovelace**: Use the custom Lovelace card to display the catalog and interact with items.

## Example Lovelace Configuration

```yaml
resources:
  - url: /hacsfiles/wholefoods_shopping_list/wholefoods-catalog-card.js
    type: module

views:
  - title: Whole Foods Catalog
    cards:
      - type: custom:wholefoods-catalog-card
        entity: sensor.whole_foods_catalog
        label_filter: ["organic"]
```