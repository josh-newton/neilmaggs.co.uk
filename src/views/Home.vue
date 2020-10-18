<template>
  <div>
    <Nav />
    <div class="container">
      <Hero />
      <Work />
      <Bio />
      <Contact />
    </div>
  </div>
</template>

<script>
import Nav from '../components/Nav';
import Hero from '../components/Hero';
import Work from '../components/Work';
import Bio from '../components/Bio';
import Contact from '../components/Contact';

export default {
  name: 'Home',
  components: {
    Nav,
    Hero,
    Work,
    Bio,
    Contact,
  },
  props: {},
  data() {
    return {};
  },
  methods: {},
};
</script>

<style scoped lang="scss">
@import '../styles/index.scss';
</style>
