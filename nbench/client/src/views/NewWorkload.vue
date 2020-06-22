<script>
export default function saveWorkload() {
  console.log('Saving it ');
  console.log('Hopefully');
}
</script>

<template>
  <!-- eslint-disable max-len -->
  <div>
    <h3>New Workload Form</h3>
    <form class="luci-form luci-form--compressed" >
      <div class="luci-form__field-group">
        <label for="name" class="luci-form__label">Test Name</label>
        <input type="text" name="name" id="name" class="luci-form__input">
      </div>
      <div class="luci-form__field-group">
        <label for="blocksize" class="luci-form__label">Block Size</label>
        <input type="text" name="blocksize" id="blocksize" class="luci-form__input">
      </div>
      <div class="luci-form__field-group">
        <label for="size" class="luci-form__label">File Size</label>
        <input type="text" name="size" id="size" class="luci-form__input">
      </div>
      <div class="luci-form__field-group">
        <label for="runtime" class="luci-form__label">Test run time (seconds)</label>
        <input type="text" name="runtime" id="runtime" class="luci-form__input">
      </div>
      <div class="luci-form__field-group">
        <label for="ioengine" class="luci-form__label">IO Engine</label>
        <span class="luci-form__select-wrapper">
            <select class="luci-form__select luci-form__input" name="ioengine" id="ioengine">
                <option v-for="(ioengine, index) in ioengines" :key="index" class="luci-form__select-option">{{ioengine}}</option>
            </select>
        </span>
      </div>
      <div class="luci-form__field-group">
        <label for="rw" class="luci-form__label">IO Engine</label>
        <span class="luci-form__select-wrapper">
            <select class="luci-form__select luci-form__input" name="rw" id="rw">
                <option v-for="(item, index) in modes" :key="index" class="luci-form__select-option">{{item}}</option>
            </select>
        </span>
      </div>
      <div class="luci-form__field-group">
        <button class="luci-button luci-button--primary" onclick="saveWorkload()"> Submit</button>
      </div>
    </form>
  </div>
</template>
<script>

export default {
  name: 'NewWorkload',

  data() {
    return {
      ioengines: ['sync', 'psync', 'vsync', 'pvsync', 'pvsync2', 'io_uring', 'libaio', 'posixaio',
        'solarisaio', 'windowsaio', 'mmap', 'splice', 'sg', 'null', 'net', 'netsplice', 'cpuio',
        'guasi', 'rdma', 'falloc', 'ftruncate', 'e4defrag', 'rados', 'rdb', 'http', 'gfapi',
        'gfapi_async', 'libhdfs', 'mtd', 'pmemblk', 'dev-dax', 'external', 'filecreate',
        'filestat', 'libpmem', 'ime_psync', 'ime_psyncv', 'ime_aio', 'libiscsi', 'nbd'],
      modes: ['read', 'write', 'trim', 'randread', 'randwrite', 'randtrim', 'readwrite',
        'randrw', 'trimwrite'],
    };
  },

};

</script>
