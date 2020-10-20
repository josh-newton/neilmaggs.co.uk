<template>
  <span>
    <nav @click="navVisible = !navVisible">
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
      @click="navVisible = !navVisible">
      <div class="line"></div>
      <div class="line"></div>
      <div class="line"></div>
    </div>
  </span>
</template>

<script>
import { gsap } from 'gsap';
import { ScrollToPlugin } from 'gsap/ScrollToPlugin';

gsap.registerPlugin(ScrollToPlugin);

export default {
  name: 'Nav',
  data() {
    return {
      navLinkActive: null,
      navVisible: false,
    };
  },
  mounted() {
    window.addEventListener('resize', this.windowResize);
  },
  methods: {
    scrollTo(toElem) {
      this.navLinkActive = toElem;
      gsap.to(window, { duration: 0.3, scrollTo: { y: `#${toElem}` }, ease: 'power2' });
    },
    windowResize() {
      if (window.innerWidth >= 768) {
        this.navVisible = false;
      }
    },
  },
};
</script>

<style scoped lang="scss">
nav {
  position: absolute;
  width: 100%;
  background: rgba(255, 255, 255, 0);
  display: flex;
  padding: 2em;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  transition: background 0.3s;

  &:hover {
    background: rgba(255, 255, 255, 0.5);
  }

  ul {
    width: 550px;
    list-style: none;
    display: flex;
    justify-content: space-around;
    margin-left: auto;
  }

  li {
    font-size: 18px;

    a {
      color: #1e272e;
      font-weight: bold;
      text-decoration: none;
    }
  }
}

.hamburger {
  display: none;
  width: 30px;
  cursor: pointer;
  flex-direction: column;

  &.open {
    .line:nth-child(1) {
      transform: rotate(45deg) translateX(32.5%) translateY(50%);
      margin-left: -5%;
    }
    .line:nth-child(2) {
      background: none;
    }
    .line:nth-child(3) {
      transform: rotate(-45deg) translateX(32.5%) translateY(-50%);
      margin-left: -5%;
    }
  }

  .line {
    width: 100%;
    height: 3px;
    background: #1e272e;
    margin: 5px;
    transition: all 0.3s;
    border-radius: 1.5px;
  }
}

@media only screen and(max-width: 768px) {

  .hamburger {
    display: block;
    position: fixed;
    top: 15px;
    right: 15px;
    z-index: 100;
  }

  nav {
    position: fixed;
    z-index: 100;
    width: 100%;
    height: auto;
    top: -20px !important;
    padding: 15px 0;

    ul {
      position: absolute;
      transform: translateY(-100%);
      width: 100%;
      height: calc(100vh + 20px);
      flex-direction: column;
      padding-top: 60px;
      transition: all 0.4s;
      margin-bottom: 0;
      background: white;

      li {
        opacity: 0;
        transform: translateY(-60%);
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;

        &:hover {
          background: rgba(0,0,0,0.4);
        }
        &.active {
          background: rgba(0,0,0,0.1);

          a {
            color: #91332b;
          }
        }
      }

      &.open {
        transform: translateY(0%);
        li {
          opacity: 1;
          transition: all 0.4s 0.2s;
          transform: translateY(0%);

          &:nth-child(2) {
            transition: all 0.4s 0.3s;
          }

          &:nth-child(3) {
            transition: all 0.4s 0.4s;
          }
        }
      }
    }

  }
}
</style>
