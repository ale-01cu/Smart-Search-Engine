import { useEffect, useState } from 'react'
import { fetching } from '../services/Fetching'

export const DetailCard = ({params}) => {
  const URL_DETAIL = 'http://localhost:8000/api/contenido/' + params.id + "/" 
  const [detail, setDetail] = useState({})

  useEffect(() => {
    fetching(URL_DETAIL).then(res => setDetail(res))
    
  }, [URL_DETAIL])

  console.log(URL_DETAIL);
  console.log(detail);
  
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