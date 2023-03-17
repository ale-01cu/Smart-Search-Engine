import { Route, Switch } from 'wouter'
import { ListCards } from './ListCards'
import { DetailCard } from './DetailCard'
import { NotFound } from '../pages/notFounds'

export const Main = ({setBuscador, URL_BUSQUEDA, URL_CONTENIDO}) => {

  return (
    <main>
        <Switch>
          <Route path='/'>
            {params => <ListCards url={URL_CONTENIDO}/>}
          </Route>

          <Route path='/detalle/:id'>
            {params => <DetailCard id={params.id}/>}
          </Route>
          
          <Route path='/result/:busqueda'>
            {params => {
              setBuscador(params.busqueda)
              return <ListCards url={URL_BUSQUEDA + params.busqueda}/>
            }}
          </Route>
          <Route path='' component={NotFound}/>
        </Switch>
    </main>
  )
}