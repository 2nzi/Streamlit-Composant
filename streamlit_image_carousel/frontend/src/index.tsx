import React from 'react'
import ReactDOM from 'react-dom/client'
import ImageSelector from './CustomComponent'

// Fonction pour rendre le composant dans le DOM
function renderComponent() {
  const root = document.getElementById('root')
  if (root) {
    ReactDOM.createRoot(root).render(<ImageSelector />)
  }
}

// Rendre le composant quand le DOM est prêt
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', renderComponent)
} else {
  renderComponent()
}

export default ImageSelector 