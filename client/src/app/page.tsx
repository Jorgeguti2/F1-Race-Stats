'use client'
import React from 'react'
import {useState, useEffect} from 'react'

export default function Home() {
  const [message, setMessage] = useState('Test')

  function getDrivers(){
    fetch('http://127.0.0.1:5000/driver/drivers')
      .then(response=>response.json())
      .then(data=>console.log(data))
      .catch(err=>console.log(err))
  }
  const postDriver = async () => {
    const res = await fetch('http://127.0.0.1:5000/driver/drivers', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ 
        name: "Test Racer 1",
        abbreviation: "TR1" 
      }),
    })
  }

  return (
    <div>
        <button className='bg-white text-black pr-1' onClick={postDriver}>
          POST
        </button>
        <button className='bg-white text-black' onClick={getDrivers}>
          GET
        </button>
    </div>
  );
}
