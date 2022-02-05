<template>
  <div class="host-interface">
    <h1>Host Interface</h1>
    <hr><br><br>
    <Acess/>
  </div>
</template>

<script>
// @ is an alias to /src
import Acess from '@/components/Acess.vue';

export default {
  name: 'Host',
  components: {
    Acess,
  },
};
</script>
