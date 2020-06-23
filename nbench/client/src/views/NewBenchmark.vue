<template>
  <!-- eslint-disable max-len -->
  <div>
    <h3>Add A New Benchmark </h3>
    <p>Select a group of workloads to group together into a benchmark</p>
    <form class="luci-form luci-form--compressed" >
      <div class="luci-form__field-group">
        <label for="name" class="luci-form__label">Benchmark Name</label>
        <input v-model="formData.BenchmarkName" maxlength="50" size="50" type="text" name="name" id="name" class="luci-form__input">
      </div>
      <div class="luci-form__field-group">
        <label for="description" class="luci-form__label">Benchmark Name</label>
        <input v-model="formData.Description" maxlength="100" size="100" type="text" name="description" id="description" class="luci-form__input">
      </div>
      <fieldset class="luci-form__fieldset">
    <legend class="luci-form__label">Select as many Benchmarks as you want</legend>
    <div class="luci-form__field-group">

        <span class="luci-form__checkbox" v-for="(post, index) in posts" :key="index">
            <label :for="post._id" class="luci-checkbox__label">
                <input v-model="formData.Workloads" type="checkbox" :name="post._id" :id="post._id" :value="post._id">
                <span class="luci-checkbox__button"></span>
                <span class="luci-checkbox__label-text">{{post.WorkloadName}}</span>
            </label>
        </span>

    </div>
</fieldset>
      <div class="luci-form__field-group">
        <button v-on:click='saveBenchmark()' class="luci-button luci-button--primary" > Submit</button>
      </div>
    </form>

  </div>
</template>
<script>
import Workloads from '@/services/api/workloads';
import Benchmarks from '@/services/api/benchmarks';

export default {
  name: 'NewBenchmark',

  created() {
    console.log('Page created running');
    Workloads.getWorkloads()
      .then((posts) => {
        console.log(JSON.stringify(posts));
        this.posts = posts;
      })
      .catch((error) => console.log(error))
      .finally(() => {
        this.loading = false;
      });
  },
  data() {
    return {
      formData: {
        BenchmarkName: '',
        Description: '',
        Workloads: [],
      },
    };
  },
  methods: {
    saveBenchmark() {
      return Benchmarks.saveBenchmark(this.formData);
    },
    getWorkloads() {
      return Workloads.getWorkloads();
    },
    deleteBenchmark() {
      return Benchmarks.deleteBenchmark();
    },
  },
  events: {
    saveBenchmark() {},
    deleteBenchmark() {},
  },

};
</script>
