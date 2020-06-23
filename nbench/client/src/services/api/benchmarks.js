import axios from 'axios';

export default {
  getBenchmarks() {
    console.log('getting benchmarks');
    return axios.get('/api/benchmark')
      // eslint-disable-next-line no-underscore-dangle
      .then((response) => response.data._items);
  },

  saveBenchmark(data) {
    const headers = {
      headers: {
        'Content-Type': 'application/json',
      },
    };
    const body = JSON.stringify(data);
    console.log('save benchmark');
    console.log(body);
    axios.post('/api/benchmark', body, headers)
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
    const url = `/api/benchmark/${docid}`;
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
