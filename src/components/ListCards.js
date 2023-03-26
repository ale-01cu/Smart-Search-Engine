import {useEffect, useState} from 'react'
import { Link } from 'wouter';

const URL_DETALLE = '/detalle/'

export const ListCards = ({url}) => {
  const [cards, setCards] = useState([]);

  useEffect(() => {
    fetch(url)
    .then(res => res.json())
    .then(data => {
      console.log(data);
      setCards(data)
    })
  }, [url]);

  return (
    <>
      {
        typeof(cards[cards.length - 1]) === 'number' && <h4 className='tiempo'>Se encontraron {cards.length - 1} resultados en {cards.pop()} segundos.</h4>
      }

      <div className="grilla">
        {
          cards.map(e => {
            if (!e.titulo) return null 

            return <Link to={URL_DETALLE + e.id} key={e.id} className="card">
              <h2>{e.titulo}</h2>
              {e.categoria}<br/>
              {e.generos}
            </Link>
          })
        }
      </div>
    </>
  )
}
