<template>
  <div class="guest-interface">
    <h1>Guest Interface</h1>
    <hr><br><br>
    <Acess/>
  </div>
</template>

<script>
// @ is an alias to /src
import Acess from '@/components/Acess.vue';

export default {
  name: 'Guest',
  components: {
    Acess,
  },
};
</script>
