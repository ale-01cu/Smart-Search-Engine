import {useEffect, useState} from 'react'
import { Link } from 'wouter';
import {fetching} from '../services/Fetching'

const URL_DETALLE = '/detalle/'

export const ListCards = ({url, setPagination}) => {
  const [cards, setCards] = useState([]);

  useEffect(() => {
    fetching(url).then(data => {
      console.log(data)

      if (data.results) {
        setPagination({'next': data.next, 'previous': data.previous})
        setCards(data.results)
      }
      else {
        setPagination({'next': "", 'previous': ""})
        setCards(data)
      }

    })
  }, [url, setPagination]);

  return (
    <>
      {/* {
        typeof(cards[cards.length - 1]) === 'number' && <h4 className='tiempo'>Se encontraron {cards.length - 1} resultados en {cards.pop()} segundos.</h4>
      } */}

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
