import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';
import './index.scss';

import { theme } from './theme'
import { ThemeProvider } from '@material-ui/core';

ReactDOM.render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <App />
    </ThemeProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
