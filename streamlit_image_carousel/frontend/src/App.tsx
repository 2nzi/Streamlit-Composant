import React from 'react'
import CustomComponent from './CustomComponent'

function App() {
  return (
    <div className="App">
      <CustomComponent 
        args={{
          images: [
            { name: "Test 1", url: "https://via.placeholder.com/150" },
            { name: "Test 2", url: "https://via.placeholder.com/150" },
            { name: "Test 3", url: "https://via.placeholder.com/150" },
          ],
          selected_image: null,
          max_visible: 5,
          background_color: '#1a1a2e',
          active_border_color: '#ffffff',
          active_glow_color: 'rgba(255, 255, 255, 0.5)',
          fallback_background: '#2a2a3e',
          fallback_gradient_end: 'rgb(0, 0, 0)',
          text_color: '#ffffff',
          arrow_color: '#ffffff'
        }}
      />
    </div>
  )
}

export default App 