import { useState, useEffect } from "react"
import Post from "./Post"
import { ofetch } from 'ofetch'

function App() {
    const [posts, setPosts] = useState([])

    useEffect(() => {
        ofetch('http://127.0.0.1:5000/api/post/')
            .then((r) => {
                console.log(r);

                setPosts(() => r?.objects || [])
            })
    }, [])

    return (
        <div>
            {posts.map((post) => <Post post={post} />)}
        </div>
    )
}

export default App