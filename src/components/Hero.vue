<template>
  <div id="hero">
    <div class="image"></div>
    <h1>Neil Maggs</h1>
    <h2>Journalist &middot; Presenter &middot; Host</h2>
  </div>
</template>

<script>

export default {
  name: 'Hero',
  data() {
    return {};
  },
  methods: {},
};
</script>

<style scoped lang="scss">
#hero {
  height: 100vh;
  min-height: 900px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align: center;
  color: #ffffff;

  .image {
    position: absolute;
    min-height: 100%;
    width: 100%;
    height: auto;
    top: 0;
    left: 0;
    background: url('../assets/hero.png') no-repeat top center;
    background-size: cover;
    z-index: -1;
  }

  *:not(.image) {
    z-index: 10;
  }

  h1 {
    margin-top: -100px;
    text-transform: uppercase;
    margin-bottom: 20px;
    font-size: 100px;
    padding-bottom: 20px;
    border-bottom: 1px solid #dcdcdc;
    text-shadow: 1px 1px 3px #696969;
    box-shadow: 0px 1px 0px #696969;
  }

  h2 {
    font-size: 38px;
    margin-top: 0;
    font-weight: normal;
    text-shadow: 1px 1px 3px #696969;
  }
}
</style>
