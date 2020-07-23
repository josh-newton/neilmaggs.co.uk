<template>
  <div class="container">
    <div
      class="scroll"
      @click="scrollTo('about')">
      <a href="#about"><i class="fas fa-chevron-down"></i></a>
    </div>

    <nav
      id="navbar"
      @click="setNavVisible(!navVisible)"
      :class="{ sticky: stickyNavActive }">
      <ul :class="{ open: navVisible }">
        <li
          @click="scrollTo('about')"
          :class="{ active: navLinkActive == 'about'}">
          <a href="#about">About</a>
        </li>
        <li
          @click="scrollTo('work')"
          :class="{ active: navLinkActive == 'work'}">
          <a href="#work">Work</a>
        </li>
        <li
          @click="scrollTo('contact')"
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
      <h2>Journalist - Presenter - Host</h2>
    </section>

    <section id="about" class="content">
      <div>
        <h2>About</h2>
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
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
        enim ad minim veniam, quis nostrud exercitation ullamco laboris
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
        reprehenderit in voluptate velit esse cillum dolore eu fugiat
        nulla pariatur. Excepteur sint occaecat cupidatat non proident,
        sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </div>
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
        <div class="image"><p>Image</p></div>
        <div class="image"><p>Image</p></div>
        <div class="image"><p>Image</p></div>
        <div class="image"><p>Image</p></div>
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
        about: null,
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
      // Temportary until I work out use gsap!
      window.location.href = `#${toElem}`;
      // gsap.to(document.body, { duration: 1, scrollTo: 800 });
    },
    onScroll() {
      this.offsets.pageY = window.pageYOffset;

      this.stickyNavActive = this.offsets.pageY >= this.offsets.nav;

      if (this.offsets.pageY >= this.offsets.about) {
        this.navLinkActive = 'about';
      }
      if (this.offsets.pageY >= this.offsets.work) {
        this.navLinkActive = 'work';
      }
      if (this.offsets.pageY >= this.offsets.contact) {
        this.navLinkActive = 'contact';
      }
    },
  },
  beforeMount() {
    console.log(window.location.hash);
    if (window.location.hash) {
      this.navElementActive = window.location.href.substr(1);
    }
  },
  mounted() {
    window.addEventListener('scroll', this.onScroll);
    this.offsets.nav = document.getElementById('navbar').offsetTop - this.offsets.pixelsTop;
    this.offsets.about = document.getElementById('about').offsetTop - this.offsets.pixelsTop;
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
  background: #989898;
  border-radius: 3px 3px 0 0;
  z-index: 10;

  a, a:visited, a:active, a:focus {
    color: white;
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
  background: #d2d2d2;

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
      color: black;
      text-decoration: none;
    }

    &:first-child {
      border-radius: 3px 3px 0 0;
    }

    &:last-child {
      border-radius: 0 0 3px 3px;
    }

    &.active {
      background: #bbb;
      a {
        color: white;
      }
    }
    &:hover {
      background: #aaa;
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
      background: #d2d2d2;
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
      align-items: center;
      width: 60vw;
    }

    h2 {
      font-size: 28px;
      margin-top: 0;
      font-weight: normal;
      padding-bottom: 20px;
      border-bottom: 1px solid #aaaaaa;
      text-align: center;
      width: 80%;
    }
  }
}

#hero {
  text-align: center;
  color: #dcdcdc;

  .image {
    position: absolute;
    min-height:100%;
    width: 100%;
    height: auto;
    top: 0;
    left: 0;
    background: url('../assets/filmed-grey.jpg') no-repeat center center;
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
  }

  h2 {
    font-size: 28px;
    margin-top: 0;
    font-weight: normal;
  }
}

#about {
  background: #989898;
  color: #fff;
}

#work {
  color: #989898;

  .gallery {
    margin-top: 40px;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    align-items: flex-end;

    .image {
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 300px;
      height: 200px;
      background: #989898;
      margin: 10px;
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
