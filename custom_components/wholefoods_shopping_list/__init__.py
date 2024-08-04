from homeassistant.core import HomeAssistant

DOMAIN = "wholefoods_shopping_list"

async def async_setup(hass: HomeAssistant, config: dict):
    hass.data[DOMAIN] = WholeFoodsCatalog()

    async def handle_add_item(call):
        name = call.data["name"]
        product_number = call.data["product_number"]
        image_url = call.data.get("image_url")
        labels = call.data.get("labels", [])
        item = {
            "name": name,
            "product_number": product_number,
            "image_url": image_url,
            "labels": labels
        }
        hass.data[DOMAIN].add_item(item)

    async def handle_remove_item(call):
        product_number = call.data["product_number"]
        hass.data[DOMAIN].remove_item(product_number)

    hass.services.async_register(DOMAIN, "add_item_to_catalog", handle_add_item)
    hass.services.async_register(DOMAIN, "remove_item_from_catalog", handle_remove_item)

    return True

class WholeFoodsCatalog:
    def __init__(self):
        self._catalog = []

    def add_item(self, item):
        existing_item = next((i for i in self._catalog if i["product_number"] == item["product_number"]), None)
        if existing_item:
            self._catalog.remove(existing_item)
        self._catalog.append(item)

    def remove_item(self, product_number):
        self._catalog = [item for item in self._catalog if item["product_number"] != product_number]

    @property
    def catalog(self):
        return self._catalog
