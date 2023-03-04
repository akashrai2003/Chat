def fetch_stats(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    # fetching number of messages
    num_messages = df.shape[0]
    # fetching number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetching number of media messages
    num_media_messages = df[df['message'] == <Media omitted>\n'].shape[0]

    return num_messages, len(words), num_media_messages
