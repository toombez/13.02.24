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
                {props.title}
            </h1>

            <p>
                {props.content}
            </p>
        </article>
    )
}