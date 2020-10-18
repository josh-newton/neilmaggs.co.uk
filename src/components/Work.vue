<template>
  <div id="work" class="content">
    <div>
      <h2>Work</h2>
      <p>Neil has worked with/for... Here is a selection of hist latest work:</p>
      <div class="articles">
        <Article
          v-for="(article, index) in articles"
          :key="index"
          :article="article" />
      </div>
    </div>
    <div class="gallery">
      <div class="image">
          <img src="../assets/neil-maggs-1.jpg" />
      </div>
      <div class="image">
          <img src="../assets/neil-maggs-2.jpg" />
      </div>
      <div class="image">
          <img src="../assets/neil-maggs-3.jpg" />
      </div>
      <div class="image">
          <img src="../assets/neil-maggs-4.jpg" />
      </div>
      <div class="image">
          <img src="../assets/neil-maggs-5.jpg" />
      </div>
      <div class="image">
          <img src="../assets/neil-maggs-6.jpg" />
      </div>
      <div class="image">
          <img src="../assets/neil-maggs-7.jpg" />
      </div>
      <div class="image">
          <img src="../assets/neil-maggs-8.jpg" />
      </div>
      <div class="image">
          <img src="../assets/neil-maggs-9.jpg" />
      </div>
      <div class="image">
          <img src="../assets/neil-maggs-10.jpg" />
      </div>
      <div class="image">
          <img src="../assets/neil-maggs-11.jpg" />
      </div>
      <div class="image">
          <img src="../assets/neil-maggs-12.jpg" />
      </div>

    </div>
  </div>
</template>

<script>
import Article from './Article';
import articles from '../data/articles.json';

export default {
  name: 'Work',
  components: {
    Article,
  },
  data() {
    return {
      articles: null,
    };
  },
  methods: {},
  mounted() {
    this.articles = articles.slice(0, 6);
  },
};
</script>

<style scoped lang="scss">
#work {
  display: flex;
  min-height: 100vh;
  height: auto;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  color: #989898;

  &.content {
    justify-content: flex-start;
    padding: 60px 0;

    > div:not(.gallery) {
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
      border-bottom: 1px solid #989898;
    }
  }

  .articles {
    display: flex;
    flex-wrap: wrap;
    margin-left: -50px;
    justify-content: space-around;
  }

  .gallery {
    margin-top: 40px;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-evenly;
    align-items: center;

    .image {
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 5px;
      img {
        max-width: 250px;
        max-height: 300px;
        border-radius: 3px;
      }
    }
  }
}
</style>
