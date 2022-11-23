import React from 'react';
import C from '../../constants';

const DEFAULT_STYLE = { width: '20px', height: '20px', marginLeft: '5px' };
export default ({ fill = C.COLORS.GREY, style = {} }) => {
  return (
    <svg fill={fill} style={{ ...DEFAULT_STYLE, ...style }} viewBox="0 0 20 22" xmlns="http://www.w3.org/2000/svg">
      <path d="M5.89614 0.103822C4.90828 0.319131 4.01799 0.780505 3.31064 1.44488C1.79227 2.87207 1.22517 4.91442 1.76788 6.94447C2.13985 8.31629 3.20088 9.6389 4.45094 10.2787L4.72534 10.4202L4.51192 10.5739C4.39606 10.6601 4.07287 10.9615 3.79847 11.2445L3.29844 11.7551H2.70085C1.78008 11.7551 1.25566 11.9519 0.792221 12.4687C0.322686 12.9916 0.078771 13.5944 0.0177923 14.3511C-0.0187949 14.8186 -0.012697 14.8247 0.170239 15.0093C0.322686 15.1631 0.408056 15.2 0.621481 15.2C1.04833 15.1938 1.15809 15.0647 1.25566 14.4372C1.35322 13.8405 1.48128 13.5329 1.76178 13.2684C1.92033 13.1146 2.01789 13.0838 2.32279 13.0592C2.66427 13.0346 2.69476 13.0408 2.66427 13.1453C2.49962 13.7113 2.47523 13.9082 2.46913 14.6771C2.46913 15.5937 2.54231 16.0981 2.78622 16.8548C3.61553 19.4508 5.68271 21.2901 8.43285 21.8869C9.05483 22.0222 10.9269 22.0406 11.494 21.9176C13.1465 21.5547 14.36 20.9087 15.4332 19.8199C16.3906 18.8479 17.0186 17.7468 17.3601 16.4488C17.5796 15.606 17.6223 14.1542 17.4516 13.4837L17.3357 13.0346L17.6955 13.0592C17.9821 13.0777 18.0858 13.1207 18.2321 13.2622C18.4943 13.5144 18.659 13.8958 18.7504 14.468C18.8419 15.0647 18.9578 15.1938 19.3785 15.2C19.5919 15.2 19.6773 15.1631 19.8298 15.0093C20.0127 14.8247 20.0188 14.8186 19.9822 14.3511C19.9212 13.5944 19.6773 12.9916 19.2078 12.4687C18.7443 11.9519 18.2199 11.7551 17.293 11.7551H16.6772L16.415 11.4229C16.1832 11.1338 15.8174 10.8016 15.4088 10.5063C15.3051 10.4325 15.3356 10.4017 15.7869 10.1372C16.9394 9.4605 17.8845 8.23017 18.2321 6.94447C19.0736 3.82558 17.2016 0.755898 14.0673 0.103822C13.4026 -0.0376659 6.53641 -0.0315142 5.89614 0.103822ZM14.0856 1.37722C14.8051 1.59252 15.421 1.96162 15.9454 2.49067C16.5003 3.04432 16.7381 3.42572 16.9882 4.15777C17.1406 4.60069 17.1589 4.73602 17.1589 5.44962C17.1589 6.16321 17.1406 6.29855 16.9882 6.74147C16.7381 7.47351 16.5003 7.85492 15.9454 8.41472C15.5308 8.82688 15.3417 8.96222 14.8722 9.18983C13.9331 9.64505 14.0612 9.63275 10 9.63275C5.93882 9.63275 6.06688 9.64505 5.1278 9.18983C4.65827 8.96222 4.46923 8.82688 4.05458 8.41472C3.49967 7.85492 3.26186 7.47351 3.01184 6.74147C2.8594 6.29855 2.8411 6.16321 2.8411 5.44962C2.8411 4.73602 2.8594 4.60069 3.01184 4.15777C3.26186 3.42572 3.49967 3.04432 4.04848 2.49682C4.71315 1.83244 5.47538 1.43258 6.34128 1.29724C6.52422 1.27264 8.26821 1.25418 10.2134 1.26033C13.2989 1.27264 13.7929 1.28494 14.0856 1.37722ZM13.0916 10.9554C15.0917 11.2199 16.4454 12.9116 16.3235 14.9785C16.232 16.4365 15.6527 17.7775 14.6466 18.8356C12.055 21.5793 7.36572 21.3886 5.03634 18.4542C3.59724 16.6333 3.28015 14.1358 4.29849 12.5855C4.87779 11.712 5.86565 11.0845 6.89009 10.9554C7.39621 10.8877 12.5855 10.8877 13.0916 10.9554Z" />
      <path d="M6.42078 3.33346C6.04272 3.42573 5.43903 3.8625 5.20121 4.21315C4.75607 4.87137 4.70119 5.70184 5.05486 6.43389C5.75612 7.86723 7.73792 8.03332 8.70139 6.74763C9.33556 5.89255 9.2441 4.66837 8.48796 3.92402C7.96354 3.40113 7.12204 3.16737 6.42078 3.33346ZM7.57938 4.79755C7.82939 5.03132 7.83549 5.04977 7.83549 5.43117C7.83549 6.02788 7.53669 6.34162 6.96959 6.34162C6.43908 6.34162 6.0793 5.97867 6.0793 5.44963C6.0793 4.90828 6.43908 4.55764 7.00008 4.55764C7.29278 4.55764 7.34766 4.58224 7.57938 4.79755Z" />
      <path d="M12.5248 3.32111C11.4821 3.59179 10.7504 4.64987 10.8845 5.69565C11.0431 7.01826 12.3907 7.91025 13.6346 7.51654C14.6469 7.20281 15.2445 6.33542 15.1713 5.28349C15.092 4.18235 14.2505 3.35187 13.1529 3.29651C12.9151 3.2842 12.6285 3.29036 12.5248 3.32111ZM13.5676 4.70524C13.8969 4.92669 14.0249 5.4988 13.8237 5.8925C13.659 6.20624 13.348 6.36003 12.9517 6.32927C12.6651 6.30466 12.5797 6.26775 12.3968 6.08321C12.1285 5.80638 12.0553 5.38807 12.226 5.03127C12.4517 4.54529 13.0919 4.3915 13.5676 4.70524Z" />
    </svg>
  );
};
