<template>
  <!-- eslint-disable max-len -->
  <div>

    <h1>Settings</h1>
    <hr>
    <h3>vCenter</h3>
    <form class="luci-form luci-form--compressed">

      <div class="luci-form__field-group">
        <label for="address" class="luci-form__label">vCenter FQDN or IP</label>
        <input v-model="vcenter.address" type="text" name="address" id="address"
               class="luci-form__input">
      </div>
      <div class="luci-form__field-group">
        <label for="username" class="luci-form__label">vCenter Username</label>
        <input v-model="vcenter.username" type="text" name="username" id="username"
               class="luci-form__input">
      </div>
      <div class="luci-form__field-group">
        <label for="name" class="luci-form__label">vCenter Password</label>
        <input v-model="vcenter.password" type="password" name="name" id="name"
               class="luci-form__input">
      </div>
            <div class="luci-form__field-group">
        <button v-on:click='savevCenter()' class="luci-button luci-button--primary" > Submit</button>
      </div>
    </form>
  <p>TODO: Should we allow for multiple vCenter configurations</p>
  </div>
</template>

<script>

import Settings from '@/services/api/settings';

export default {
  name: 'Settings',

  data() {
    return {
      vcenter: {
        address: '',
        username: 'administrator@vsphere.local',
        password: 'NetApp!23',
      },
    };
  },
  created() {
    Settings.getvCenter()
      .then((posts) => {
        console.log(JSON.stringify(posts));
        // eslint-disable-next-line no-underscore-dangle
        this.vcenter.username = posts._items[0].username;
        // eslint-disable-next-line no-underscore-dangle
        this.vcenter.password = posts._items[0].password;
        // eslint-disable-next-line no-underscore-dangle
        this.vcenter.address = posts._items[0].address;
      })
      .catch((error) => console.log(error))
      .finally(() => {
        this.loading = false;
      });
  },
  methods: {
    savevCenter() {
      return Settings.savevCenter(this.vcenter);
    },
    get() {
      return Settings.getvCenter();
    },
    deletevCenter() {
      return Settings.deletevCenter();
    },
  },
  events: {
    savevCenter() {
    },
    deletevCenter() {
    },
  },

};
</script>
