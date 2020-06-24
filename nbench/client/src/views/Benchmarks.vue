<template>
  <div>
    <div class="luci-grid">
      <div class="luci-grid__col luci-grid__col-8"> <h1>Benchmarks</h1> </div>
      <div class="luci-grid__col luci-grid__col-3">
          <button class="luci-button luci-button--primary" @click="$router.push('/newbenchmark')">
                New Benchmark
          </button>
      </div>
    </div>
    <div class="luci-table">
      <span onclick="workloads()"></span>
      <table class="luci-table__table">
        <thead>
        <tr>
          <th class="" scope="col">Name</th>
          <th class="" scope="col">Description</th>
          <th class="" scope="col">Created</th>
          <th class="" scope="col">&nbsp;</th>
          <th class="" scope="col">&nbsp;</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(post, index) in posts" :key="index">
          <td> {{post.BenchmarkName}} </td>
          <td> {{post.Description}}</td>
          <td> {{post._created}}</td>
          <td>
             <button v-on:click='runBenchmark(post._etag, post._id, index)'
                     class="luci-button luci-button--small" > Run
             </button>
          </td>
          <td>
            <button v-on:click='deleteBenchmark(post._etag, post._id, index)'
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
import Benchmark from '@/services/api/benchmarks';

export default {
  name: 'Benchmark',

  data() {
    return {
      loading: true,
      posts: [],
    };
  },

  created() {
    Benchmark.getBenchmarks()
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
    deleteBenchmark(etag, docid, index) {
      console.log('Delete Benchmark', etag, ' | ', docid);

      Benchmark.deleteBenchmark(etag, docid);
      this.posts.splice(index);
    },
    runBenchmark(etag, docid, index) {
      console.log('Run Benchmark', etag, ' | ', docid, ' | ', index);
      this.$router.push('Home');
    },
  },
  events: {
    deleteBenchmark() {},
    runBenchmark() {},
  },
};
</script>
