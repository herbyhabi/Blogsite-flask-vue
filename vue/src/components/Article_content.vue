<template>
    <div style="background:#eee;padding: 20px">
        <Card :bordered="false">
            <p slot="title">
                {{articleInfo.title}}


            </p>
            <p>{{articleInfo.content}}</p>
        </Card>
    </div>
</template>
<script>
    export default {
        props: {
            articleInfo: Object
        },
    }
</script>
