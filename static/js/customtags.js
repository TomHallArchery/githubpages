class MyCustomTag extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `<h1>Hello, World!</h1>`;
  }
}

customElements.define('my-custom-tag', MyCustomTag);
