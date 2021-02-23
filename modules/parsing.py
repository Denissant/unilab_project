def cv_parse(data):
    """
    contains a formula to calculate each respondent's rating
    determines whether their characteristics fit the requirements and stores the result into 'satisfied' variable
    """

    rating = 0
    good_qualities = ['teamwork', 'leadership', 'planning', 'negotiating', 'coaching']
    bad_buzzwords = ['creative', 'motivated', 'hard worker']

    for k in data:
        if type(data[k]) is str:
            data[k] = data[k].lower()
    if data['relevant_experience'] < 3 or data['age'] > 35 or data['age'] < 22 or data['school_diploma'] is False or data['bachelors_degree'] is False or data['driving_license'] is False:
        data.update({'satisfied': False})
    else:
        data.update({'satisfied': True})

    if data['last_position'].find('manager') > -1:
        rating += 3
    if data['bachelors_uni_faculty'].find('management') > -1:
        rating += 3
    if data['english_level'] > 7:
        rating += 1
    experience_bonus = data['relevant_experience'] - 3
    rating += experience_bonus
    qualities_list = data['skills_and_qualities'].split(', ')
    for q in qualities_list:
        if q in good_qualities:
            rating += 1
        elif q in bad_buzzwords:
            rating -= 0.5
    data.update({'rating': rating})
    return data
