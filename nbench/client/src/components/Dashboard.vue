<template>
  <!-- eslint-disable max-len -->
  <div class="dashboard">
    <h1>There are currently no tests running</h1>
    <h3>How it works</h3>
    <p>
      NBench is a benchmarking tool that allows you to define any number of workloads
      and organize them into different benchmarks. Each workload can represent different aspects
      of a real world environment. Running them concurrently as a single benchmark provides
      you with a true understanding of how your environment will operate under real world loads.
    </p>
    <h3>To get started</h3>
    <p>
      Start by reviewing the available workloads or add a few of your own.  Workloads are based
      on a number of factors, you can start by reviewing the pre-configured benchmarks and then
      examine your applications and environment to add as many as needed.
    </p>
    <p>
      Next, Arrange the different workloads into a benchmark suite. Here you will need to
      define which datastore will be used for each workload. The system will create the needed
      number of virtual machines, configure the datastores and run the benchmarks.
    </p>
    <p>
      Finally, you can watch a running benchmark on the Dashboard. Once it's finished the results
      will be available for review.
    </p>

  </div>
</template>

<script>
export default {
  name: 'Dashboard',
};
</script>
