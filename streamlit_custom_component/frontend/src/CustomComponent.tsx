import React, { useState, useEffect } from 'react'
import {
  withStreamlitConnection,
  ComponentProps,
  Streamlit,
} from 'streamlit-component-lib'

interface ImageItem {
  name: string
  url: string
}

function ImageSelector({ args }: ComponentProps) {
  const { 
    images, 
    selected_image, 
    max_visible = 5,
    background_color = '#1a1a2e',
    active_border_color = '#ffffff',
    active_glow_color = 'rgba(255, 255, 255, 0.5)',
    fallback_background = '#2a2a3e',
    fallback_gradient_end = 'rgb(0, 0, 0)',
    text_color = '#ffffff'
  } = args
  const [activeIndex, setActiveIndex] = useState(0)
  const [isHovering, setIsHovering] = useState(false)

  useEffect(() => {
    // Informer Streamlit que le composant est prêt
    Streamlit.setFrameHeight()
  }, [])

  useEffect(() => {
    // Mettre à jour la sélection si elle change depuis Python
    if (selected_image) {
      const index = images?.findIndex(img => img.name === selected_image) || 0
      setActiveIndex(index)
    }
  }, [selected_image, images])

  // Calculer les images visibles (dynamique selon max_visible)
  const getVisibleImages = () => {
    if (!images || images.length === 0) return []
    
    const length = images.length
    const centerIndex = Math.floor(max_visible / 2)
    const visibleImages = []
    
    for (let i = 0; i < max_visible; i++) {
      const offset = i - centerIndex
      const imageIndex = (activeIndex + offset + length) % length
      visibleImages.push(images[imageIndex])
    }
    
    return visibleImages
  }

  const visibleImages = getVisibleImages()

  // Sélectionner un joueur par position
  const selectPlayer = (position: number) => {
    const centerPosition = Math.floor(max_visible / 2) // Index du joueur central
    const diff = position - centerPosition
    const newIndex = (activeIndex + diff + images.length) % images.length
    setActiveIndex(newIndex)
    
    // Envoyer les données à Python
    const selectedImage = images[newIndex]
    Streamlit.setComponentValue({
      selected_image: selectedImage.name,
      selected_url: selectedImage.url,
      current_index: newIndex,
      timestamp: new Date().toISOString()
    })
  }

  // Navigation avec les flèches
  const scrollLeft = () => {
    const newIndex = (activeIndex - 1 + images.length) % images.length
    setActiveIndex(newIndex)
    
    const selectedImage = images[newIndex]
    Streamlit.setComponentValue({
      selected_image: selectedImage.name,
      selected_url: selectedImage.url,
      current_index: newIndex,
      timestamp: new Date().toISOString()
    })
  }

  const scrollRight = () => {
    const newIndex = (activeIndex + 1) % images.length
    setActiveIndex(newIndex)
    
    const selectedImage = images[newIndex]
    Streamlit.setComponentValue({
      selected_image: selectedImage.name,
      selected_url: selectedImage.url,
      current_index: newIndex,
      timestamp: new Date().toISOString()
    })
  }

  if (!images || images.length === 0) {
    return (
             <div style={{ 
         padding: '20px', 
         backgroundColor: background_color,
         borderRadius: '12px',
         textAlign: 'center',
         color: text_color
       }}>
         Aucune image disponible
       </div>
    )
  }

  return (
         <div style={{ 
       padding: '20px', 
       backgroundColor: background_color,
       borderRadius: '12px',
       textAlign: 'center',
       color: text_color,
       fontFamily: 'Urbanist, sans-serif'
     }}>
      {/* Nom du joueur actif */}
             <div style={{
         position: 'relative',
         textAlign: 'center',
         fontSize: '1.2rem',
         fontWeight: 'bold',
         marginBottom: '1rem',
         color: text_color,
         textTransform: 'uppercase',
         letterSpacing: '1px'
       }}>
        {images[activeIndex]?.name || 'Joueur inconnu'}
      </div>

      {/* Carrousel des joueurs */}
      <div style={{
        width: '100%',
        maxWidth: '500px',
        margin: '0 auto 2rem auto',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        gap: '15px'
      }}>
        {/* Bouton précédent */}
        <button
          onClick={scrollLeft}
          style={{
            background: 'none',
            border: 'none',
            width: '30px',
            height: '30px',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: 0,
            opacity: isHovering ? 1 : 0,
            transition: 'opacity 0.3s ease'
          }}
        >
          <div style={{
            width: '10px',
            height: '10px',
            borderLeft: '2px solid white',
            borderBottom: '2px solid white',
            transform: 'rotate(45deg)',
            marginLeft: '5px'
          }} />
        </button>

        {/* Conteneur des images */}
        <div 
          style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            position: 'relative',
            height: '120px',
            width: '500px'
          }}
          onMouseEnter={() => setIsHovering(true)}
          onMouseLeave={() => setIsHovering(false)}
        >
                     {visibleImages.map((image, index) => {
             const isSelected = index === Math.floor(max_visible / 2) // L'image centrale est sélectionnée
            
            return (
              <div
                key={index}
                onClick={() => selectPlayer(index)}
                style={{
                  width: isSelected ? '90px' : '70px',
                  height: isSelected ? '90px' : '70px',
                  borderRadius: '50%',
                  overflow: 'hidden',
                  position: 'absolute',
                  cursor: 'pointer',
                  transition: 'all 0.3s ease',
                                     border: isSelected ? `2px solid ${active_border_color}` : '2px solid transparent',
                   backgroundColor: '#000000',
                   opacity: 1,
                   visibility: 'visible',
                   zIndex: isSelected ? 5 : 5 - Math.abs(index - Math.floor(max_visible / 2)),
                   boxShadow: isSelected ? 
                     `0 0 10px ${active_glow_color}, 0 0 20px ${active_glow_color.replace('0.5', '0.3')}, 0 0 30px ${active_glow_color.replace('0.5', '0.1')}` : 
                     'none',
                                     // Positionnement dynamique des images selon max_visible
                   left: `${(index / (max_visible - 1)) * 100}%`,
                   transform: `translateX(-${(index / (max_visible - 1)) * 100}%)`
                }}
              >
                {image.url ? (
                  <img
                    src={image.url}
                    alt={image.name}
                    style={{
                      width: '100%',
                      height: '100%',
                      objectFit: 'cover',
                      objectPosition: 'center 20%'
                    }}
                    onError={(e) => {
                      // En cas d'erreur de chargement, remplacer l'image par le fallback
                      const target = e.target as HTMLImageElement;
                      target.style.display = 'none';
                      const parent = target.parentElement;
                      if (parent) {
                        const fallback = parent.querySelector('.image-fallback') as HTMLElement;
                        if (fallback) {
                          fallback.style.display = 'flex';
                        }
                      }
                    }}
                  />
                ) : null}
                                 {/* Fallback en cas d'absence d'URL ou d'erreur de chargement */}
                 <div 
                   className="image-fallback"
                   style={{
                     width: '100%',
                     height: '100%',
                     display: image.url ? 'none' : 'flex',
                     flexDirection: 'column',
                     alignItems: 'center',
                     justifyContent: 'center',
                     backgroundColor: fallback_background,
                     color: text_color,
                     fontSize: isSelected ? '12px' : '10px',
                     textAlign: 'center',
                     lineHeight: '1.1',
                     fontWeight: '600',
                     textTransform: 'uppercase',
                     letterSpacing: '0.3px',
                     borderRadius: '50%',
                     boxShadow: 'inset 0 0 10px rgba(0, 0, 0, 0.3)',
                     background: `linear-gradient(135deg, ${fallback_background} 0%, ${fallback_gradient_end} 100%)`,
                     position: 'absolute',
                     top: 0,
                     left: 0,
                     wordBreak: 'break-word',
                     overflow: 'hidden'
                   }}
                 >
                   {image.name}
                 </div>
              </div>
            )
          })}
        </div>

        {/* Bouton suivant */}
        <button
          onClick={scrollRight}
          style={{
            background: 'none',
            border: 'none',
            width: '30px',
            height: '30px',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: 0,
            opacity: isHovering ? 1 : 0,
            transition: 'opacity 0.3s ease'
          }}
        >
          <div style={{
            width: '10px',
            height: '10px',
            borderLeft: '2px solid white',
            borderBottom: '2px solid white',
            transform: 'rotate(-135deg)',
            marginRight: '5px'
          }} />
        </button>
      </div>

      
    </div>
  )
}

export default withStreamlitConnection(ImageSelector)