def high_score(scores:list) -> None:
    h_score = scores[0]
    for score in scores[1:]:
        if score > h_score:
            h_score = score
    print(f'The highest score in the class is: {h_score}')