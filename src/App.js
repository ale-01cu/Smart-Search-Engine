import './styles/index.css'
import {Header} from './components/header'
import {Main} from './components/main'
import { useState } from 'react';

const URL_CONTENIDO = 'http://localhost:8000/api/contenido/'
const URL_BUSQUEDA = `http://localhost:8000/api/search/?busqueda=`


function App() {
  const [buscador, setBuscador] = useState("")

  return (
    <div>
      <Header buscador={buscador}/>
      <Main setBuscador={setBuscador} URL_BUSQUEDA={URL_BUSQUEDA} URL_CONTENIDO={URL_CONTENIDO}/>
    </div>
    );
}

export default App;
