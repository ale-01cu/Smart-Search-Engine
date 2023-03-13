import './styles/App.css';
import { Route, Switch } from 'wouter'
import { ListCards } from './components/ListCards'
import { DetailCard } from './components/DetailCard'
import {Buscador} from './components/Buscador'
import { useState } from 'react';

const URL_CONTENIDO = 'http://localhost:8000/api/contenido'
const URL_BUSQUEDA = `http://localhost:8000/api/contenido/resultadoBusqueda/?busqueda=`


function App() {
  const [buscador, setBuscador] = useState("")

  return (
    <div className="App">
      <header className="App-header">
        <Buscador actualizarUrl valueInput={buscador}/>
      </header>

      <main>
        <Switch>
          <Route path='/'><ListCards url={URL_CONTENIDO}/></Route>
          <Route path='/detalle/:id'>
            {params => <DetailCard id={params.id}/>}
          </Route>
          <Route path='/result/:busqueda'>
            {params => {
              setBuscador(params.busqueda)
              return <ListCards url={URL_BUSQUEDA + params.busqueda}/>
            }}
          </Route>
        </Switch>
      </main>


    </div>
  );
}

export default App;
