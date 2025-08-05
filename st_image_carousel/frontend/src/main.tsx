import React from 'react'
import ReactDOM from 'react-dom/client'
import CustomComponent from './CustomComponent'

// Pour un composant Streamlit, on n'a pas besoin de React.StrictMode
// et le composant doit être rendu directement
ReactDOM.createRoot(document.getElementById('root')!).render(
  <CustomComponent />
) 