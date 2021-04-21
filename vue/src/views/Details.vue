<template>
  <div>
      <a @click="modifyEvent">编辑</a>
      <a @click="deleteArticle">删除</a>
      <ArticleContent v-bind:articleInfo="article_info"/>
      <div>提示：{{this.$route.query}}</div>
  </div>
</template>

<script>
import ArticleContent from '@/components/Article_content.vue'
import axios from 'axios'
export default {
  data () {
    return {
      id: '',
      article_info: []

    }
  },
  components: {
    ArticleContent
  },

  mounted () {
    this.getArticleDetails()
  },
  methods: {

    getArticleDetails () {
      this.id = this.$route.query.articleId
      var parms = new URLSearchParams()
      parms.append('article_id', this.id)
      var that = this
      axios.post('http://localhost:5000/api/details', parms).then(function (res) {
        // console.log(res.data.data)
        that.article_info = res.data.data[0]

        // 带查询参数
        // this.$router.push({path: '/details', query:{id: id}});
      })
    },

    deleteArticle () {
      var parms = new URLSearchParams()
      parms.append('article_id', this.id)
      var that = this
      axios.post('http://localhost:5000/api/delete', parms).then(function (res) {
        console.log(res.data)
        if (res.data.data == 1) {
          this.$router.push({ path: '/' })
        }
      })
    },
    modifyEvent () {
      this.$router.push({ path: '/edit', query: { articleId: this.id } })
    }

  }
}
</script>
