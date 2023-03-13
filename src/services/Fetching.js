
export const fetching = props => {

return fetch(props)
  .then(res => res.json())
  .then(data => {
    console.log(data);
    return data
  })
  .catch(err => {
    console.log(err);
  })

}