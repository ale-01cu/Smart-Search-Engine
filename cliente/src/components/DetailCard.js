import { fetching } from '../services/Fetching'

export const DetailCard = ({params}) => {
  const URL_DETAIL = 'http://localhost:8000/api/contenido/' + params.id

  fetching(URL_DETAIL).then(res => {console.log(res)})

  return (
    <div className='detalle'>
      estamos en detalleasdasdasdasd
      dasdasdasdasdasdasdasd
      asdasdasdasdsa
    </div>
  )
}