import React, { useState, useEffect } from 'react';

interface Member {
  // Define the structure of a member object based on the API response
  id: number;
  name: string;
}

interface Data {
  members: Member[];
}

function App() {

  const [data, setData] = useState<Data>({ members: [] });

  useEffect(() => {
    fetch("/members")
      .then(res => res.json())
      .then(data => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-bold underline">
        Hello world!
      </h1>
      {data.members.length === 0 ? (
        <p>Loading...</p>
      ) : (
        data.members.map((member, i) => (
          <p key={i}>{member.name}</p>
        ))
      )}
    </div>
  );
}

export default App;
