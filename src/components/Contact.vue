<template>
  <div id="contact" class="section">
    <h2 class="section-title">Contact</h2>
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
  align-items: center;
  flex-direction: column;

  .links {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
    width: 60%;
  }

  a, a:visited, a:active, a:focus {
    color: #272727;
    text-decoration: none;
    display: flex;
    align-items: center;
    padding: 10px 20px;
    transition: color 0.2s;
  }

  a:hover {
    color: lighten(#272727, 40%);
  }

  i {
    font-size: 22px;
    padding-right: 10px;
  }
}
</style>
