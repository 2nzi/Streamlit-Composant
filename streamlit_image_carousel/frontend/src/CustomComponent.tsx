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
    background_color = '#ffffff',
    active_border_color = '#ffffff',
    active_glow_color = 'rgba(255, 255, 255, 0.5)',
    fallback_background = '#000000',
    fallback_gradient_end = '#000000',
    text_color = '#000000',
    arrow_color = '#31333f'
  } = args
  
  const [activeIndex, setActiveIndex] = useState(0)
  const [isHovering, setIsHovering] = useState(false)
  const [searchTerm, setSearchTerm] = useState('')
  const [showSuggestions, setShowSuggestions] = useState(false)
  const [filteredPlayers, setFilteredPlayers] = useState<ImageItem[]>([])

  useEffect(() => {
    // Informer Streamlit que le composant est prêt
    Streamlit.setFrameHeight()
  }, [])

  useEffect(() => {
    // Mettre à jour la sélection si elle change depuis Python
    if (selected_image) {
      const index = images?.findIndex((img: ImageItem) => img.name === selected_image) || 0
      setActiveIndex(index)
    }
  }, [selected_image, images])

  // Fonction de recherche avec suggestions
  useEffect(() => {
    if (!images) return

    if (searchTerm.trim() === '') {
      setFilteredPlayers([])
      setShowSuggestions(false)
      return
    }

    const searchLower = searchTerm.toLowerCase()
    const filtered = images.filter((player: ImageItem) => 
      player.name.toLowerCase().includes(searchLower)
    )

    setFilteredPlayers(filtered)
    setShowSuggestions(filtered.length > 0)
  }, [searchTerm, images])

  // Sélectionner un joueur depuis la recherche
  const selectPlayerFromSearch = (player: ImageItem) => {
    const index = images.findIndex((img: ImageItem) => img.name === player.name)
    if (index !== -1) {
      setActiveIndex(index)
      setSearchTerm('')
      setShowSuggestions(false)
      
      // Envoyer les données à Python
      Streamlit.setComponentValue({
        selected_image: player.name,
        selected_url: player.url,
        current_index: index,
        timestamp: new Date().toISOString()
      })
    }
  }

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
    const centerPosition = Math.floor(max_visible / 2)
    const diff = position - centerPosition
    const newIndex = (activeIndex + diff + images.length) % images.length
    setActiveIndex(newIndex)
    
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
      fontFamily: 'Urbanist, sans-serif',
      // minHeight: '100px'  // Augmentation de la hauteur minimale
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
            opacity: 1,
            transition: 'opacity 0.3s ease'
          }}
        >
          <div style={{
            width: '10px',
            height: '10px',
            borderLeft: `2px solid ${arrow_color}`,
            borderBottom: `2px solid ${arrow_color}`,
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
            const isSelected = index === Math.floor(max_visible / 2)
            
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
                  backgroundColor: 'rgba(50, 50, 50, 0.46)',
                  opacity: 1,
                  visibility: 'visible',
                  zIndex: isSelected ? 5 : 5 - Math.abs(index - Math.floor(max_visible / 2)),
                  boxShadow: isSelected ? 
                    `0 0 10px ${active_glow_color}, 0 0 20px ${active_glow_color.replace('0.5', '0.3')}, 0 0 30px ${active_glow_color.replace('0.5', '0.1')}` : 
                    'none',
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
            opacity: 1,
            transition: 'opacity 0.3s ease'
          }}
        >
          <div style={{
            width: '10px',
            height: '10px',
            borderLeft: `2px solid ${arrow_color}`,
            borderBottom: `2px solid ${arrow_color}`,
            transform: 'rotate(-135deg)',
            marginRight: '5px'
          }} />
        </button>
      </div>

      {/* Barre de recherche avec suggestions */}
      <div style={{
        marginTop: '2rem',
        position: 'relative',
        width: '300px',
        margin: '2rem auto 0 auto',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        minHeight: '200px'
      }}>
        {/* Barre de recherche */}
        <div style={{
          position: 'relative',
          marginBottom: '1rem',
          width: '100%',
          display: 'flex',
          justifyContent: 'center'
        }}>
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Rechercher un joueur..."
            style={{
              width: '100%',
              maxWidth: '280px',
              padding: '10px 14px',
              paddingLeft: '35px',
              border: '2px solid rgba(50, 50, 50, 0.2)',
              borderRadius: '20px',
              backgroundColor: 'rgba(184, 184, 184, 0.46)',
              color: text_color,
              fontSize: '14px',
              outline: 'none',
              transition: 'all 0.3s ease',
              fontFamily: 'Urbanist, sans-serif',
              textAlign: 'left'
            }}
            onFocus={() => setShowSuggestions(true)}
            onBlur={() => {
              setTimeout(() => setShowSuggestions(false), 200)
            }}
          />
        </div>

        {/* Suggestions - Simplifiées */}
        {showSuggestions && filteredPlayers.length > 0 && (
          <div style={{
            width: '280px',
            backgroundColor: 'rgba(50, 50, 50, 0.2)',
            borderRadius: '12px',
            border: '1px solid rgba(255, 255, 255, 0.2)',
            maxHeight: '120px',
            overflowY: 'auto',
            zIndex: 1000,
            backdropFilter: 'blur(10px)',
            marginTop: '0'
          }}>
            {filteredPlayers.slice(0, 5).map((player, index) => (
              <div
                key={index}
                onClick={() => selectPlayerFromSearch(player)}
                style={{
                  padding: '12px 16px',
                  cursor: 'pointer',
                  borderBottom: index < filteredPlayers.length - 1 ? '1px solid rgba(255, 255, 255, 0.1)' : 'none',
                  transition: 'background-color 0.2s ease',
                  textAlign: 'left'
                }}
                onMouseEnter={(e) => {
                  e.currentTarget.style.backgroundColor = 'rgba(255, 255, 255, 0.1)'
                }}
                onMouseLeave={(e) => {
                  e.currentTarget.style.backgroundColor = 'transparent'
                }}
              >
                <div style={{
                  fontSize: '14px',
                  color: text_color
                }}>
                  {player.name}
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Message si aucun résultat */}
        {searchTerm && filteredPlayers.length === 0 && (
          <div style={{
            textAlign: 'center',
            padding: '10px',
            color: text_color,
            opacity: 0.7,
            fontSize: '13px',
            width: '280px',
            marginTop: '0'
          }}>
            Aucun joueur trouvé pour "{searchTerm}"
          </div>
        )}
      </div>
    </div>
  )
}

export default withStreamlitConnection(ImageSelector) 