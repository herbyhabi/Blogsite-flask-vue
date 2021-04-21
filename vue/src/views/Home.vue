<template>
  <div class="home">
    <HelloWorld />
    <ArticleList v-bind:list="article_list"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import ArticleList from '../components/Article_list.vue'

import axios from "axios"

export default {
  name: 'Home',
  data () {
    return {
      article_list: []
    }
  },
  components: {
    HelloWorld,
    ArticleList
  },

  mounted(){
    this.getArticleList()
  },

  methods:{
    getArticleList(){
      var that = this
      axios.get('http://localhost:5000/api/list').then(function (res) {
        that.article_list = res.data
        console.log(that.article_list)
      })
    }
  }
}
</script>
