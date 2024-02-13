function Post(props) {
    return (
        <article
            style={{
                border: '1px solid black',
                padding: 8,
                borderRadius: 8
            }}
        >
            <h1>
                {props.post.title}
            </h1>

            <p>
                {props.post.content}
            </p>
        </article>
    )
}

export default Post