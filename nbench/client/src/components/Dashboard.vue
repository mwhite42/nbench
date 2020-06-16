<template>
  <!-- eslint-disable max-len -->
  <div class="dashboard">
    <h1>There are currently no tests running</h1>
    <h3>To get started</h3>
    <p>
      Start by reviewing the available workloads or add a few of your own.
    </p>
    <p>
      Next, Arrange the different workloads into a benchmark suite. Here you will need to
      define which datastore will be used for each workload.
    </p>
    <p>
      Then we need to run the benchmark, this will create the required number of virutal machines,
      configure them with the correct datastore and start the benchmark suite.
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
