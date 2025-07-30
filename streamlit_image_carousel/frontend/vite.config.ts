import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'build',
    rollupOptions: {
      input: 'index.html',
      output: {
        entryFileNames: 'index.mjs',
        chunkFileNames: '[name].mjs',
        assetFileNames: '[name].[ext]'
      }
    }
  },
  server: {
    port: 3001
  }
}) 