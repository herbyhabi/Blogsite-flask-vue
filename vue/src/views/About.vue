<template>
  <div class="about">
    <h1>文章标题</h1>
    <QuillEditor />
  </div>
</template>

<script>
import QuillEditor from '@/components/MarkdownEditor.vue'
export default {
  components: {
    QuillEditor
  }

}
</script>
