import {useEffect, useState} from 'react'
import { Link } from 'wouter';
import { fetching } from '../services/Fetching'
const URL_DETALLE = 'api/contenido/'

export const ListCards = ({url}) => {
  const [cards, setCards] = useState([]);

  useEffect(() => {
    // setCards([
    //   {
    //     'id': 1,
    //     'titulo': 'avengers'
    //   },
    //   {
    //     'id': 2,
    //     'titulo': 'arrastrados'
    //   },
    //   {
    //     'id': 3,
    //     'titulo': 'la bestia'
    //   },
    //   {
    //     'id': 4,
    //     'titulo': 'amarrados'
    //   },
    //   {
    //     'id': 5,
    //     'titulo': 'apocalipsis'
    //   }
    // ])
    console.log(url);
    fetching(url).then(res => {console.log(res);})
    

  }, [url]);

  return (
    <div className="grilla">
      {
        cards.map(e => 
        (
          <Link to={URL_DETALLE + e.id} key={e.id} className="card">
            {e.titulo}
          </Link>
        ))
      }
    </div>
  )
}
