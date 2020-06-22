<template>
  <div>
    <div class="luci-grid">
      <div class="luci-grid__col luci-grid__col-8"> <h1>Storage Workloads</h1> </div>
      <div class="luci-grid__col luci-grid__col-3">
          <button class="luci-button luci-button--primary" @click="$router.push('/newworkload')">
                New Workload
          </button>
      </div>
    </div>
    <div class="luci-table">
      <span onclick="workloads()"></span>
      <table class="luci-table__table">
        <thead>
        <tr>
          <th class="" scope="col">Name</th>
          <th class="" scope="col">Block Size</th>
          <th class="" scope="col">File Size</th>
          <th class="" scope="col">Runtime</th>
          <th class="" scope="col">IO Engine</th>
          <th class="" scope="col">&nbsp;</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="post in posts" :key="post.name">
          <td> {{post.name}} </td>
          <td> {{post.blocksize}} </td>
          <td> {{post.size}} </td>
          <td> {{post.runtime}} </td>
          <td> {{post.ioengine}} </td>
          <td> <a href="#">Remove</a> </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import WorkloadApi from '@/services/api/workloads';

export default {
  name: 'Workloads',

  data() {
    return {
      loading: true,
      posts: [],
    };
  },

  created() {
    WorkloadApi.getWorkloads()
      .then((posts) => {
        console.log(posts);
        this.posts = posts;
      })
      .catch((error) => console.log(error))
      .finally(() => {
        this.loading = false;
      });
  },
};
</script>
