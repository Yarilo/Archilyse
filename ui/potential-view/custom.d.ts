// we need to have this file in order to jest tests work
declare module '*.gif';
declare module '*.png';
declare module '*.csv' {
  const content: any;
  export default content;
}
