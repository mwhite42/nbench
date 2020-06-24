<template>
  <!-- eslint-disable max-len -->
  <div>
    <h3>Add A New Benchmark </h3>
    <p>Select a group of workloads to group together into a benchmark</p>
    <form class="luci-form luci-form--compressed">
      <div class="luci-grid">
        <div class="luci-grid__col luci-grid__col-4">
          <div class="luci-form__field-group">
            <label for="name" class="luci-form__label">Benchmark Name</label>
            <input v-model="formData.BenchmarkName" maxlength="50" size="50" type="text" name="name"
                   id="name" class="luci-form__input">
          </div>
        </div>
        <div class="luci-grid__col luci-grid__col-8">
          <div class="luci-form__field-group">
            <label for="description" class="luci-form__label">Benchmark Description</label>
            <input v-model="formData.Description" maxlength="100" size="100" type="text"
                   name="description" id="description" class="luci-form__input">
          </div>
        </div>
      </div>
      <div class="luci-grid">
        <div class="luci-grid__col luci-grid__col-4">
          <div class="luci-form__field-group">
            <label for="datastore" class="luci-form__label">Datastore</label>
            <span class="luci-form__select-wrapper">
            <select v-model="formData.DatastoreName" class="luci-form__select luci-form__input"
                    name="datastore" id="datastore">
                <option v-for="(datastoreitem, index) in datastorelist" :key="index"
                        class="luci-form__select-option">
                  {{datastoreitem.name}}
                </option>
            </select>
          </span>
          </div>
        </div>
        <div class="luci-grid__col luci-grid__col-2">
          <div class="vld-parent">
            <loading :active.sync="isLoading" :is-full-page=true></loading>
          </div>
        </div>
        <div class="luci-grid__col luci-grid__col-6">
        </div>
      </div>
      <fieldset class="luci-form__fieldset">
        <legend class="luci-form__label">Select as many Benchmarks as you want</legend>
        <div class="luci-form__field-group">
        <span class="luci-form__checkbox" v-for="(workloaditem, index) in workloadlist"
              :key="index">
            <label :for="workloaditem._id" class="luci-checkbox__label">
                <input v-model="formData.Workloads" type="checkbox" :name="workloaditem._id"
                       :id="workloaditem._id" :value="workloaditem._id">
                <span class="luci-checkbox__button"></span>
                <span class="luci-checkbox__label-text">{{workloaditem.WorkloadName}}</span>
            </label>
        </span>
        </div>
      </fieldset>
      <div class="luci-form__field-group">
        <button v-on:click='saveBenchmark()' class="luci-button luci-button--primary"> Submit
        </button>
      </div>
    </form>

  </div>
</template>
<script>
import Workloads from '@/services/api/workloads';
import Benchmarks from '@/services/api/benchmarks';
import Loading from 'vue-loading-overlay';

export default {
  name: 'NewBenchmark',

  created() {
    console.log('Page created running');
    Workloads.getWorkloads()
      .then((workloadlist) => {
        console.log(JSON.stringify(workloadlist));
        this.workloadlist = workloadlist;
      })
      .catch((error) => console.log(error))
      .finally(() => {
      });
    Workloads.getDatastores()
      .then((datastorelist) => {
        // console.log(JSON.stringify(datastorelist));
        console.log(JSON.stringify(datastorelist.datastores));
        this.datastorelist = datastorelist.datastores;
        this.isLoading = false;
      });
  },
  data() {
    return {
      formData: {
        BenchmarkName: '',
        Description: '',
        DatastoreName: '',
        Workloads: [],
      },
      datastorelist: ['Loading'],
      workloadlist: [],
      isLoading: true,
      fullPage: true,
    };
  },
  components: {
    Loading,
  },
  methods: {
    saveBenchmark() {
      Benchmarks.saveBenchmark(this.formData);
      this.$router.push('benchmarks');
    },

    getWorkloads() {
      return Workloads.getWorkloads();
    },
    deleteBenchmark() {
      return Benchmarks.deleteBenchmark();
    },
  },
  events: {
    saveBenchmark() {
    },
    deleteBenchmark() {
    },
  },

};
</script>
