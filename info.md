# Whole Foods Shopping List

This is a custom integration for Home Assistant that allows you to manage a shopping list specifically for Whole Foods. You can add items with product names, product numbers, and images, and filter them by labels.

## Installation

1. Add the repository to HACS.
2. Install the integration via HACS.
3. Configure the integration in Home Assistant.

## Usage

- Add items to your catalog using the provided services.
- Display the catalog in Lovelace using the custom card.
- Filter items by labels and add them to your Whole Foods cart.

Lovelace Integration:
```
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