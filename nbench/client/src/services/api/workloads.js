import axios from 'axios';

export default {
  getWorkloads() {
    return axios.get('/api/workload')
      // eslint-disable-next-line no-underscore-dangle
      .then((response) => response.data._items);
  },
  saveWorkload() {
    console.log('export save workload');
  },
};
