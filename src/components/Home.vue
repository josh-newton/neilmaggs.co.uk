<template>
  <div class="container">
    <div
      class="scroll"
      @click.prevent="scrollTo('bio')">
      <a href="#work"><i class="fas fa-chevron-down"></i></a>
    </div>

    <nav
      id="navbar"
      @click="setNavVisible(!navVisible)"
      :class="{ sticky: stickyNavActive }">
      <ul :class="{ open: navVisible }">
        <li
          @click.prevent="scrollTo('work')"
          :class="{ active: navLinkActive == 'work'}">
          <a href="#work">Work</a>
        </li>
        <li
          @click.prevent="scrollTo('bio')"
          :class="{ active: navLinkActive == 'bio'}">
          <a href="#bio">Bio</a>
        </li>
        <li
          @click.prevent="scrollTo('contact')"
          :class="{ active: navLinkActive == 'contact'}">
          <a href="#contact">Contact</a>
        </li>
      </ul>
    </nav>
    <div
      class="hamburger"
      :class="{ open: navVisible }"
      @click="setNavVisible(!navVisible)">
      <div class="line"></div>
      <div class="line"></div>
      <div class="line"></div>
    </div>

    <section id="hero">
      <div class="image"></div>
      <h1>Neil Maggs</h1>
      <h2>Journalist &middot; Presenter &middot; Host</h2>
    </section>

    <section id="work" class="content">
      <div>
        <h2>Work</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
        enim ad minim veniam, quis nostrud exercitation ullamco laboris
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
        reprehenderit in voluptate velit esse cillum dolore eu fugiat
        nulla pariatur. Excepteur sint occaecat cupidatat non proident,
        sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
        enim ad minim veniam, quis nostrud exercitation ullamco laboris
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
        reprehenderit in voluptate velit esse cillum dolore eu fugiat
        nulla pariatur. Excepteur sint occaecat cupidatat non proident,
        sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
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
    </section>

    <section id="bio" class="content">
      <div>
        <h2>Bio</h2>
        <p>Bristol born and raised, Neil Maggs is a descendent of a family of
          ironmongers who used to run a shop on Stapleton Road, Eastville, five
          generations ago. One of four children, Neil was a keen actor and a
          talented sportsman playing international football for England
          Schoolboys and also Southampton Academy. Wanting to pursue a career
          as a journalist, Neil obtained a BA English and Media degree before
          taking a brief detour getting heavily involved in the rave scene,
          firstly as an MC and later as a DJ (experience which would serve him
          well later in his career). He then worked for several years as a
          private investigator before heading back to university to acquire a
          Masters degree in Community Sport Development.</p>

        <p>Post university, Neil worked in the community support sector for 12
          years. In 2007 he set up Streetgames [insert link] in Bristol which
          delivered sport to deprived areas across the city. Streetgames has
          gone on to expand to all regions across the UK. After this he became
          a local authority development officer for Central and East Bristol, a
          South West Doorstep sport advisor for community projects specialising
          in diversity and improving access to minority groups and he also sat
          on the Bristol Mayoral City Office panel for sport.</p>

        <p>Getting frustrated at the lack of media attention in community sport,
          he began to appear on various radio shows and online platforms as a
          specialist in this area. He set up an award winning midweek sportsbar,
          which, at the time, was the only dedicated community support show in
          the city and beyond. The show recently won 'Best Community Radio Show'
          at the National Community Media Association awards.</p>

        <p>Neil then went on to create and found a TV version of Doorstep Sport
          [insert link] which is currently in its second season on Made in
          Bristol TV [insert link]. The show uses comedy as a vehicle to spread
          awareness of projects and stories in local communities. Neil is
          passionate about pushing through local voices and giving a voice to
          the voiceless. "People need to see and hear people like them, to push
          themselves forward in sport or other areas". Doorstep sport has given
          Neil a platform to interview some big names in sport, politics and
          other areas such as Bobby Reid, Lee Haskins, Greg Streete, Marvin
          Reese, John Landsdowne and George Furguson.</p>

        <p>Neil has become an experienced host, MCing at various events
          including Bristol Rovers FC, Gloucester Cricket, City Hall and
          European City of Sport. He has also appeared on various debates and
          panel discussions particularly around issues of representation of
          race and class in the media.</p>

        <p>Neil has more recently returned to serious journalism, pioneering
          the Bristol Born and Bred video series for Bristol Live [insert link],
          interviewing a range of sports stars in the city and visiting where
          they grew up. He has also written and presented a series of
          documentaries on the estates of Bristol, for the Bristol Cable, all
          showing a side to life in the city rarely shown. He has written for
          various outlets including the BBC, Bristol Post, Bristol 247, BCFM,
          Cable, BCFM, Made TV, Xtra Time and Connect Sport.</p>

        <p>Neil’s most recent work has seen him start a new podcast series for
          the Cable called Bristol Unpacked [insert link], and he is currently
          working on various documentary projects with BBC Radio 4. This was
          kickstarted by a show he made for the award winning Analysis programme
          called Whiteness [insert link].</p>

        <br/>
        <p><b>Awards include:</b><br/><br/>
        National Community radio show of the year winner - CMA 2017<br/>
        Best Radio presenter winner - Bristol Diversity Awards<br/>
        Best presenter nominee - South West Media Mogul Awards - 2018<br/>
        Best presenter nominee - South West Media Mogul Awards - 2019</p>
      </div>
    </section>

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
  </div>
</template>

<script>
import { gsap } from 'gsap';
import { ScrollToPlugin } from 'gsap/ScrollToPlugin';

gsap.registerPlugin(ScrollToPlugin);

export default {
  name: 'Home',
  props: {},
  data() {
    return {
      stickyNavActive: false,
      navLinkActive: null,
      navVisible: false,
      offsets: {
        pixelsTop: 60,
        pageY: null,
        nav: null,
        bio: null,
        work: null,
        contact: null,
      },
    };
  },
  methods: {
    setNavVisible(visible) {
      this.navVisible = visible;
    },
    scrollTo(toElem) {
      this.navLinkActive = toElem;
      console.log(toElem);
      // Temportary until I work out use gsap!
      // window.location.href = `#${toElem}`;
      gsap.to(window, { duration: 0.3, scrollTo: { y: `#${toElem}` }, ease: 'power2' });
    },
    onScroll() {
      this.offsets.pageY = window.pageYOffset;

      this.stickyNavActive = this.offsets.pageY >= this.offsets.nav;

      if (this.offsets.pageY >= this.offsets.work) {
        this.navLinkActive = 'work';
      }
      if (this.offsets.pageY >= this.offsets.bio) {
        this.navLinkActive = 'bio';
      }
      if (this.offsets.pageY >= this.offsets.contact) {
        this.navLinkActive = 'contact';
      }
    },
  },
  beforeMount() {
    if (window.location.hash) {
      this.navElementActive = window.location.href.substr(1);
    }
  },
  mounted() {
    window.addEventListener('scroll', this.onScroll);
    this.offsets.nav = document.getElementById('navbar').offsetTop - this.offsets.pixelsTop;
    this.offsets.bio = document.getElementById('bio').offsetTop - this.offsets.pixelsTop;
    this.offsets.work = document.getElementById('work').offsetTop - this.offsets.pixelsTop;
    this.offsets.contact = document.getElementById('contact').offsetTop - this.offsets.pixelsTop;
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.scroll {
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  height: 80px;
  width: 110px;
  bottom: 0;
  right: 60px;
  background: #676767;
  border-radius: 3px 3px 0 0;
  z-index: 10;

  a, a:visited, a:active, a:focus {
    color: #ffffff;
    font-size: 46px;

    animation-name: bouncing;
    animation-duration: 1.2s;
    animation-timing-function: ease-in;
    animation-iteration-count: infinite;
    animation-direction: normal;
  }

  @keyframes bouncing {
    0% { margin-top: -3px; }
    50% { margin-top: 9px; }
    100% { margin-top: -3px; }
  }
}

nav {
  border-radius: 3px;
  position: absolute;
  top: calc(100% + 60px);
  width: 110px;
  height: 260px;
  right: 60px;
  background: #676767;

  display: flex;
  justify-content: center;

  ul {
    width: 100%;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  li {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    list-style: none;
    flex-grow: 1;
    transition: all 0.3s;
    cursor: pointer;

    a, a:visited, a:active, a:focus {
      color: white;
      text-decoration: none;
      font-weight: 800;
    }

    &:first-child {
      border-radius: 3px 3px 0 0;
    }

    &:last-child {
      border-radius: 0 0 3px 3px;
    }

    &.active {
      background: #ffffff;
      a {
        color: #676767;
      }
    }
    &:hover {
      background: darken(#676767, 5%);
      a {
        color: white;
      }
    }
  }
}

.hamburger {
  display: none;
  width: 30px;
  // height: 60px;
  cursor: pointer;
  flex-direction: column;

  &.open {
    .line:nth-child(1) {
      transform: rotate(45deg) translateX(25%) translateY(50%);
      margin-left: -12.5%;
    }
    .line:nth-child(2) {
      background: none;
    }
    .line:nth-child(3) {
      transform: rotate(-45deg) translateX(25%) translateY(-50%);
      margin-left: -12.5%;
    }
  }

  .line {
    width: 100%;
    height: 3px;
    background: #232323;
    margin: 3px;
    transition: all 0.5s;
    border-radius: 1.5px;
  }
}

@media only screen and(max-width: 1024px) {

  .scroll {
    width: 100% !important;
    left: 0;
    bottom: 0;
  }

  nav {
    position: absolute;
    z-index: 100;
    width: 100%;
    right: 0;
    height: auto;
    top: 0 !important;

    ul {
      position: absolute;
      transform: translateY(-100%);
      background: #676767;
      width: 100%;
      height: 100vh;
      flex-direction: column;
      padding-top: 60px;
      transition: all 0.4s;

      li {
        opacity: 0;
        transform: translateY(-60%);
      }

      &.open {
        transform: translateY(0%);
        li {
          opacity: 1;
          transition: all 0.4s var(--delay);
          transform: translateY(0%);
        }
      }
    }

  }

  .hamburger {
    display: block;
    position: fixed;
    top: 20px;
    right: 30px;
    z-index: 100;

    &.open .line{
      background: #ffffff;
    }
  }

}

nav.sticky {
  position: fixed;
  top: 60px;
}

section {
  display: flex;
  min-height: 100vh;
  height: auto;
  align-items: center;
  justify-content: center;
  flex-direction: column;

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
}

#hero {
  text-align: center;
  color: #ffffff;

  .image {
    position: absolute;
    min-height:100%;
    width: 100%;
    height: auto;
    top: 0;
    left: 0;
    background: url('../assets/hero.png') no-repeat center center;
    background-size: cover;
  }

  *:not(.image) {
    z-index: 10;
  }

  h1 {
    margin-top: -100px;
    margin-bottom: 20px;
    font-size: 80px;
    padding-bottom: 20px;
    border-bottom: 1px solid #dcdcdc;
    text-shadow: 1px 1px 3px #696969;
    box-shadow: 0px 1px 0px #696969;
  }

  h2 {
    font-size: 28px;
    margin-top: 0;
    font-weight: normal;
    text-shadow: 1px 1px 3px #696969;
  }
}

#bio {
  background: #82AC9F;
  color: #fff;
  text-align: justify;
}

#work {
  color: #989898;
  h2 {
    border-bottom: 1px solid #989898;
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

#contact {
  background: #989898;
  color: #fff;

  .links {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
  }


  a, a:visited, a:active, a:focus {
    color: white;
    text-decoration: none;
    display: flex;
    align-items: center;
    padding: 10px 20px;
    transition: color 0.2s;
  }

  a:hover {
    color: #ddd;
  }

  i {
    font-size: 22px;
    padding-right: 10px;
  }
}
</style>
