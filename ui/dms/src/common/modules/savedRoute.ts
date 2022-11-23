import { ProviderLocalStorage } from '../../providers';
import { C } from '../index';

const getCurrentRoute = () => {
  const currentRoute = window.location.pathname;

  if (currentRoute.endsWith('/')) return currentRoute.slice(0, -1);

  return currentRoute;
};

export const restore = () => {
  const savedRoute = ProviderLocalStorage.get(C.STORAGE.PREVIOUS_ROUTE);
  const currentRoute = getCurrentRoute();

  if (savedRoute && currentRoute === C.URLS.BASE_PATH) {
    history.replaceState(null, null, savedRoute);
  }
};

export const update = () => {
  const route = window.location.pathname + window.location.search;
  ProviderLocalStorage.set(C.STORAGE.PREVIOUS_ROUTE, route);
};
