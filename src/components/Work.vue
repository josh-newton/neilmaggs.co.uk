<template>
  <div id="work" class="section">
    <h2 class="section-title">Work</h2>
    <div>
    </div>
    <div class="latest">
      <h3>Latest</h3>
      <div class="articles">
        <Article
          v-for="(article, index) in articles"
          :key="index"
          :article="article" />
      </div>
    </div>
    <div>
      <h3>Articles</h3>
      <p>
        Have had written pieces in The Telegraph, The Times, Wales Online,
        Daily Mirror, Daily Express, Bristol Post, Bristol Live, Birmingham Live,
        Somerset Live, Gloucestershire Live, Bristol 247, Bristol Cable.</p>
    </div>
    <div>
      <h3>Audio</h3>
      <h4>Midweek Sports Bar - BCFM Radio</h4>
      <p>
        A radio show dedicated to community sport in Bristol. Highlighting
        minority sports and minority groups and offering opportunities for new
        presenters from range of BAME, disability, age and gender groups.
        presenters from range of BAME, disability, age and gender groups.
        presenters from range of BAME, disability, age and gender groups.
        presenters from range of BAME, disability, age and gender groups.
      </p>

      <h4>Sport in the community - BBC Radio Bristol</h4>
      <p>
        A series of six community sport short documentaries on fringe sport
        activities in the Bristol, Somerset and Gloucestershire areas. Aired
        on Saturday Sport Show.
      </p>

      <h4>Under the radar – BBC Radio Bristol</h4>
      <p>
        A series of short documentaries on physical activity groups for older
        people across the west country. Aired on breakfast show.
      </p>

      <h4>BBC Radio 4 – Analysis</h4>
      <p>
        A documentary called ‘Whiteness’ examining the terms white privilege and
        white fragility and how it relates to contemporary Britain. Set in
        Bristol and London.
      </p>

      <h4>Bristol Unpacked – Bristol Cable</h4>
      <p>
        A podcast series for Bristol Cable, on Spotify, Apple Podcasts, Acast,
        and other platforms. Interviewing key people in the city on bog
        current topics.
      </p>

    </div>
    <div>
      <h3>TV/Video</h3>
      <h4>
        Doorstep Sport TV Series 1 &amp; 2 – Made TV network (Bristol, Cardiff,
        Leeds, Birmingham)
      </h4>
      <p>
        Show focused on community sport centred in Bristol. Highlighting BAME,
        women’s, and disability sport in the city.
      </p>

      <h4>Bristol Born and Bred – Reach PLC</h4>
      <p>
        Web series of features on sport stars born and raised in the city of
        Bristol. Go back to visit where they started they grew up. Guests
        include Premier league footballer Bobby Reid, UFC fighter Nad Narimani,
        former world champion boxer Lee Haskins, and ex England cricketer
        Marcus Trescothick.
      </p>

      <h4>BBC Inside Out West</h4>
      <p>
        Researcher for various documentaries including paedophile football coach
        Bob Higgins, Roma football team, holiday hunger, and black teachers.
      </p>

      <h4>BBC Two – Sea Cities</h4>
      <p>
        Researcher and sound for BBC Sea Cities series, episode focusing on
        Bristol and its martime history.
      </p>

      <h4>Community documentaries – Bristol Cable</h4>
      <p>
        A series of documentaries exploring issues in working class communities
        of Bristol. Areas include Hartcliffe, Easton, Cadbury Heath, Hillfields
        Southmead and Knowle West.
      </p>

      <h4>South Bristol and Bloody Brexit – Bristol Cable</h4>
      <p>
        Documentary on highest voting Brexit ward in Bristol – Filwood.
      </p>
    </div>
    <div>
      <h3>Comedy</h3>
      <h4>The Maggsy & Holbrook Show – Amazon Prime</h4>
      <p>
        Spoof chat show series featuring celebrity guests, including Ewen
        McIntosh from The Office, and actor Joe Sims.
      </p>
    </div>
    <div class="awards">
      <h3>Awards</h3>
      <p>
        <b>Media Mogul Awards</b> – South-West Best radio & TV presenter award
        nominee – 2019
      </p>
      <p><b>Bristol Diversity Awards</b> – Best TV producer nominee – 2018</p>
      <p><b>Bristol Diversity Awards</b> – Best radio presenter nominee – 2018</p>
      <p>
          <b>Media Mogul Awards</b> – South West Best radio & TV presenter award
          nominee – 2018
      </p>
      <p>
        <b>Community Radio show of the Year</b> – Gold at the National Radio Awards
        2017
      </p>
      <p><b>Most LGBT+ friendly radio show</b> – Shout Out Awards nominee 2016</p>
      <p><b>Media Project of the Year</b> - Thank You Awards – Up Our Street 2015</p>
      <p><b>BBC Power of Sport West nominee</b> – 2009</p>
      <p><b>SWEB services to sport in the West</b> – 2010</p>
    </div>
    <div class="gallery">
      <div class="image" v-for="(image, index) in new Array(12)" :key="index">
          <img :src="require(`../assets/neil-maggs-${index + 1}.jpg`)" />
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
    this.articles = articles.slice(0, 4);
  },
};
</script>

<style scoped lang="scss">
#work {
  &.section {
    padding: 3em;
  }

  .latest h3 {
    margin-bottom: 0;
  }

  .articles {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
  }

  .awards p {
    margin-bottom: 0;
  }

  .gallery {
    margin-top: 60px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;

    .image {
      display: flex;
      align-items: center;
      margin: 1em;
      img {
        max-width: 250px;
        max-height: 300px;
        border-radius: 3px;
      }
    }
  }
}
</style>
