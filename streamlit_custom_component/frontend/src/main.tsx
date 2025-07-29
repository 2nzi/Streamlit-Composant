import React from 'react'
import ReactDOM from 'react-dom/client'
import ImageSelector from './CustomComponent.tsx'

// Exemple d'images pour le développement
const sampleImages = [
  {
    name: "Lionel Messi",
    url: "https://upload.wikimedia.org/wikipedia/commons/b/b4/Lionel-Messi-Argentina-2022-FIFA-World-Cup_%28cropped%29.jpg"
  },
  {
    name: "Cristiano Ronaldo",
    url: "https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg"
  },
  {
    name: "Kylian Mbappé",
    url: "https://upload.wikimedia.org/wikipedia/commons/5/57/Kylian_Mbapp%C3%A9_2019.jpg"
  }
]

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <ImageSelector 
      args={{
        images: sampleImages,
        selected_image: null
      }}
    />
  </React.StrictMode>,
) 