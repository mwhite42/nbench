import axios from 'axios';

export default {
  getvCenter() {
    console.log('Running getvCenter');
    return axios.get('/api/settings/vCenter')
      // eslint-disable-next-line no-underscore-dangle
      .then((response) => response.data);
  },
  savevCenter(data) {
    const headers = {
      headers: {
        'Content-Type': 'application/json',
      },
    };
    const body = JSON.stringify(data);
    console.log('Save vCenter Settings');
    console.log(body);
    axios.post('/api/settings/vCenter', body, headers)
      .then((res) => {
        console.log('RESPONSE: ', res);
      })
      .catch((err) => {
        console.log('Error: ', err);
      });

    return 'nothing';
  },
  // TODO: implement delete
  deletevCenter() {
  },
};
