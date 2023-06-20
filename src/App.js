import './styles/index.css'
import {Header} from './components/header'
import {Main} from './components/main'
import Footer from './components/footer'
import { useState, useEffect } from 'react';
import {fetching} from './services/Fetching'

const URL_CONTENIDO = 'http://localhost:8000/api/contenido/?p=1'
const URL_BUSQUEDA = `http://localhost:8000/api/search/?busqueda=`


function App() {
  const [buscador, setBuscador] = useState("")
  const [pagination, setPagination] = useState({})
  const [urlContenido, setUrlContenido] = useState(URL_CONTENIDO)
  

  return (
    <div>
      <Header buscador={buscador}/>
      <Main setBuscador={setBuscador} URL_BUSQUEDA={URL_BUSQUEDA} URL_CONTENIDO={urlContenido} setPagination={setPagination}/>
      <Footer next={pagination.next || ""} previous={pagination.previous || ""} setUrlContenido={setUrlContenido}/>
    </div>
    );
}

export default App;
