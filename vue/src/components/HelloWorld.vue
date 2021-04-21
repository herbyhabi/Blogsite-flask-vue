<template>
  <div class="test">
    <a @click="newArticle">{{msg}}</a>

  </div>
</template>

<script>
export default {
  props: {
    msg: {
      type: String,
      default: '写文章'
    },
    list: Object
  },

  methods: {
    newArticle () {
      this.$router.push({ path: '/edit' })
    }

  }
}
</script>
