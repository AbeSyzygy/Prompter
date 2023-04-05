def parseText(file_path):
    with open(file_path, "r") as f:
        sentences = f.readlines()

    sentences = [s.strip() for s in sentences]

    weight_idx = []
    i = 0
    for s in sentences:
        if ":" in s:
            num_pos = (sentences[i]).index(":") + 1
            weight_idx.append(int(s[num_pos]))
            s = s[:num_pos-1]
            sentences[i] = s
        else:
            weight_idx.append(1)
        i = i + 1
    prompts_weighted = []
    for i, s in enumerate(sentences):
        for chance in range(weight_idx[i]):
            prompts_weighted.append(s)

    return prompts_weighted