import { useState, useEffect } from "react"
import Post from "./Post"
import { ofetch } from 'ofetch'

function App() {
    const [posts, setPosts] = useState([])

    useEffect(() => {
        refreshPosts()
    }, [])

    async function refreshPosts() {
        const responce = await ofetch('http://127.0.0.1:5000/api/post/')
        setPosts(() => responce?.objects || [])
    }

    return (
        <div>
            <button onClick={refreshPosts}>
                refresh
            </button>

            {posts.map((post) => <Post key={post.id} post={post} />)}
        </div>
    )
}

export default App