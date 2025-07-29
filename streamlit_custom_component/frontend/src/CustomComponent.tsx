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
  const { images, selected_image, max_visible = 5 } = args
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

  // Calculer les 5 images visibles (2 avant, 1 central, 2 après)
  const getVisibleImages = () => {
    if (!images || images.length === 0) return []
    
    const length = images.length
    const prev2 = (activeIndex - 2 + length) % length
    const prev1 = (activeIndex - 1 + length) % length
    const next1 = (activeIndex + 1) % length
    const next2 = (activeIndex + 2) % length
    
    return [
      images[prev2],
      images[prev1],
      images[activeIndex],
      images[next1],
      images[next2]
    ]
  }

  const visibleImages = getVisibleImages()

  // Sélectionner un joueur par position (0-4)
  const selectPlayer = (position: number) => {
    const centerPosition = 2 // Index du joueur central
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
        backgroundColor: '#1a1a2e',
        borderRadius: '12px',
        textAlign: 'center',
        color: '#ffffff'
      }}>
        Aucune image disponible
      </div>
    )
  }

  return (
    <div style={{ 
      padding: '20px', 
      backgroundColor: '#1a1a2e',
      borderRadius: '12px',
      textAlign: 'center',
      color: '#ffffff',
      fontFamily: 'Urbanist, sans-serif'
    }}>
      {/* Nom du joueur actif */}
      <div style={{
        position: 'relative',
        textAlign: 'center',
        fontSize: '1.2rem',
        fontWeight: 'bold',
        marginBottom: '2rem',
        color: '#ffffff',
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
            const isSelected = index === 2 // L'image centrale est sélectionnée
            const isHidden = !isHovering && !isSelected
            
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
                  border: isSelected ? '2px solid #ffffff' : '2px solid transparent',
                  backgroundColor: '#000000',
                  opacity: isHidden ? 0 : 1,
                  visibility: isHidden ? 'hidden' : 'visible',
                  zIndex: isSelected ? 5 : 5 - Math.abs(index - 2),
                  boxShadow: isSelected ? 
                    '0 0 10px rgba(255, 255, 255, 0.5), 0 0 20px rgba(255, 255, 255, 0.3), 0 0 30px rgba(255, 255, 255, 0.1)' : 
                    'none',
                  // Positionnement des images
                  left: index === 0 ? '0' : 
                        index === 1 ? '22%' : 
                        index === 2 ? '50%' : 
                        index === 3 ? '78%' : '100%',
                  transform: index === 0 ? 'none' : 
                            index === 1 ? 'translateX(-22%)' : 
                            index === 2 ? 'translateX(-50%)' : 
                            index === 3 ? 'translateX(-78%)' : 'translateX(-100%)'
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
                  />
                ) : (
                  <div style={{
                    width: '100%',
                    height: '100%',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    backgroundColor: '#2a2a3e',
                    color: '#ffffff',
                    fontSize: '10px',
                    textAlign: 'center',
                    padding: '5px',
                    lineHeight: '1.2'
                  }}>
                    {image.name}
                  </div>
                )}
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

      {/* Détails du joueur */}
      {images[activeIndex] && (
        <div style={{
          padding: '0 3rem',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          textAlign: 'center'
        }}>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(2, 1fr)',
            gap: '1rem 5rem',
            marginTop: '0.5rem',
            width: '100%',
            maxWidth: '350px',
            marginLeft: 'auto',
            marginRight: 'auto'
          }}>
            <div style={{
              display: 'flex',
              flexDirection: 'column',
              gap: '0.25rem',
              alignItems: 'flex-start'
            }}>
              <span style={{
                fontSize: '0.8rem',
                color: '#8a8a8a',
                textTransform: 'uppercase',
                letterSpacing: '0.5px',
                textAlign: 'left'
              }}>
                Position
              </span>
              <span style={{
                fontSize: '1rem',
                fontWeight: '600',
                color: 'white',
                textAlign: 'left'
              }}>
                {activeIndex + 1} / {images.length}
              </span>
            </div>
            
            <div style={{
              display: 'flex',
              flexDirection: 'column',
              gap: '0.25rem',
              alignItems: 'flex-start'
            }}>
              <span style={{
                fontSize: '0.8rem',
                color: '#8a8a8a',
                textTransform: 'uppercase',
                letterSpacing: '0.5px',
                textAlign: 'left'
              }}>
                Nom
              </span>
              <span style={{
                fontSize: '1rem',
                fontWeight: '600',
                color: 'white',
                textAlign: 'left'
              }}>
                {images[activeIndex].name}
              </span>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default withStreamlitConnection(ImageSelector)