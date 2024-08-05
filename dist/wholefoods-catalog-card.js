class WholeFoodsCatalogCard extends HTMLElement {
  set hass(hass) {
    const entityId = this.config.entity;
    const state = hass.states[entityId];

    if (!this.content) {
      this.innerHTML = `
        <style>
          .catalog-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 10px;
          }
          .catalog-item img {
            max-width: 100px;
            max-height: 100px;
          }
        </style>
        <div id="catalog"></div>
      `;
      this.content = this.querySelector('#catalog');
    }

    const catalog = state.attributes.catalog;
    const labelFilter = this.config.label_filter;

    const filteredCatalog = catalog.filter(item => 
      !labelFilter || item.labels.some(label => labelFilter.includes(label))
    );

    this.content.innerHTML = filteredCatalog.map(item => `
      <div class="catalog-item">
        <img src="${item.image_url}" alt="${item.name}">
        <div>${item.name}</div>
        <button onclick="handleAddToCart('${item.product_number}')">Add to cart</button>
      </div>
    `).join('');

    window.handleAddToCart = function(productNumber) {
      hass.callService('wholefoods_shopping_list', 'add_to_cart', { product_number: productNumber });
    };
  }

  setConfig(config) {
    if (!config.entity) {
      throw new Error('You need to define an entity');
    }
    this.config = config;
  }

  getCardSize() {
    return 3;
  }
}

customElements.define('wholefoods-catalog-card', WholeFoodsCatalogCard);
