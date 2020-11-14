import React from 'react';
import Navigation from './navigation';
import { types } from '../queries';
import './App.scss';
import { TextField } from '@material-ui/core';
import { Autocomplete } from '@material-ui/lab';
import { GET } from '../queries';
import { QueryImage } from '../../interfaces';

function App() {

  const onTypeChange = async (newType: string | null) => {
    if (newType === null) return;
    const reponse = await fetch(GET(newType));
    const json = await reponse.json() as QueryImage;
    console.log(json);
  }

  return (
    <>
      <Navigation />

      <div className="App container">
        <h2>What are you looking for?</h2>

        <Autocomplete
          id="combo-box-demo"
          options={types}
          onChange={(event, newType) => onTypeChange(newType)}
          getOptionLabel={(type) => type.charAt(0).toUpperCase() + type.slice(1)}
          style={{ margin: '0 auto', width: 300 }}
          renderInput={(params) => <TextField {...params} />}
        />
      </div>

    </>
  );
}

export default App;
