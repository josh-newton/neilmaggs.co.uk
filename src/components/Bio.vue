<template>
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
</template>

<script>

export default {
  name: 'Bio',
  data() {
    return {};
  },
  methods: {},
};
</script>

<style scoped lang="scss">
#bio {
  background: #82AC9F;
  color: #fff;
  text-align: justify;
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
</style>
