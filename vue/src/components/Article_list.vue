<template>
    <List item-layout="vertical">
        <ListItem v-for="item in list" :key="item.id">
            <h2 v-show="true" @click="goToDetailsPage(item.id)">{{item.title}}</h2>
            <ListItemMeta :description="item.time"/>
            <!-- {{ item.content }} -->
            <!-- <template slot="action">
                <li>
                    <Icon type="ios-star-outline" /> 123
                </li>
                <li>
                    <Icon type="ios-thumbs-up-outline" /> 234
                </li>
                <li>
                    <Icon type="ios-chatbubbles-outline" /> 345
                </li>
            </template> -->
            <template slot="extra">
                <img src="https://dev-file.iviewui.com/5wxHCQMUyrauMCGSVEYVxHR5JmvS7DpH/large" style="width: 280px">
            </template>
        </ListItem>
    </List>
</template>
<script>
import axios from "axios"
    export default {
        data () {
            return {
                article_id: '',
                data: [
                    {
                        title: 'This is title 1',
                        description: 'This is description, this is description, this is description.',
                        avatar: 'https://dev-file.iviewui.com/userinfoPDvn9gKWYihR24SpgC319vXY8qniCqj4/avatar',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'This is title 2',
                        description: 'This is description, this is description, this is description.',
                        avatar: 'https://dev-file.iviewui.com/userinfoPDvn9gKWYihR24SpgC319vXY8qniCqj4/avatar',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'This is title 3',
                        description: 'This is description, this is description, this is description.',
                        avatar: 'https://dev-file.iviewui.com/userinfoPDvn9gKWYihR24SpgC319vXY8qniCqj4/avatar',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    }
                ]
            }
        },

        props: {
            list: Object
        },

    methods:{
        goToDetailsPage(id){
        
        // var parms = new URLSearchParams()
        // parms.append('article_id', id)
        // var that = this
        // axios.post('http://localhost:5000/api/details', parms).then(function (res) {
        //     console.log(res.data)
        //     // 带查询参数
            this.$router.push({path: '/details', query:{articleId: id}});

        // })
        }
    }

    }
</script>
