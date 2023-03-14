
export const fetching = async (props) => {
  try {
    const res = await fetch(props)
    const data = await res.json()
    console.log(data);
    return data
    
  } catch (error) {
    
    console.log(error);
  }

}