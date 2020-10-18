<template>
  <section id="contact" class="content">
    <div>
      <h2>Contact</h2>
      <div class="links">
        <a href="mailto:info@neilmaggs.co.uk">
          <span><i class="fas fa-at"></i></span><span>info@neilmaggs.co.uk</span>
        </a>
        <a href="https://twitter.com/neilmaggs2" target="_blank">
          <span><i class="fab fa-twitter-square"></i></span><span>twitter.com/neilmaggs2</span>
        </a>
        <a href="https://linkedin.com/in/neil-maggs-734866131" target="_blank">
          <span><i class="fab fa-linkedin"></i></span><span>linkedin.com/in/neil-maggs</span>
        </a>
      </div>
    </div>
  </section>
</template>

<script>

export default {
  name: 'Contact',
  data() {
    return {};
  },
  methods: {},
};
</script>

<style scoped lang="scss">
#contact {
  display: flex;
  min-height: 100vh;
  height: auto;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  color: #989898;
  min-height: 250px;

  &.content {
    justify-content: flex-start;
    padding: 60px 0;

    > div {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: left;
      width: 60vw;
    }

    h2 {
      font-size: 28px;
      margin-top: 0;
      font-weight: normal;
      padding-bottom: 20px;
      border-bottom: 1px solid #fff;
      text-align: center;
      width: 80%;
      align-self: center;
    }
  }
  h2 {
    border-bottom: 1px solid #989898;
  }

  .links {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
  }


  a, a:visited, a:active, a:focus {
    color: #989898;
    text-decoration: none;
    display: flex;
    align-items: center;
    padding: 10px 20px;
    transition: color 0.2s;
  }

  a:hover {
    color: darken(#989898, 20%);
  }

  i {
    font-size: 22px;
    padding-right: 10px;
  }
}
</style>
