import React from 'react';
import { useRouter } from '../common/hooks';
import Header from './Header';
import './layout.scss';

const goBack = (event, history) => {
  event.preventDefault();
  history.goBack();
};

const BackLink = ({ history }) => (
  <div className="back-link">
    <a href="#" onClick={event => goBack(event, history)}>
      {'<- Go back'}
    </a>
  </div>
);

const Layout = props => {
  const { history, pathname } = useRouter();
  const splittedPath = pathname.split('/');

  const isEntity = splittedPath.length === 3;
  const isPlanImg =
    splittedPath.length >= 3 &&
    // URL /admin/floor/plan?floor_id=XXX has no backbutton
    splittedPath[1] === 'floor' &&
    splittedPath[2] === 'plan';

  const isThereAPreviousPageToGoBack = history && history.length > 1;
  const showBackLink = isEntity && isThereAPreviousPageToGoBack && !isPlanImg;
  return (
    <div className="layout">
      <div id="left-sidebar" />
      <div className="main">
        <Header title={pathname} />
        {showBackLink && <BackLink history={history} />}
        <div className="layout-content">{props.children}</div>
      </div>
    </div>
  );
};

export default Layout;
