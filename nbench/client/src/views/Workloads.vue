<template>
  <div>
    <div class="luci-grid">
      <div class="luci-grid__col luci-grid__col-8"> <h1>Workloads</h1> </div>
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
        <tr v-for="(post, index) in posts" :key="index">
          <td> {{post.WorkloadName}} </td>
          <td> {{post.blockSize}} </td>
          <td> {{post.fileSize}} </td>
          <td> {{post.runTime}} </td>
          <td> {{post.ioEngine}} </td>
          <td>
             <button v-on:click='deleteWorkload(post._etag, post._id, index)'
                     class="luci-button luci-button--small" > Remove
             </button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import Workload from '@/services/api/workloads';

export default {
  name: 'Workloads',

  data() {
    return {
      loading: true,
      posts: [],
    };
  },

  created() {
    Workload.getWorkloads()
      .then((posts) => {
        console.log(posts);
        this.posts = posts;
      })
      .catch((error) => console.log(error))
      .finally(() => {
        this.loading = false;
      });
  },
  methods: {
    deleteWorkload(etag, docid, index) {
      console.log('Delete Workload', etag, ' | ', docid);

      Workload.deleteWorkload(etag, docid);
      this.posts.splice(index);
    },
  },
  events: {
    deleteWorkload() {},
  },
};
</script>
