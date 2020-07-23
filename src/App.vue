<template>
  <div class="app">
    <Home />
  </div>
</template>

<script>
import Home from './components/Home.vue';

export default {
  name: 'App',
  components: {
    Home,
  },
};
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Montserrat&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css');

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: 'Montserrat', sans-serif;
  background: ghostwhite;
}

h1, h2, h3{
  font-family: 'Montserrat', sans-serif;
  font-weight: 400;
}
</style>
