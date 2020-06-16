import axios from 'axios';

export default {
  getWorkloads() {
    return axios.get('/api/benchmark')
      // eslint-disable-next-line no-underscore-dangle
      .then((response) => response.data._items);
  },
};
