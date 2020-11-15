import React, { useState } from 'react';
import Navigation from './navigation';
import { types } from '../queries';
import './App.scss';
import { TextField } from '@material-ui/core';
import { Autocomplete } from '@material-ui/lab';
import { SEARCH } from '../queries';
import { QueryImage } from '../interfaces';
import Gallery from './gallery';

function App() {
  const [search, setSearch] = useState<string>();
  const [images, setImages] = useState<QueryImage[]>();

  const onTypeChange = async (newType: string | null) => {
    if (newType === null) return;
    const reponse = await fetch(SEARCH(newType));
    const images = await reponse.json() as QueryImage[];
    setImages(images);
    setSearch(newType);
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
          style={{ margin: '0 auto 24px', width: 300 }}
          renderInput={(params) => <TextField {...params} />}
        />

        {(images && search) && <Gallery {...{ images, search }} />}
      </div>

    </>
  );
}

export default App;
