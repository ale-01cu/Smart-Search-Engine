import './styles/App.css';
import { Route, Switch } from 'wouter'
import { ListCards } from './components/ListCards'
import { DetailCard } from './components/DetailCard'
import {Buscador} from './components/Buscador'
import { useState } from 'react';

const URL_CONTENIDO = 'http://localhost:8000/api/contenido'

function App() {
  const [listCards, setListCards] = useState([])
  const [url, setUrl] = useState([])

  const actualizarUrl = (nuevaUrl) => {
    setUrl(nuevaUrl)
  }


  return (
    <div className="App">
      <header className="App-header">
        <Buscador actualizarUrl={actualizarUrl}/>
      </header>

      <main>
        <Route path='/'><ListCards url={URL_CONTENIDO}/></Route>
        <Route path='/detalle/:id' component={DetailCard}/>
        <Route path='/result'><ListCards url={url}/></Route>
      </main>


    </div>
  );
}

export default App;
