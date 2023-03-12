import {useEffect, useState} from 'react'
import { Link } from 'wouter';
import { fetching } from '../services/Fetching'
const URL_DETALLE = 'detalle/'

export const ListCards = ({url}) => {
  const [cards, setCards] = useState([]);

  useEffect(() => {
    fetching(url).then(res => {
      setCards(res)
    })
    

  }, [url]);

  return (
    <div className="grilla">
      {
        cards.map(e => 
        (
          <Link to={URL_DETALLE + e.id} key={e.id} className="card">
            <h2>{e.titulo}</h2>
            {e.categoria}<br/>
            {e.generos}
          </Link>
        ))
      }
    </div>
  )
}
