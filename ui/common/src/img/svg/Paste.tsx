import React from 'react';
import C from '../../constants';

const DEFAULT_STYLE = { width: '20px', height: '20px', marginLeft: '5px' };
export default ({ fill = C.COLORS.GREY, style = {} }) => (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill={'#434C50'} style={{ ...DEFAULT_STYLE, ...style }}>
    <path d="M0 0h24v24H0z" fill="none" />
    <path d="M19 2h-4.18C14.4.84 13.3 0 12 0c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm7 18H5V4h2v3h10V4h2v16z" />
  </svg>
);
