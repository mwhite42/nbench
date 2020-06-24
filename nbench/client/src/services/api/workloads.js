import axios from 'axios';
import Vue from 'vue';

export default {
  getWorkloads() {
    this.isLoading = true;
    console.log('Running getWorkloads from workloads.js');
    return axios.get('/api/workload')
      // eslint-disable-next-line no-underscore-dangle
      .then((response) => response.data._items);
  },

  getDatastores() {
    this.isLoading = true;
    console.log('Running getDatastores from workloads.js');
    return axios.get('/api/getDatastores')
      .then((response) => response.data);
  },

  saveWorkload(data) {
    this.isLoading = true;
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
    this.isLoading = false;
    Vue.notify({
      group: 'foo',
      title: 'Test message',
      text: 'This is a test',
      duration: 60000,
      closeOnClick: true,
    });
  },

  deleteWorkload(etag, docid) {
    this.isLoading = true;
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
    this.isLoading = false;
  },
};
