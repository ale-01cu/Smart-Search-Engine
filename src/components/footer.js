import {Link} from 'wouter'


const Footer = ({next = '', previous = '', setUrlContenido}) => {

  const handleClickAnterior = e => {
    setUrlContenido(previous)
  }

  const handleClickSiguiente = e => {
    setUrlContenido(next)
  }


  return <footer>

    <button onClick={handleClickAnterior} disabled={previous === ''} className='btn-previous'>Anterior</button>
    <button onClick={handleClickSiguiente} disabled={next === ''} className='btn-next'>Siguiente</button>
  
  </footer>
  

  
}

export default Footer