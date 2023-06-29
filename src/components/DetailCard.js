import { useEffect, useState } from 'react'
import { fetching } from '../services/Fetching'

export const DetailCard = ({id, query}) => {
  const URL_DETAIL = 'http://localhost:8000/api/contenido/' + id + "/"
  const [detail, setDetail] = useState({})
  console.log(query);

  useEffect(() => {
    fetch(URL_DETAIL)
      .then(res => res.json())
      .then(data => {
        console.log(data);
        setDetail(data)
      })
    
  }, [URL_DETAIL])

  return (
    <div className='detalle'>
      <h1>{detail.titulo}</h1>
      <h4>{detail.fecha_de_estreno}</h4>
      <h4>{detail.categoria}</h4>
      <h4>{detail.fecha_de_estreno}</h4>
      <p>{detail.descripcion}
      </p>
      <h4>{detail.generos}</h4>
    </div>
  )
}