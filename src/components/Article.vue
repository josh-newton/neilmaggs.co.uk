<template>
  <div class="article">
    <div class="image" v-if="article.image">
      <a :href="article.link" target="_blank"><img :src="article.image"/></a>
    </div>
    <div class="title">
      <h4><a :href="article.link" target="_blank">{{ article.title }}</a></h4>
    </div>
    <div class="description">
      <p>{{ article.description }}</p>
    </div>
    <div class="date">
      <p>{{ article.date }}</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Article',
  props: ['article'],
};
</script>

<style scoped lang="scss">
.article {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 30px;
  width: 450px;
  max-width: 600px;
  flex-grow: 1;
}
p {
  margin-top: 0;
}
.title {
  text-transform: uppercase;
  a, a:visited, a:active, a:focus {
    color: #272727;
    text-decoration: none;
    transition: color 0.2s;
  }

  a:hover {
    color: lighten(#272727, 50%);
  }
}
.image img {
  width: 100%;
  border-radius: 3px;
}
.date {
  align-self: flex-start;
  font-size: 14px;
}
h4 {
  font-size: 1.17em;
  font-weight: 400;
  margin: 1em 0;
}
</style>
