
export const fetching = props => {

return fetch(props)
  .then(res => res.json())
  .then(data => data)
  .catch(err => {
    console.log(err);
  })

}