import axios from 'axios';

export default {
  getWorkloads() {
    console.log('Running getWorkloads from workloads.js');
    axios.get('/api/logger?test=ing');
    return axios.get('/api/workload')
      // eslint-disable-next-line no-underscore-dangle
      .then((response) => response.data._items);
  },

  saveWorkload(data) {
    const headers = {
      headers: {
        'Content-Type': 'application/json',
      },
    };
    const body = JSON.stringify(data);
    console.log('Save Workload');
    console.log(body);
    axios.post('/api/workload', body, headers)
      .then((res) => {
        console.log('RESPONSE: ', res);
      })
      .catch((err) => {
        console.log('Error: ', err);
      });

    return 'nothing';
  },

  deleteWorkload(etag, docid) {
    const headers = {
      headers: {
        'Content-Type': 'application/json',
        'If-Match': etag,
      },
    };
    const url = `/api/workload/${docid}`;
    axios.delete(url, headers)
      .then((res) => {
        console.log('RESPONSE: ', res);
      })
      .catch((err) => {
        console.log('Error: ', err);
      });

    return 'nothing';
  },
};
