
export const fetching = props => {

return fetch(props)
  .then(res => res.json())
  .then(data => {
    console.log(data);
  })
  .catch(err => {
    console.log(err);
  })

}