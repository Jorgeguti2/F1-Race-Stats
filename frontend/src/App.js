import React, { useState, useEffect } from 'react'

function App() {

  // Used to set the data we retrie
  const [data, setData] = useState([{}])

  // useEffect to fetch the /members route in the backend.
  // Whatever response that the /members route gives us, in this case
  //    the json array, we put that into res.json and then set that data into the data variable
  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  // Passed in this empty array to make sure the useEffect only runs once
  }, [])

  return (
    <div>

    {(typeof data.members === 'undefined') ? (
      <p>Loading...</p>
    ) : (
      data.members.map((member, i) => (
        <p key={i}>{member}</p>
      ))
    )}

    </div>
  )
}

export default App
