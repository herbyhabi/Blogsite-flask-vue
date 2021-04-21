<template>
  <div class="about">
    <h1>文章标题: </h1>
    <Input type="text" v-model="title" placeholder="请输入100个字以内的标题" >
    </input>
    <a @click="publishArticle">发布文章</a>  
     <a @click="saveToDraftBox">保存为草稿</a>
    <Divider />
    <MarkdownEditor ref="child" v-on:listenChildEvent="getContentFromChild" />
    
  </div>
</template>

<script>
import axios from 'axios'
import MarkdownEditor from '@/components/MarkdownEditor.vue'
export default {
  data () {
          return {
              text: '',
              title: '',
              article_content: ''
              
          }
  }, 

  components: {
    MarkdownEditor
  },

  

  mounted(){
        this.init()
  },
  methods: {
      getContentFromChild: function(data){
      
        console.log(data)
        this.text = data
      },

      saveToDraftBox(){
      
      console.log(this.text)
      var that = this
      var parms = new URLSearchParams()
      parms.append('title', this.title)
      parms.append('content', this.text)
      parms.append('status', '0')
      
      
      // 通过路由判断是新建还是编辑文章
      if(this.$route.query.articleId == undefined){
        console.log('test')
        axios.post('http://localhost:5000/api/writeessay', parms).then(function (res) {
        // alert('保存成功')
        // that.$router.push({ path: '/' })
        console.log(res.data.article_id)
        that.$router.push({path: '/edit', query:{articleId: res.data.article_id}});
        console.log(that.$route.query)
        alert('保存成功！')
        
        })
      }
      else{
        var article_id = this.$route.query.articleId
        parms.append('article_id', article_id)
        axios.post('http://localhost:5000/api/update', parms).then(function (res) {
       
        console.log(res.data)
        // that.$router.push({path: '/edit', query:{articleId: res.data.article_id}});
        // console.log(that.$route.query)
        alert('保存成功！')
        
        })

      }
      },

      
      publishArticle(){
      
      console.log(this.text)
      var that = this
      var parms = new URLSearchParams()
      parms.append('title', this.title)
      parms.append('content', this.text)
      parms.append('status', '1')
      
      
      // 通过路由判断是新建还是编辑文章
      if(this.$route.query.articleId == undefined){
        console.log('test')
        axios.post('http://localhost:5000/api/writeessay', parms).then(function (res) {
        // alert('保存成功')
        // that.$router.push({ path: '/' })
        console.log(res.data.article_id)
        // that.$router.push({path: '/edit', query:{articleId: res.data.article_id}});
        // console.log(that.$route.query)
        alert('发布成功！')
        that.$router.push({path: '/'});

        
        })
      }
      else{
        var article_id = this.$route.query.articleId
        parms.append('article_id', article_id)
        axios.post('http://localhost:5000/api/update', parms).then(function (res) {
       
        console.log(res.data)
        // that.$router.push({path: '/edit', query:{articleId: res.data.article_id}});
        // console.log(that.$route.query)
        alert('发布成功!')
        that.$router.push({path: '/'});
        
        })
      }
  
        
      
      },

      init(){
        console.log('start')
        
        if (this.$route.query.articleId != undefined){
            console.log(this.$route.query.articleId)
            var parms = new URLSearchParams()
            parms.append('article_id', this.$route.query.articleId)
            var that = this
           axios.post('http://localhost:5000/api/details', parms).then(function (res) {
            // console.log(res.data.data)
            that.article_content = res.data.data[0].content
            that.title = res.data.data[0].title
            console.log(that.article_content)

            that.$refs.child.init(that.article_content);

            // 带查询参数
            // this.$router.push({path: '/details', query:{id: id}});

        })
        }

      },

      


  },
        
    
  
}
</script>
