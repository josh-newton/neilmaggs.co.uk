<template>
  <div id="hero">
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
  height: 946px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align: center;
  color: #ffffff;
  background: url('../assets/hero.png') no-repeat top center;
  background-size: cover;

  h1 {
    margin-bottom: 20px;
    font-size: 100px;
    padding-bottom: 20px;
    border-bottom: 2px solid #dcdcdc;
    text-shadow: 1px 1px 3px #696969;
    box-shadow: 0px 1px 0px #696969;
  }

  h2 {
    font-size: 38px;
    text-shadow: 1px 1px 3px #696969;
    text-transform: none;
  }
}
</style>
