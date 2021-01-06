<template>
  <div class="wrapper flexBox flexCol">
    <div class="flex1 autoBox">
      <router-view></router-view>
    </div>
    <div class="navTab flexBox">
      <div @click="setIndex(1)" class="flex1 center flexBox flexCol">
        <img v-show="currentIndex != 1" class="thisIcon" src="../../assets/icons/home.png" alt="">
        <img v-show="currentIndex == 1" class="thisIcon" src="../../assets/icons/home1.png" alt="">
        <router-link :class="{active: (currentIndex == 1),notActive:(currentIndex != 1)}"  to="firstPage">step1</router-link>
      </div>
      <div @click="setIndex(2)" class="flex1 center flexBox flexCol">
        <img v-show="currentIndex != 2" class="thisIcon" src="../../assets/icons/comments.png" alt="">
        <img v-show="currentIndex == 2" class="thisIcon" src="../../assets/icons/comments1.png" alt="">
        <router-link :class="{active: (currentIndex == 2),notActive:(currentIndex != 2)}" to="secondPage">step2</router-link>
      </div>
      <div @click="setIndex(3)" class="flex1 center flexBox flexCol">
        <img v-show="currentIndex != 3" class="thisIcon" src="../../assets/icons/Category.png" alt="">
        <img v-show="currentIndex == 3" class="thisIcon" src="../../assets/icons/Category1.png" alt="">
        <router-link :class="{active: (currentIndex == 3),notActive:(currentIndex != 3)}" to="thirdPage">step3</router-link>
      </div>
      <div @click="setIndex(4)" class="flex1 center flexBox flexCol">
        <img v-show="currentIndex != 4" class="thisIcon" src="../../assets/icons/account.png" alt="">
        <img v-show="currentIndex == 4" class="thisIcon" src="../../assets/icons/account1.png" alt="">
        <router-link :class="{active: (currentIndex == 4),notActive:(currentIndex != 4)}" to="forthPage">step4</router-link>
      </div>
      <div @click="setIndex(5)" class="flex1 center flexBox flexCol">
        <img v-show="currentIndex != 5" class="thisIcon" src="../../assets/icons/Category.png" alt="">
        <img v-show="currentIndex == 5" class="thisIcon" src="../../assets/icons/Category1.png" alt="">
        <router-link :class="{active: (currentIndex == 5),notActive:(currentIndex != 5)}" to="fifthPage">step5</router-link>
      </div>
      <div @click="setIndex(6)" class="flex1 center flexBox flexCol">
        <img v-show="currentIndex != 6" class="thisIcon" src="../../assets/icons/comments.png" alt="">
        <img v-show="currentIndex == 6" class="thisIcon" src="../../assets/icons/comments1.png" alt="">
        <router-link :class="{active: (currentIndex == 6),notActive:(currentIndex != 6)}" to="sixthPage">step6</router-link>
      </div>
      <div @click="setIndex(7)" class="flex1 center flexBox flexCol">
        <img v-show="currentIndex != 7" class="thisIcon" src="../../assets/icons/home.png" alt="">
        <img v-show="currentIndex == 7" class="thisIcon" src="../../assets/icons/home1.png" alt="">
        <router-link :class="{active: (currentIndex == 7),notActive:(currentIndex != 7)}" to="seventhPage">step7</router-link>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data: function () {
      return {
        currentIndex: 1
      }
    },
    methods: {
      setIndex: function(index){
        this.currentIndex = index
      }
    },
    watch: {
      $route: function(route){
        if(route.path == '/' || route.path == '/firstPage'){
          this.currentIndex = 1
        }
        if(route.path == '/secondPage'){
          this.currentIndex = 2;
        }
        if(route.path == '/thirdPage'){
          this.currentIndex = 3
        }
        if(route.path == '/forthPage'){
          this.currentIndex = 4
        }
        if(route.path == '/fifthPage'){
          this.currentIndex = 5
        }
        if(route.path == '/sixthPage'){
          this.currentIndex = 6
        }
        if(route.path == '/seventhPage'){
          this.currentIndex = 7
        }
      }
    }
  }
</script>

<style lang="scss" type="text/css" scoped>
  .navTab{
    height: 70px;
    background: #eeeeee;
  }
  .thisIcon{
    width: 25px;
    height: 25px;
  }
  .active{
    color: red;
    text-decoration: none;
  }
  .notActive{
    color: #999999;
    text-decoration: none;
  }
</style>
