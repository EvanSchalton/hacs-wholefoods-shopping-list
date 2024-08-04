from homeassistant.helpers.entity import Entity

DOMAIN = "wholefoods_shopping_list"

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([WholeFoodsCatalogSensor(hass.data[DOMAIN])])

class WholeFoodsCatalogSensor(Entity):
    def __init__(self, catalog):
        self._catalog = catalog

    @property
    def name(self):
        return "Whole Foods Catalog"

    @property
    def state(self):
        return len(self._catalog.catalog)

    @property
    def extra_state_attributes(self):
        return {"catalog": self._catalog.catalog}
