import {Buscador} from './Buscador'
import { Link } from 'wouter'

export const Header = ({buscador}) => {

  return (
    <header className="App-header">
      <Link to='http://localhost:8000' className='btn-inicio'>Inicio</Link>
      <Buscador valueInput={buscador}/>
    </header>
  )
}